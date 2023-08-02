from dataclasses import dataclass, field
from typing import List
from pathlib import Path
from typing import NamedTuple
from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.structure.level import BaseLevel
from pdf_report_builder.utils.file_watcher import FileWatcher
from pdf_report_builder.structure.level_enum import NodeType

from settings import FILE_WATCHER

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

    def __post_init__(self):
        for file in self.files:
            file.parent = self
        for subel in self.subelements:
            subel.parent = self

    def __repr__(self) -> str:
        return f'StructuralElement([{self.code_attr}] {self.name}; files={len(self.files)} & subelements={len(self.subelements)})'
    
    def _handle_file_add(self, file: PDFFile, callback: callable):
        if FILE_WATCHER:
            FileWatcher().add_file(file)
        callback(file)
        file.parent = self
    
    def _handle_subel_add(self, subel, callback):
        callback(subel)
        subel.parent = self

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

        self._handle_file_add(
            new_file,
            lambda f: self.files.append(f)
        )
    
    def add_subelement(
            self,
            element: BaseLevel
    ):
        self._handle_subel_add(
            element,
            lambda x: self.subelements.append(x)
        )
    
    def insert_file(self, i: int, file: PDFFile):
        self._handle_file_add(
            file,
            lambda f: self.files.insert(i, f)
        )
    
    def insert_subelement(self, i: int, subel):
        self._handle_subel_add(
            subel,
            lambda x: self.subelements.insert(i, x)
        )
    
    def parse_files(self, files: list[FileDescription]):
        for file in files:
            self.add_file(file_description=file)
    
    def remove_file(self, file: PDFFile | int):
        if isinstance(file, PDFFile):
            if FILE_WATCHER:
                FileWatcher().remove_file(file)
            if file in self.files:
                self.files.remove(file)
        elif isinstance(file, int):
            pdffile = self.files[file]
            if FILE_WATCHER:
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
    
    @property
    def level(self):
        return NodeType.ELEMENT
    
    @property
    def tome(self):
        parent = self.parent
        while parent is not None:
            if parent.level == NodeType.TOME:
                return parent
            parent = parent.parent
        return None
    
    @property
    def is_computed(self):
        return self.computed > 0
    
    def append_child(self, child):
        if isinstance(child, PDFFile):
            self.add_file(file=child)
        elif hasattr(child, 'level') and child.level == NodeType.ELEMENT:
            self.add_subelement(child)
    
    def insert_child(self, i: int, child):
        if isinstance(child, PDFFile):
            self.insert_file(i, child)
        elif hasattr(child, 'level') and child.level == NodeType.ELEMENT:
            self.insert_subelement(i, child)
    
    def remove_child(self, child):
        if isinstance(child, PDFFile):
            self.remove_file(child)
        elif hasattr(child, 'level') and child.level == NodeType.ELEMENT:
            self.remove_element(child)
