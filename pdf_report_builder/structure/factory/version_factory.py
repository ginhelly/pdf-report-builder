from .base_factory import BaseFactory
from .tome_factory import TomeFactory
from .dict_processors import DictProcessor
from pdf_report_builder.structure.version import Version

class VersionFactory(BaseFactory):

    @staticmethod
    def from_dict(d: dict):
        dict_processor = DictProcessor(d)
        dict_processor.parse_levels_list('tomes', TomeFactory.from_dict)
        dict_processor.remove_invalid_keys([
                'name', 
                'tomes', 
                'code', 
                'comments'
            ])
        return Version(**dict_processor.d)