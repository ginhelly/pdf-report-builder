import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from pdf_report_builder.project.io.saveformats import saveformats
from pdf_report_builder.utils.parsing import continue_on_key_error

WORKING_DIR = Path(os.getenv('APPDATA')) / 'PDF_Report_Builder'

def _default_name():
    return f'New Project {datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'

@dataclass
class ProjectSettings:
    savepath: Path = WORKING_DIR / (_default_name() + '.json')
    name: str = _default_name()
    save_format: saveformats = saveformats.JSON_V01

    @continue_on_key_error
    @staticmethod
    def from_dict(d: dict):
        d['savepath'] = Path(d['savepath'])
        save_format = int(d['save_format'])
        try:
            d['save_format'] = saveformats(save_format)
        except ValueError:
            raise IOError('Неизвестный формат')
        return ProjectSettings(**d)