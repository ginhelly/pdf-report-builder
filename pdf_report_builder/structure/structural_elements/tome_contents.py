import os
from pathlib import Path

from dataclasses import dataclass, field
from .computed import ComputedElement
from pdf_report_builder.project.storage_settings import SettingsStorage

DEFAULT_TEMPLATE = Path(os.getcwd()) / 'pdf_report_builder' \
    / 'data' / 'computed_elements_templates' / 'tome_contents.docx'

@dataclass
class TomeContentsElement(ComputedElement):
    doc_template: Path = field(default=DEFAULT_TEMPLATE)