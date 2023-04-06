from dataclasses import dataclass
from copy import deepcopy
from pathlib import Path
import json
from pdf_report_builder.structure.version import Version
from pdf_report_builder.project.settings import ProjectSettings
from pdf_report_builder.project.base_project import BaseReportProject
from pdf_report_builder.project.io.serializer import write_to_file, read_from_file
from pdf_report_builder.project.event_channel import EventChannel

class ReportProject(BaseReportProject):
    """Управление документами проектов техотчетов"""
    for_save = ['versions', 'settings']

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
        self.settings = settings or ProjectSettings()
        self.versions = versions or [
            Version()
        ]
        self.modified = False
        self.event_channel = EventChannel()
        self.event_channel.subscribe('modified', self.set_modified)
        self.event_channel.subscribe(
            'remove_tome',
            self.handle_tome_remove
        )
        self.event_channel.subscribe(
            'remove_element',
            self.handle_element_remove
        )
        self.event_channel.subscribe(
            'remove_file',
            self.handle_file_remove
        )
    
    def set_modified(self):
        self.modified = True
    
    def close(self):
        self.event_channel.unsubscribe('modified', self.set_modified)
        self.event_channel.unsubscribe('remove_tome', self.handle_tome_remove)
        self.event_channel.unsubscribe('remove_element', self.handle_element_remove)
        self.event_channel.unsubscribe('remove_file', self.handle_file_remove)
    
    def __del__(self):
        self.close()

    def save(self):
        write_to_file(self)
        self.modified = False
    
    def rename(self, new_name: str):
        self.settings.name = new_name
    
    def save_as(self, new_path: Path):
        self.settings.savepath = new_path
        self.save()
    
    def set_current_version_id(self, id: int):
        self.settings.current_version_id = id
        #self.event_channel.unsubscribe('remove_tome', self.handle_tome_remove)
    
    def get_current_version(self):
        return self.versions[self.settings.current_version_id]
    
    def create_new_version(self, name: str):
        ver = Version(
            name,
            self.settings.savepath.parent
        )
        self.versions.append(ver)
        self.set_current_version_id(len(self.versions) - 1)
    
    def handle_tome_remove(self, payload):
        self.get_current_version().remove_tome(payload[0])
    
    def handle_element_remove(self, payload):
        element = payload[0]
        ver = self.get_current_version()
        for tome in ver.tomes:
            tome.remove_element(element)
    
    def handle_file_remove(self, payload):
        file = payload[0]
        ver = self.get_current_version()
        for tome in ver.tomes:
            for el in tome.structural_elements:
                el.remove_file(file)
    
    def clone_current_version(self, name: str):
        ver = deepcopy(self.get_current_version())
        ver.name = name
        self.versions.append(ver)
        self.set_current_version_id(len(self.versions) - 1)
    
    def remove_versions(self, versions: list):
        remove_counter = 0
        for ver_id in versions:
            print('NOW ', ver_id)
            if isinstance(ver_id, Version):
                ver = ver_id
            else:
                ver = self.versions[ver_id - remove_counter]
            self.set_current_version_id(self.settings.current_version_id - 1)
            if ver == self.get_current_version():
                self.set_current_version_id(len(self.versions) - 1)
            self.versions.remove(ver)
            remove_counter += 1
    
    def all_paths_are_relative(self):
        root_path = self.settings.savepath.parent
        for ver in self.versions:
            for tome in ver.tomes:
                if tome.savepath.is_relative_to(root_path):
                    print(f'{tome.savepath} is not relative to {root_path}')
                    return False
                for el in tome.structural_elements:
                    for file in el.files:
                        if not file.path.is_relative_to(root_path):
                            print(f'{file.path} is not relative to {root_path}')
                            return False
        return True
    
    def update_relative_paths(self):
        base_root = Path(self.settings.savepath)
        for ver in self.versions:
            ...
    
    @staticmethod
    def open(path: Path):
        project_as_dict = read_from_file(path)
        project = ReportProject.from_dict(project_as_dict, path)
        #project.settings.savepath = path
        if project.settings.paths_relative:
            project.update_relative_paths
        project.modified = False
        return project
    
    @staticmethod
    def from_dict(d: dict, path: Path):
        if 'settings' in d:
            d['settings'] = ProjectSettings.from_dict(d['settings'], path)
            EventChannel().publish('settings_changed', d['settings'])
        if 'versions' in d:
            d['versions'] = [
                Version.from_dict(ver) for ver in d['versions']
            ]
        return ReportProject(**d)
    