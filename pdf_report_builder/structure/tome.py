from dataclasses import dataclass

@dataclass
class Tome:
    """
    Том техотчета
    """
    basename: str

    def __post_init__(self):
        self.structural_elements = []