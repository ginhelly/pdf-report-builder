from .base_factory import BaseFactory
from .element_factory import StructuralElementFactory
from .dict_processors import DictProcessor
from pdf_report_builder.structure.tome import Tome

class TomeFactory(BaseFactory):

    @staticmethod
    def from_dict(d: dict):
        dict_processor = DictProcessor(d)
        dict_processor.parse_path('savepath')
        dict_processor.parse_boolean('expanded', True)
        dict_processor.parse_boolean('use_custom_enumeration_start', False)
        dict_processor.parse_levels_list('structural_elements', StructuralElementFactory.from_dict)
        dict_processor.remove_invalid_keys([
                'basename', 
                'human_readable_name', 
                'savepath', 
                'structural_elements', 
                'expanded', 
                'use_custom_enumeration_start', 
                'custom_enumeration_start'
            ])
        return Tome(**dict_processor.d)