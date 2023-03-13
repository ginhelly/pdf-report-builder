from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from pdf_report_builder.project.io.saveformats import saveformats

@dataclass
class ProjectSettings:
    savepath: Path
    name: str = f'Новый проект ({datetime.now()})'
    save_format: saveformats = saveformats.JSON_V01