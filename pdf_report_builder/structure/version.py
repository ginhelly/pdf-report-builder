from dataclasses import dataclass, field
from typing import List
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.utils.parsing import continue_on_key_error

@dataclass
class Version:
    name: str = "По умолчанию"
    tomes: List = field(
        default_factory=lambda: [Tome('ИГДИ')]
    )

    def add_tome(self, tome: Tome):
        self.tomes.append(tome)
    
    def remove_tome(self, tome: Tome | int):
        if isinstance(tome, Tome):
            self.tomes.remove(tome)
        else:
            self.tomes.remove(self.tomes[tome])
    
    @continue_on_key_error
    @staticmethod
    def from_dict(d: dict):
        d['tomes'] = [
            Tome.from_dict(tome) for tome in d['tomes']
        ]
        return Version(**d)
    