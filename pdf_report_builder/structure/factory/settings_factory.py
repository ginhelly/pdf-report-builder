from pathlib import Path
from .base_factory import BaseFactory
from .dict_processors import DictProcessor
from pdf_report_builder.project.settings import ProjectSettings
from pdf_report_builder.project.io.saveformats import saveformats

class SettingsFactory(BaseFactory):

    @staticmethod
    def from_dict(d: dict, path: Path | None):
        if not path is None:
            d['savepath'] = path
        if not 'save_format' in d:
            raise IOError('Неизвестный формат!')
        try:
            save_format = d['save_format']
            d['save_format'] = saveformats(save_format)
        except ValueError:
            raise IOError('Неизвестный формат')
        
        dict_processor = DictProcessor(d)
        dict_processor.parse_boolean('paths_relative', True)
        dict_processor.remove_invalid_keys([
                'savepath', 
                'name', 
                'save_format', 
                'paths_relative',
                'current_version_id'
            ])
        return ProjectSettings(**dict_processor.d)