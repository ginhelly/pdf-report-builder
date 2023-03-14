from pdf_report_builder.structure.version import Version
from pdf_report_builder.project.settings import ProjectSettings

class BaseReportProject:
    def __init__(
            self,
            versions: list[Version] | None = None,
            settings: ProjectSettings | None = None
        ) -> None:
        pass