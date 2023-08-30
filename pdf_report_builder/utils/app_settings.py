from .singleton import Singleton

class AppSettings(metaclass=Singleton):
    _settings = {}
    
    @classmethod
    def set(cls, key: str, value):
        cls._settings[key] = value
    
    @classmethod
    def get(cls, key: str):
        try:
            return cls._settings[key]
        except KeyError:
            return None
    
    @classmethod
    def print(cls):
        print(cls._settings)
