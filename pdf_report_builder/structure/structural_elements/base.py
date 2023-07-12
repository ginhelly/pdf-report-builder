from dataclasses import dataclass, field
from typing import List
from pathlib import Path
from typing import NamedTuple
from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.structure.level import BaseLevel
from pdf_report_builder.utils.file_watcher import FileWatcher

class FileDescription(NamedTuple):
    path: Path
    subset: str

@dataclass
class StructuralElement(BaseLevel):
    name: str = "Структурный элемент"
    computed: int = 0
    enumeration_include: bool = True
    enumeration_print: bool = True
    create_bookmark: bool = True
    code_attr: str = ""
    files: List[PDFFile] = field(
        default_factory=lambda: []
    )
    subelements: List[BaseLevel] = field(
        default_factory=lambda: []
    )
    expanded: bool = True
    code_add: bool = False
    inner_enumeration: bool = False

    def __repr__(self) -> str:
        return f'StructuralElement([{self.code_attr}] {self.name}; files={len(self.files)} & subelements={len(self.subelements)})'

    def add_file(
            self,
            file: PDFFile | None = None,
            file_description: FileDescription | None = None,
            file_path: Path | None = None,
            subset: str | None = None
        ):
        if file is not None:
            new_file = file
        elif file_description is not None:
            new_file = PDFFile(*file_description)
        else:
            new_file = PDFFile(file_path, subset)
        FileWatcher().add_file(new_file)
        self.files.append(new_file)
    
    def add_subelement(
            self,
            element: BaseLevel
    ):
        self.subelements.append(element)
    
    def parse_files(self, files: list[FileDescription]):
        for file in files:
            self.add_file(file_description=file)
    
    def remove_file(self, file: PDFFile | int):
        if isinstance(file, PDFFile):
            FileWatcher().remove_file(file)
            if file in self.files:
                self.files.remove(file)
        elif isinstance(file, int):
            pdffile = self.files[file]
            FileWatcher().remove_file(pdffile)
            self.files.remove(pdffile)
    
    def remove_element(self, el: BaseLevel | int):
        if isinstance(el, StructuralElement):
            if el in self.subelements:
                self.subelements.remove(el)
        elif isinstance(el, int):
            self.subelements.remove(self.subelements[el])
    
    @property
    def pages_number(self):
        """Возвращает число страниц внутри структурного элемента без учета вложенных элементов"""
        return sum(file.subset_pages_number for file in self.files)
    
    @property
    def code(self):
        return self.code_attr
