import os
from pathlib import Path

from dataclasses import dataclass, field
from .computed import ComputedElement
from .computed_types import ComputedTypes
from pdf_report_builder.structure.tome import Tome

DEFAULT_TEMPLATE = Path(os.getcwd()) / 'pdf_report_builder' \
    / 'data' / 'computed_elements_templates' / 'tome_contents.docx'

@dataclass
class TomeContentsElement(ComputedElement):
    doc_template: Path = field(default=DEFAULT_TEMPLATE)

    def _get_tome(self):
        tome = None
        parent = self.parent
        while True:
            if type(parent) == Tome:
                tome = parent
                break
            parent = parent.parent
        return tome

    def make_pdf(self):
        tome = self._get_tome()

    @property
    def computed(self):
        return ComputedTypes.TOME_CONTENTS.value
    
    @computed.setter
    def computed(self, value):
        ...