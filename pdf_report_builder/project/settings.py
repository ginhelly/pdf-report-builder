import os
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from pdf_report_builder.project.io.saveformats import saveformats
from pdf_report_builder.structure.level import BaseLevel

WORKING_DIR = Path(os.getenv('APPDATA')) / 'PDF_Report_Builder'

def _default_name():
    return f'Новый проект {datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'

@dataclass
class ProjectSettings(BaseLevel):
    savepath: Path = field(
        default_factory=lambda: WORKING_DIR / (_default_name() + '.reportprj')
    )
    name: str = field(default_factory=_default_name)
    save_format: saveformats = saveformats.JSON_V01
    current_version_id: int = 0

    @staticmethod
    def from_dict(d: dict):
        if 'savepath' in d:
            d['savepath'] = Path(d['savepath'])
        if 'save_format' in d:
            save_format = int(d['save_format'])
            try:
                d['save_format'] = saveformats(save_format)
            except ValueError:
                raise IOError('Неизвестный формат')
        return ProjectSettings(**d)