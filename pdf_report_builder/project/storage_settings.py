from pdf_report_builder.utils.singleton import Singleton

from .event_channel import EventChannel
from .settings import ProjectSettings


class SettingsStorage(metaclass=Singleton):
    def __init__(self):
        EventChannel().subscribe('settings_changed', self.set_settings)
    
    def set_settings(self, payload):
        if isinstance(payload, ProjectSettings):
            self._settings = payload
            return
        self._settings = payload[0]
    
    @property
    def settings(self):
        if hasattr(self, '_settings'):
            return self._settings
        return None