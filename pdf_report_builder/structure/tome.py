from dataclasses import dataclass, field
from datetime import datetime
from os.path import expanduser
from pathlib import Path
from typing import List

from pdf_report_builder.structure.structural_elements.base import \
    StructuralElement
from pdf_report_builder.structure.level import BaseLevel

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

    def add_element(self, element: StructuralElement):
        self.structural_elements.append(element)
    
    def remove_element(self, element: StructuralElement | int):
        if isinstance(element, StructuralElement):
            self.structural_elements.remove(element)
        else:
            self.structural_elements.remove(
                self.structural_elements[element]
            )
    
    @property
    def pages_number(self):
        return sum(element.pages_number for element in self.structural_elements)

    @staticmethod
    def from_dict(d: dict):
        if 'savepath' in d:
            d['savepath'] = Path(d['savepath'])
        if 'structural_elements' in d:
            d['structural_elements'] = [
                StructuralElement.from_dict(el) for el in d['structural_elements']
            ]
        return Tome(**d)
    

    

    