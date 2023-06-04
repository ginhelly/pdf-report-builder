from dataclasses import dataclass, field
from datetime import datetime
from os.path import expanduser
from pathlib import Path
from typing import List

from pdf_report_builder.structure.structural_elements.base import \
    StructuralElement
from pdf_report_builder.structure.level import BaseLevel
from pdf_report_builder.project.storage_settings import SettingsStorage

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

    def add_element(self, element: StructuralElement):
        self.structural_elements.append(element)
    
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
    def input_pdfs_number(self):
        return sum(len(element.files) for element in self.structural_elements)

    @staticmethod
    def from_dict(d: dict):
        if 'savepath' in d:
            if SettingsStorage().settings.paths_relative:
                d['savepath'] = SettingsStorage().settings.savepath.parent / d['savepath']
            d['savepath'] = Path(d['savepath'])
        if 'structural_elements' in d:
            d['structural_elements'] = [
                StructuralElement.from_dict(el) for el in d['structural_elements']
            ]
        
        valid = ['basename', 'human_readable_name', 'savepath', 'structural_elements']
        for key in list(d.keys()):
            if not key in valid:
                del d[key]
        return Tome(**d)
    

    

    