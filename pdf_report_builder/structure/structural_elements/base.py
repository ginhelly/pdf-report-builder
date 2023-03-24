from dataclasses import dataclass, field
from typing import List
from pathlib import Path
from typing import NamedTuple
from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.structure.level import BaseLevel

class FileDescription(NamedTuple):
    path: Path
    subset: str

@dataclass
class StructuralElement(BaseLevel):
    name: str = "Структурный элемент"
    official: bool = False
    code_attr: str = ""
    files: List[PDFFile] = field(
        default_factory=lambda: []
    )

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
    
    def remove_file(self, file: PDFFile | int):
        if isinstance(file, PDFFile):
            if file in self.files:
                self.files.remove(file)
        elif isinstance(file, int):
            self.structural_elements.remove(
                self.files[file]
            )
    
    @property
    def pages_number(self):
        return sum(file.subset_pages_number for file in self.files)
    
    @staticmethod
    def from_dict(d: dict):
        d['official'] = True \
            if not 'official' in d or d['official'] == 'True' \
            else False
        if 'files' in d:
            d['files'] = [PDFFile.from_dict(file) for file in d['files']]
        valid = ['name', 'official', 'code_attr', 'files']
        for key in list(d.keys()):
            if not key in valid:
                del d[key]
        return StructuralElement(**d)

