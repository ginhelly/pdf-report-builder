from dataclasses import dataclass
from pathlib import Path
import json
from pdf_report_builder.structure.version import Version
from pdf_report_builder.project.settings import ProjectSettings
from pdf_report_builder.project.base_project import BaseReportProject
from pdf_report_builder.project.io.serializer import write_to_file, read_from_file

class ReportProject(BaseReportProject):
    """Управление документами проектов техотчетов"""

    def __init__(
            self,
            versions: list[Version] | None = None,
            settings: ProjectSettings | None = None
        ) -> None:
        """
        Создать проект техотчета
        -versions: список версий структуры проекта
        -settings: датакласс ProjectSettings
        """
        self.versions = versions or []
        self.settings = settings or ProjectSettings()

    def save(self):
        write_to_file(self)
    
    def rename(self, new_name: str):
        self.settings.name = new_name
    
    def save_as(self, new_path: Path):
        self.settings.savepath = new_path
        self.save()
    
    @staticmethod
    def open(path: Path):
        project = read_from_file(path)
        project.savepath = path