import io
from pdf_report_builder.project.base_project import BaseReportProject

class BaseSerializer:
    def serialize(self, output: io.TextIOWrapper, project: BaseReportProject):
        pass

    def deserialize(self, file: io.TextIOWrapper) -> BaseReportProject:
        pass