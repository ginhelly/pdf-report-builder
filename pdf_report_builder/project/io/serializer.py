from pathlib import Path
import io

from pdf_report_builder.project.base_project import BaseReportProject
from pdf_report_builder.project.io.base_serializer import BaseSerializer
from pdf_report_builder.project.io.json_serializer import JsonProjectSerializer
from pdf_report_builder.project.io.saveformats import *

def get_serializer(saveformat: saveformats) -> BaseSerializer:
    if saveformat == saveformats.JSON_V01:
        return JsonProjectSerializer()

def write_to_file(project: BaseReportProject):
    serializer = get_serializer(project.settings.save_format)
    save_folder = project.settings.savepath.parent
    save_folder.mkdir(exist_ok=True)
    with open(project.settings.savepath, 'w+', encoding='utf-8') as output:
        serializer.serialize(output, project)

def read_from_file(path: Path) -> BaseReportProject:
    if (not path.exists) or (not path.is_file()):
        raise FileNotFoundError('Не найден файл проекта!')
    if not path.suffix.upper() in FILE_EXTENSIONS:
        raise TypeError('Файл не может быть обработан!')
    save_format = FILE_EXTENSIONS[path.suffix.upper()]
    serializer = get_serializer(save_format)
    with open(path, 'r+', encoding='utf-8') as input_file:
        return serializer.deserialize(input_file)
