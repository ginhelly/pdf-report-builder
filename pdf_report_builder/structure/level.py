from pdf_report_builder.project.event_channel import EventChannel

class BaseLevel:
    def __post_init__(self):
        self._parent = None

    def __setattr__(self, __name: str, __value) -> None:
        try:
            old_value = self.__getattribute__(__name)
        except AttributeError:
            old_value = None
        super().__setattr__(__name, __value)
        if not old_value is None and not __value == old_value and not self.parent is None:
            EventChannel().publish('modified')
    
    @property
    def is_expanded(self):
        if hasattr(self, 'expanded'):
            return self.expanded
        return True
    
    def set_expanded(self, value: bool):
        self.expanded = value
    
    @property
    def parent(self):
        if hasattr(self, '_parent'):
            return self._parent
        return None
    
    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def full_code(self):
        code = self.code
        parent = self.parent
        while not parent is None:
            code = parent.code + code
            parent = parent.parent
        return code