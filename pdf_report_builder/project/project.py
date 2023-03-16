from dataclasses import dataclass
from pathlib import Path
import json
from pdf_report_builder.structure.version import Version
from pdf_report_builder.project.settings import ProjectSettings
from pdf_report_builder.project.base_project import BaseReportProject
from pdf_report_builder.project.io.serializer import write_to_file, read_from_file
from pdf_report_builder.utils.parsing import continue_on_key_error

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
        project_as_dict = read_from_file(path)
        project = ReportProject.from_dict(project_as_dict)
        project.settings.savepath = path
        return project
    
    @continue_on_key_error
    @staticmethod
    def from_dict(d: dict):
        d['settings'] = ProjectSettings.from_dict(d['settings'])
        d['versions'] = [
            Version.from_dict(ver) for ver in d['versions']
        ]
        return ReportProject(**d)
    