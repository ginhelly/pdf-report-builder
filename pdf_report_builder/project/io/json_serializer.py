import json
import io
from dataclasses import asdict
from pdf_report_builder.project.base_project import BaseReportProject
from pdf_report_builder.project.io.base_serializer import BaseSerializer

class JsonProjectSerializer(BaseSerializer):
    def serialize(self, output: io.TextIOWrapper, project: BaseReportProject):
        settings_dict = asdict(project.settings)
        