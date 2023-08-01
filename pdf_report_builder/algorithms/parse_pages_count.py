from pathlib import Path
from typing import List, Optional
from dataclasses import dataclass, field

from pypdf import PdfReader

from pdf_report_builder.structure.level_enum import NodeType
from pdf_report_builder.paperformats.format import PaperFormatStorage
from pdf_report_builder.project.base_project import BaseReportProject
from pdf_report_builder.structure.level import BaseLevel
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.structure.files.input_pdf import PDFFile


@dataclass
class ParseReportNode:
    name: str
    type: NodeType
    pages_native: int = 0 # Сколько у элемента внутри PDF-страниц
    pages_a4: float = 0.0 # Сколько у элемента внутри страниц, эквивалентных A4
    enumeration: bool = True # Включать ли элемент в сквозную нумерацию
    current_page_number: int = 0 # Номер первой страницы элемента в сквозной нумерации
    children: List['ParseReportNode'] = field(default_factory=lambda: [])
    parent: Optional['ParseReportNode'] = None
    custom_tome_enum_start: int = -1 # Кастомный номер первой страницы тома
    level: Optional['BaseLevel'] = None
    code: str = '' # Сборный шифр элемента
    create_bookmark: bool = False # Создавать ли закладку на элементе
    page_number_in_pdf_tome: int = 0


class ProjectParser:
    def __init__(self, count_a4: bool = False):
        self.count_a4 = count_a4

    def _parse_pages_read_pdf(self, file: PDFFile):
        pages_native = file.subset_pages_number
        if not (file.path.exists() and file.path.is_file()):
            return (pages_native, 0)
        if not self.count_a4:
            return (pages_native, 0)
        
        reader = PdfReader(file.path)
        P = PaperFormatStorage()
        pages_a4 = 0.0
        
        for page_number in list(file.subset):
            page = reader.pages[page_number]
            width = page.mediabox.width * page.user_unit * 25.4 / 72 
            height = page.mediabox.height * page.user_unit * 25.4 / 72 
            paper_format = P.find_format_by_size(width, height)
            pages_a4 = pages_a4 + paper_format.multiple_of_a4
        return (pages_native, pages_a4)
            

    def _parse_pages_parse_file(self, file: PDFFile, parent: ParseReportNode):
        file_name = Path(file.path).name
        file_node = ParseReportNode(file_name, NodeType.FILE, parent=parent, level=file)
        parent.children.append(file_node)
        pages_native, pages_a4 = self._parse_pages_read_pdf(file)
        file_node.pages_native = pages_native
        file_node.pages_a4 = pages_a4

    def _parse_pages_parse_element(self, element: StructuralElement, parent: ParseReportNode):
        element_node = ParseReportNode(element.name, NodeType.ELEMENT, parent=parent, level=element)
        parent.children.append(element_node)
        self.set_code(element_node)
        for subel in element.subelements:
            self._parse_pages_parse_element(subel, element_node)
        for file in element.files:
            self._parse_pages_parse_file(file, element_node)
        element_node.pages_a4 += sum(
            node.pages_a4 for node in element_node.children if node.type == NodeType.FILE
        )
        element_node.pages_native += sum(
            node.pages_native for node in element_node.children if node.type == NodeType.FILE
        )
        element_node.pages_a4 += sum(
            node.pages_a4 for node in element_node.children if node.type == NodeType.ELEMENT
        )
        element_node.pages_native += sum(
            node.pages_native for node in element_node.children if node.type == NodeType.ELEMENT
        )
        if not element.enumeration_include:
            element_node.enumeration = False
        if element.create_bookmark:
            element_node.create_bookmark = True


    def _parse_pages_parse_tome(self, tome: Tome, parent: ParseReportNode):
        custom_enum = tome.custom_enumeration_start \
            if tome.use_custom_enumeration_start \
            else -1
        tome_node = ParseReportNode(
            tome.human_readable_name, 
            NodeType.TOME, 
            parent=parent,
            custom_tome_enum_start=custom_enum,
            level=tome
        )
        parent.children.append(tome_node)
        self.set_code(tome_node)
        for element in tome.structural_elements:
            self._parse_pages_parse_element(element, tome_node)
        tome_node.pages_a4 += sum(
            node.pages_a4 for node in tome_node.children
        )
        tome_node.pages_native += sum(
            node.pages_native for node in tome_node.children
        )

    def count_pages_recursive(self, node: ParseReportNode, n: int = 1):
        if node.type == NodeType.TOME and node.custom_tome_enum_start > -1:
            n = node.custom_tome_enum_start
        node.current_page_number = n
        if node.type == NodeType.FILE:
            return n + node.pages_native
        if node.type == NodeType.ELEMENT:
            subel_nodes = [child for child in node.children if child.type == NodeType.ELEMENT]
            for subel in subel_nodes:
                n = self.count_pages_recursive(subel, n)
            if node.enumeration:
                file_nodes = [child for child in node.children if child.type == NodeType.FILE]
                for file in file_nodes:
                    n = self.count_pages_recursive(file, n)
            return n
        for child in node.children:
            n = self.count_pages_recursive(child, n)
        return n

    def set_code(self, node: ParseReportNode):
        code = node.level.code
        parent = node.parent
        if parent is not None:
            code = parent.code + code
        node.code = code

    def calculate_page_number_in_tome_recursive(self, node: ParseReportNode, index: int = 0):
        if node.type in (NodeType.TOME, NodeType.VERSION):
            index = 0
            for child in node.children:
                index += self.calculate_page_number_in_tome_recursive(child, index)
        elif node.type == NodeType.ELEMENT:
            node.page_number_in_pdf_tome = index
            subelements = filter(
                lambda child: child.type == NodeType.ELEMENT,
                node.children
            )
            for subel in subelements:
                index += self.calculate_page_number_in_tome_recursive(subel, index)
            index += node.level.pages_number
        return index
            
    def parse_project_for_pages(self, project: BaseReportProject):
        ver = project.get_current_version()
        root_node = ParseReportNode(ver.name, NodeType.VERSION, level=ver)
        self.set_code(root_node)
        for tome in ver.tomes:
            self._parse_pages_parse_tome(tome, root_node)
        root_node.pages_a4 += sum(
            node.pages_a4 for node in root_node.children
        )
        root_node.pages_native += sum(
            node.pages_native for node in root_node.children
        )
        self.count_pages_recursive(root_node)
        self.calculate_page_number_in_tome_recursive(root_node)
        return root_node
    
    def get_tome_node(self, root_node: ParseReportNode, tome):
        for node in root_node.children:
            if tome is node.level:
                return node
        return None