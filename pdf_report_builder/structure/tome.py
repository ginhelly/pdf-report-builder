from dataclasses import dataclass, field
from typing import List
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.utils.parsing import continue_on_key_error

@dataclass
class Tome:
    """
    Том техотчета
    """
    basename: str
    human_readable_name: str = 'Новый том'
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

    @continue_on_key_error
    @staticmethod
    def from_dict(d: dict):
        d['structural_elements'] = [
            StructuralElement.from_dict(el) for el in d['structural_elements']
        ]
        return Tome(**d)
    

    

    