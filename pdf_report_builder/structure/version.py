from dataclasses import dataclass, field
from pathlib import Path
from typing import List

from pdf_report_builder.structure.level_enum import NodeType
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.level import BaseLevel


@dataclass
class Version(BaseLevel):
    name: str = "По умолчанию"
    tomes: List = field(
        default_factory=lambda: [Tome('.ИГДИ')]
    )
    code: str = '0000.000.КИИ.0/0.0000'
    comments: str = ''

    def __post_init__(self):
        super().__post_init__()
        for tome in self.tomes:
            tome.parent = self
    
    def create_tome(
        self,
        basename: str,
        human_readable_name: str,
        savepath: Path
    ):
        new_tome = Tome(basename, human_readable_name, savepath)
        self.append_tome(new_tome)

    def append_tome(self, tome: Tome):
        self.tomes.append(tome)
        tome.parent = self
    
    def remove_tome(self, tome: Tome | int):
        if isinstance(tome, Tome) and tome in self.tomes:
            self.tomes.remove(tome)
        elif type(tome) == int:
            self.tomes.remove(self.tomes[tome])
    
    @property
    def level(self):
        return NodeType.VERSION
    
    def append_child(self, child):
        if isinstance(child, Tome):
            self.append_tome(child)
    
    def remove_child(self, child):
        if isinstance(child, Tome):
            self.remove_tome(child)
