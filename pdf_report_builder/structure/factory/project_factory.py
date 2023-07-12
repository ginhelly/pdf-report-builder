from pathlib import Path

from .base_factory import BaseFactory
from .settings_factory import SettingsFactory
from .version_factory import VersionFactory
from .dict_processors import DictProcessor
from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.project.settings import ProjectSettings
from pdf_report_builder.project.event_channel import EventChannel
from pdf_report_builder.utils.lock_file import create_lock_file
from pdf_report_builder.project.io.serializer import read_from_file

class ProjectFactory(BaseFactory):

    @staticmethod
    def open(path: Path):
        create_lock_file(path)
        project_as_dict = read_from_file(path)
        project = ProjectFactory.from_dict(
            project_as_dict,
            path
        )
        project.modified = False
        return project

    @staticmethod
    def from_dict(d: dict, path: Path | None):
        dict_processor = DictProcessor(d)
        dict_processor.parse_level(
                'settings',
                lambda settings_dict: SettingsFactory.from_dict(
                    settings_dict,
                    path
                ),
                ProjectSettings()
            )
        EventChannel().publish('settings_changed', d['settings'])
        dict_processor.parse_levels_list(
                'versions',
                lambda version_dict: VersionFactory.from_dict(version_dict)
            )
        dict_processor.remove_invalid_keys()
        return ReportProject(**dict_processor.d)