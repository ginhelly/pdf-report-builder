from .base_factory import BaseFactory
from .dict_processors import DictProcessor
from pdf_report_builder.structure.files.input_pdf import PDFFile

class FileFactory(BaseFactory):

    @staticmethod
    def from_dict(d: dict):
        dict_processor = DictProcessor(d)
        dict_processor.parse_path('path')
        dict_processor.parse_boolean('instant_read', True)
        dict_processor.parse_boolean('expanded', True)
        change_subset = False
        if 'subset' in dict_processor.d:
            subset = dict_processor.d['subset']
            del dict_processor.d['subset']
            change_subset = True
        dict_processor.remove_invalid_keys()
        file = PDFFile(**dict_processor.d)
        filepath = dict_processor.d['path']
        if filepath.exists() and filepath.is_file() \
            and filepath.suffix == '.pdf' and change_subset:
            file.change_subset(subset)
        return file