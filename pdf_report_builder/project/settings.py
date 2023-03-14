import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from pdf_report_builder.project.io.saveformats import saveformats

WORKING_DIR = Path(os.getenv('APPDATA')) / 'PDF_Report_Builder'

@dataclass
class ProjectSettings:
    savepath: Path = WORKING_DIR / f'Project{datetime.now()}'
    name: str = f'Новый проект ({datetime.now()})'
    save_format: saveformats = saveformats.JSON_V01