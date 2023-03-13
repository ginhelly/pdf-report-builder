from dataclasses import dataclass
#from pdf_report_builder.structure.structural_elements.base import StructuralElement

@dataclass
class Tome:
    """
    Том техотчета
    """
    basename: str

    def __post_init__(self):
        self.structural_elements = []
    

    