from dataclasses import dataclass
from pathlib import Path
from typing import NamedTuple
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.files.input_pdf import PDFFile

class FileDescription(NamedTuple):
    path: Path
    subset: str

@dataclass
class StructuralElement:
    name: str
    official: bool
    code_attr: str
    tome: Tome | None = None

    def __post_init__(self):
        self.files = []
    
    def add_file(
            self,
            file_description: FileDescription | None = None,
            file_path: Path | None = None,
            subset: str | None = None
        ):
        if file_description is None:
            new_file = PDFFile(file_path, subset)
        else:
            new_file = PDFFile(*file_description)
        self.files.append(new_file)
    
    def parse_files(self, files: list[FileDescription]):
        for file in files:
            self.add_file(file_description=file)
    
    @property
    def pages_number(self):
        return sum(file.subset_pages_number for file in self.files)

