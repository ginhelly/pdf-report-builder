import os
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.utils.logger import ProcessingLogger

from .base import StructuralElement

WORKING_DIR = Path(os.getenv('APPDATA')) / 'PDF_Report_Builder'

def _default_temp_path():
    return WORKING_DIR / f'TempFile{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.pdf'

@dataclass
class ComputedElement(StructuralElement):
    pdf_temp_path: Path = field(default_factory=_default_temp_path)
    enumeration_include: bool = False
    enumeration_print: bool = False
    create_bookmark: bool = True

    def make_pdf(self, logger: ProcessingLogger | None = None):
        ...

    @property
    def subelements(self):
        return []
    
    @property
    def file_exists(self):
        return self.pdf_temp_path.exists() \
            and self.pdf_temp_path.is_file()
    
    @property
    def files(self):
        if self.file_exists:
            file = PDFFile(self.pdf_temp_path)
            self._handle_file_add(file, lambda x: ...)
            return [file]
        return []
    
    @subelements.setter
    def subelements(self, value):
        ...
    
    @files.setter
    def files(self, value):
        ...
