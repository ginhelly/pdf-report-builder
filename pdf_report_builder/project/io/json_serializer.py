import json
import io
from dataclasses import asdict
from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.project.io.serializer import BaseSerializer

class JsonProjectSerializer(BaseSerializer):
    def serialize(self, output: io.TextIOWrapper, project: ReportProject):
        settings_dict = asdict(project.settings)
        