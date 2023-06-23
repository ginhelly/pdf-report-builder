from dataclasses import dataclass, field
from typing import List
from pathlib import Path
from typing import NamedTuple
from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.structure.structural_elements.common import ElementScheme
from pdf_report_builder.structure.level import BaseLevel

class FileDescription(NamedTuple):
    path: Path
    subset: str

@dataclass
class StructuralElement(BaseLevel):
    name: str = "Структурный элемент"
    official: bool = False
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
        self.files.append(new_file)
    
    def add_subelement(
            self,
            element: BaseLevel | ElementScheme | dict
    ):
        if isinstance(element, dict):
            new_subelement = StructuralElement.from_dict(element)
        elif isinstance(element, ElementScheme):
            new_subelement = StructuralElement.from_scheme(element)
        else:
            new_subelement = element
        self.subelements.append(new_subelement)
    
    def parse_files(self, files: list[FileDescription]):
        for file in files:
            self.add_file(file_description=file)
    
    def remove_file(self, file: PDFFile | int):
        if isinstance(file, PDFFile):
            if file in self.files:
                self.files.remove(file)
        elif isinstance(file, int):
            self.files.remove(
                self.files[file]
            )
    
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
    
    @staticmethod
    def from_dict(d: dict):
        d['official'] = True \
            if not 'official' in d or d['official'] == 'True' \
            else False
        d['enumeration_include'] = True \
            if not 'enumeration_include' in d or d['enumeration_include'] == 'True' \
            else False
        d['enumeration_print'] = True \
            if not 'enumeration_print' in d or d['enumeration_print'] == 'True' \
            else False
        d['create_bookmark'] = True \
            if not 'create_bookmark' in d or d['create_bookmark'] == 'True' \
            else False
        if 'files' in d:
            d['files'] = [PDFFile.from_dict(file) for file in d['files']]
        if 'subelements' in d:
            d['subelements'] = [StructuralElement.from_dict(el) for el in d['subelements']]
        valid = ['name', 'official', 'code_attr', 'files', 'subelements', 'enumeration_include', 'enumeration_print', 'create_bookmark']
        for key in list(d.keys()):
            if not key in valid:
                del d[key]
        return StructuralElement(**d)

    @staticmethod
    def from_scheme(scheme: ElementScheme):
        new_element = StructuralElement(
            name=scheme.name,
            official=scheme.official,
            enumeration_include=scheme.enumeration_include,
            enumeration_print=scheme.enumeration_print,
            code_attr=scheme.code_attr
        )
        return new_element
