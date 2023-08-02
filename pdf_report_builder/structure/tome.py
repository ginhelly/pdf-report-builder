from dataclasses import dataclass, field
from datetime import datetime
from os.path import expanduser
from pathlib import Path
from typing import List

from pdf_report_builder.structure.structural_elements.base import \
    StructuralElement
from pdf_report_builder.structure.level import BaseLevel
from pdf_report_builder.structure.level_enum import NodeType

def _default_savepath():
    return Path(expanduser('~/Documents')) / f'Новый том {datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.pdf'

@dataclass
class Tome(BaseLevel):
    """
    Том техотчета
    """
    basename: str
    human_readable_name: str = 'Новый том'
    savepath: Path = field(default_factory=_default_savepath)
    structural_elements: List[StructuralElement] = field(
        default_factory=lambda: []
    )
    expanded: bool = True
    use_custom_enumeration_start: bool = False
    custom_enumeration_start: int = 0

    def __post_init__(self):
        super().__post_init__()
        for element in self.structural_elements:
            element.parent = self

    def __repr__(self) -> str:
        return f'Tome([{self.basename}] {self.human_readable_name}; {self.savepath})'

    def create_element(
        self,
        name: str,
        official: bool,
        code_attr: str = None
    ):
        new_element = StructuralElement(
            name, official,
            code_attr=code_attr
        )
        self.add_element(new_element)
    
    def create_empty_element(self):
        new_element = StructuralElement()
        self.add_element(new_element)
    
    def _handle_element_add(self, element: StructuralElement, callback: callable):
        callback(element)
        element.parent = self

    def add_element(self, element: StructuralElement):
        self._handle_element_add(
            element,
            lambda x: self.structural_elements.append(x)
        )
    
    def append_element(self, element: StructuralElement):
        self.add_element(element)
    
    def insert_element(self, i: int, element: StructuralElement):
        self._handle_element_add(
            element,
            lambda x: self.structural_elements.insert(i, x)
        )
    
    def remove_element(self, element: StructuralElement | int):
        if isinstance(element, StructuralElement):
            if element in self.structural_elements:
                self.structural_elements.remove(element)
        elif isinstance(element, int):
            self.structural_elements.remove(
                self.structural_elements[element]
            )
    
    @property
    def pages_number(self):
        return sum(element.pages_number for element in self.structural_elements)
    
    @property
    def code(self):
        return self.basename

    @property
    def input_pdfs_number(self):
        def count_files_recursive(el: StructuralElement):
            res = 0
            for subel in el.subelements:
                res += count_files_recursive(subel)
            res += len(el.files)
            return res
        return sum(count_files_recursive(element) for element in self.structural_elements)
    
    @property
    def level(self):
        return NodeType.TOME
    
    def append_child(self, child):
        if isinstance(child, StructuralElement):
            self.add_element(child)

    def insert_child(self, i: int, child):
        if isinstance(child, StructuralElement):
            self.insert_element(i, child)
    
    def remove_child(self, child):
        if isinstance(child, StructuralElement):
            self.remove_element(child)