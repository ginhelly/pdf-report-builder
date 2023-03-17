from dataclasses import dataclass, field
from os.path import expanduser
from pathlib import Path
from typing import List

from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.level import BaseLevel


@dataclass
class Version(BaseLevel):
    name: str = "По умолчанию"
    default_folder: Path = Path(expanduser('~/Documents'))
    tomes: List = field(
        default_factory=lambda: [Tome('ИГДИ')]
    )

    def __post_init__(self):
        for tome in self.tomes:
            if tome.savepath.parent == Path(expanduser('~/Documents')):
                tome_filename = tome.savepath.name
                tome.savepath = self.default_folder / tome_filename

    def append_tome(self, tome: Tome):
        self.tomes.append(tome)
    
    def remove_tome(self, tome: Tome | int):
        if isinstance(tome, Tome):
            self.tomes.remove(tome)
        else:
            self.tomes.remove(self.tomes[tome])
    
    @staticmethod
    def from_dict(d: dict):
        if 'tomes' in d:
            d['tomes'] = [
                Tome.from_dict(tome) for tome in d['tomes']
            ]
        return Version(**d)
    