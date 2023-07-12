from pdf_report_builder.structure.structural_elements.computed_types import ComputedTypes
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.structure.structural_elements.tome_contents import TomeContentsElement
from pdf_report_builder.utils.file_watcher import FileWatcher
from .base_factory import BaseFactory
from .dict_processors import DictProcessor
from .file_factory import FileFactory

from settings import FILE_WATCHER

BASE_VALID_ELEMENT_KEYS = [
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
]


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
        if FILE_WATCHER:
            for file in dict_processor.d['files']:
                FileWatcher().add_file(file)
        dict_processor.parse_levels_list('subelements', StructuralElementFactory.from_dict)
        return dict_processor
    
    def _computed_element_processor(self, d: dict):
        dict_processor = self._regular_element_processor(d)
        dict_processor.parse_path('pdf_temp_path')
        return dict_processor

    def create_regular_element(self, d: dict):
        dict_processor = self._regular_element_processor(d)
        dict_processor.remove_invalid_keys(BASE_VALID_ELEMENT_KEYS)
        return StructuralElement(**dict_processor.d)
    
    def create_tome_contents_element(self, d: dict):
        dict_processor = self._computed_element_processor(d)
        dict_processor.parse_path('doc_template')
        dict_processor.remove_invalid_keys(
            BASE_VALID_ELEMENT_KEYS + ['pdf_temp_path', 'doc_template']
        )
        return TomeContentsElement(**dict_processor.d)
