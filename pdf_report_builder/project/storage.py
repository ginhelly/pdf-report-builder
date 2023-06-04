from pdf_report_builder.utils.singleton import Singleton

from .project import ReportProject
from .event_channel import EventChannel

class ProjectStorage(metaclass=Singleton):
    def __init__(self):
        EventChannel().subscribe('project_changed', self.set_project)
    
    def set_project(self, payload):
        if isinstance(payload, ReportProject):
            self._project = payload
        else:
            self._project = payload[0]
        EventChannel().publish('settings_changed', self._project.settings)
    
    @property
    def project(self):
        if hasattr(self, '_project'):
            return self._project
        return None