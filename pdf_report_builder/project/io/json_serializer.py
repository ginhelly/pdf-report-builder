import io
import json
from dataclasses import asdict
from pathlib import Path

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

CUSTOM_STRING_ENCODERS = {
    # Path: lambda x: str(x),
    # PagesSubset: lambda x: str(x)
    list: lambda elements: [serialize_level(el) for el in elements],
    ProjectSettings: lambda settings: serialize_level(settings),
    saveformats: lambda save_format: save_format.value
}

def ensure_strings_in_dict(d: dict):
    res = {}
    for i in d:
        if not type(d[i]) in CUSTOM_STRING_ENCODERS:
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
            as_dict = level.__dict__
    res = ensure_strings_in_dict(as_dict)
    return res

class JsonProjectSerializer(BaseSerializer):
    def serialize(self, output: io.TextIOWrapper, project: BaseReportProject):
        project_as_dict = serialize_level(project)
        dumps = json.dumps(project_as_dict, ensure_ascii=False)
        output.write(dumps)

    def deserialize(self, file: io.TextIOWrapper) -> BaseReportProject:
        project_as_dict = json.load(file)
        