from pdf_report_builder.project.project import ReportProject

class BaseProjectTemplate:
    def __init__(self) -> None:
        self._project = ReportProject()

    def make_project(self):
        return self._project
