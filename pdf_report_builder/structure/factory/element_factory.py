from enum import Enum

from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.structure.structural_elements.tome_contents import TomeContentsElement
from .base_factory import BaseFactory
from .dict_processors import DictProcessor
from .file_factory import FileFactory

class ComputedTypes(Enum):
    REGULAR=0
    TOME_CONTENTS=1


class StructuralElementFactory(BaseFactory):

    @staticmethod
    def from_dict(d: dict):
        if not 'computed' in d:
            d['computed'] = 0
        element_creator = StructuralElementFactory()._get_element_creator(d['computed'])
        return element_creator(d)
        
    def _get_element_creator(self, type: int):
        if type == ComputedTypes.REGULAR.value:
            return self.create_regular_element
        if type == ComputedTypes.TOME_CONTENTS.value:
            return self.create_tome_contents_element
    
    def _regular_element_processor(self, d: dict):
        dict_processor = DictProcessor(d)
        dict_processor.parse_boolean('enumeration_include', True)
        dict_processor.parse_boolean('enumeration_print', False)
        dict_processor.parse_boolean('create_bookmark', True)
        dict_processor.parse_boolean('expanded', True)
        dict_processor.parse_boolean('code_add', False)
        dict_processor.parse_boolean('inner_enumeration', False)
        dict_processor.parse_levels_list('files', FileFactory.from_dict)
        dict_processor.parse_levels_list('subelements', StructuralElementFactory.from_dict)
        return dict_processor

    def create_regular_element(self, d: dict):
        dict_processor = self._regular_element_processor(d)
        dict_processor.remove_invalid_keys([
            'name',
            'computed',
            'code_attr',
            'files',
            'subelements',
            'enumeration_include',
            'enumeration_print',
            'create_bookmark',
            'expanded',
            'code_add',
            'inner_enumeration'
        ])
        return StructuralElement(**dict_processor.d)
