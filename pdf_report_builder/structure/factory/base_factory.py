from pdf_report_builder.utils.singleton import Singleton

class BaseFactory(metaclass=Singleton):
    
    @staticmethod
    def from_dict(d: dict):
        pass