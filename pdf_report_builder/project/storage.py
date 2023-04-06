from .project import ReportProject
from .event_channel import Singleton, EventChannel

class ProjectStorage(metaclass=Singleton):
    def __init__(self):
        EventChannel().subscribe('project_changed', self.set_project)
    
    def set_project(self, payload):
        if isinstance(payload, ReportProject):
            self._project = payload
            return
        self._project = payload[0]
    
    @property
    def project(self):
        if hasattr(self, '_project'):
            return self._project
        return None