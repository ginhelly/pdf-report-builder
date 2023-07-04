from pdf_report_builder.project.event_channel import EventChannel

class BaseLevel:
    def __setattr__(self, __name: str, __value) -> None:
        try:
            old_value = self.__getattribute__(__name)
        except AttributeError:
            old_value = None
        super().__setattr__(__name, __value)
        if not old_value is None and not __value == old_value:
            EventChannel().publish('modified')
    
    @property
    def is_expanded(self):
        if hasattr(self, 'expanded'):
            return self.expanded
        return True
    
    def set_expanded(self, value: bool):
        self.expanded = value