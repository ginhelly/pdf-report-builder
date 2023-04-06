import io
import json
from dataclasses import asdict
from pathlib import Path
from copy import copy

from pdf_report_builder.project.base_project import BaseReportProject
from pdf_report_builder.project.io.base_serializer import BaseSerializer
from pdf_report_builder.project.settings import ProjectSettings
from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.structure.files.pages_subset import PagesSubset
from pdf_report_builder.structure.structural_elements.base import \
    StructuralElement
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.version import Version
from pdf_report_builder.project.io.saveformats import saveformats
from pdf_report_builder.project.storage_settings import SettingsStorage

def encode_path(p: Path):
    settings = SettingsStorage().settings
    if settings.paths_relative and p.is_relative_to(settings.savepath.parent):
        return str(p.relative_to(settings.savepath.parent))
    return str(p)

CUSTOM_STRING_ENCODERS = {
    # Path: lambda x: str(x),
    # PagesSubset: lambda x: str(x)
    list: lambda elements: [serialize_level(el) for el in elements],
    ProjectSettings: lambda settings: serialize_level(settings),
    saveformats: lambda save_format: save_format.value,
    int: lambda i: i
}

def ensure_strings_in_dict(d: dict):
    res = {}
    for i in d:
        if isinstance(d[i], Path):
            res[i] = encode_path(d[i])
        elif not type(d[i]) in CUSTOM_STRING_ENCODERS:
            res[i] = str(d[i])
        else:
            res[i] = CUSTOM_STRING_ENCODERS[type(d[i])](d[i])
    return res

def serialize_level(level):
    if type(level) == dict:
        as_dict = level
    else:
        try:
            as_dict = asdict(level)
        except Exception:
            as_dict = copy(level.__dict__)
    if hasattr(level, 'for_save'):
        for key in list(as_dict.keys()):
            if not key in level.for_save:
                del(as_dict[key])

    res = ensure_strings_in_dict(as_dict)
    return res

class JsonProjectSerializer(BaseSerializer):
    def serialize(self, output: io.TextIOWrapper, project: BaseReportProject):
        project_as_dict = serialize_level(project)
        dumps = json.dumps(project_as_dict, ensure_ascii=False)
        output.write(dumps)

    def deserialize(self, file: io.TextIOWrapper) -> BaseReportProject:
        return json.load(file)
        