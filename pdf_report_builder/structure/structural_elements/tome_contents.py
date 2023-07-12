import os
from pathlib import Path

from dataclasses import dataclass, field
from .computed import ComputedElement
from .computed_types import ComputedTypes

DEFAULT_TEMPLATE = Path(os.getcwd()) / 'pdf_report_builder' \
    / 'data' / 'computed_elements_templates' / 'tome_contents.docx'

@dataclass
class TomeContentsElement(ComputedElement):
    doc_template: Path = field(default=DEFAULT_TEMPLATE)

    @property
    def computed(self):
        return ComputedTypes.TOME_CONTENTS.value
    
    @computed.setter
    def computed(self, value):
        ...