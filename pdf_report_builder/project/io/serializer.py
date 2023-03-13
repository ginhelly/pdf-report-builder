from pathlib import Path
import io

from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.project.io.json_serializer import JsonProjectSerializer
from pdf_report_builder.project.io.saveformats import *

class BaseSerializer:
    def serialize(self, output: io.TextIOWrapper, project: ReportProject):
        pass

    def deserialize(self, file: io.TextIOWrapper) -> ReportProject:
        pass

def get_serializer(saveformat: saveformats) -> BaseSerializer:
    if saveformat == saveformats.JSON_V01:
        return JsonProjectSerializer()

def write_to_file(project: ReportProject):
    serializer = get_serializer(project.settings.save_format)
    with open(project.settings.savepath, 'w+', encoding='utf-8') as output:
        serializer.serialize(output, project)

def read_from_file(path: Path) -> ReportProject:
    if (not path.exists) or (not path.is_file()):
        raise FileNotFoundError('Не найден файл проекта!')
    save_format = FILE_EXTENSIONS[path.suffix.upper()]
    serializer = get_serializer(save_format)
    with open(path, 'r+', encoding='utf-8') as input_file:
        return serializer.deserialize(input_file)
