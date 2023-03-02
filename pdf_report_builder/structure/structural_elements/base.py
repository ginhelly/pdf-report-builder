from dataclasses import dataclass
from pathlib import Path
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.structure.files.pages_subset import PagesSubset

@dataclass
class StructuralElement:
    name: str
    official: bool
    code_attr: str
    tome: Tome | None

    def __post_init__(self):
        self.files = []
    
    def add_file(self, file_path: Path, pages: str):
        subset = PagesSubset.from_string(pages)
        new_file = PDFFile(file_path, subset)
        self.files.append(new_file)
