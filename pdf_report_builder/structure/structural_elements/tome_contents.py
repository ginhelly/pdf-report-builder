import os
from pathlib import Path

from docx import Document
from docx2pdf import convert as docx2pdf_convert
import fitz

from dataclasses import dataclass, field
from .computed import ComputedElement
from .computed_types import ComputedTypes
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.algorithms.parse_pages_count import ProjectParser, ParseReportNode
from pdf_report_builder.project.storage import ProjectStorage
from pdf_report_builder.utils.logger import ProcessingLogger
from pdf_report_builder.utils.app_settings import AppSettings

DEFAULT_TEMPLATE = AppSettings.get('DATA_PATH') / 'computed_elements_templates' / 'tome_contents.docx'

@dataclass
class TomeContentsElement(ComputedElement):
    doc_template: Path = field(default=DEFAULT_TEMPLATE)

    def _get_nodes_with_bookmark_recursive(self, node: ParseReportNode):
        for child in node.children:
            if child.create_bookmark:
                yield child
            yield from self._get_nodes_with_bookmark_recursive(child)

    def get_nodes_with_bookmark(self, root_node: ParseReportNode):
        return self._get_nodes_with_bookmark_recursive(root_node)

    def get_doc_temp_path(self):
        return self.pdf_temp_path.parent / (self.pdf_temp_path.stem + '.docx')
    
    def process_doc(self, node: ParseReportNode, logger: ProcessingLogger | None = None):
        doc = Document(self.doc_template)
        table = doc.tables[0]
        if not logger is None:
            logger.writeline('  Заполняю таблицу внутри шаблона')
        for i, node in enumerate(self.get_nodes_with_bookmark(node)):
            if i > 0:
                table.add_row()
            row = table.rows[-1]
            row.cells[0].text = node.code
            row.cells[1].text = node.name
            if node.current_page_number and node.current_page_number > 0:
                row.cells[2].text = f'с.{node.current_page_number}'
        
        if not logger is None:
            logger.writeline('  Сохраняю документ')
        doc_temp_path = self.get_doc_temp_path()
        doc.save(doc_temp_path)

    def make_pdf(self, logger: ProcessingLogger | None = None):
        tome = self.tome
        project = ProjectStorage().project

        if not logger is None:
            logger.writeline(f' Считаю номера страниц...')
            logger.set_fraction(3)

        parser = ProjectParser(count_a4=False)
        root_node = parser.parse_project_for_pages(project)
        tome_node = parser.get_tome_node(root_node, tome)

        if not logger is None:
            logger.add_fraction()
            logger.writeline(' Создаю временный документ Word из шаблона...')
        self.process_doc(tome_node)

        if not logger is None:
            logger.add_fraction()
            logger.writeline(' Преобразую документ в PDF...')
        docx2pdf_convert(
            self.get_doc_temp_path(),
            self.pdf_temp_path
        )
        os.remove(self.get_doc_temp_path())
        if not logger is None:
            logger.add_fraction()


    @property
    def computed(self):
        return ComputedTypes.TOME_CONTENTS.value
    
    @computed.setter
    def computed(self, value):
        ...