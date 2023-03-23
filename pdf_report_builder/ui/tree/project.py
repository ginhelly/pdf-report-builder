import wx
from pdf_report_builder.project.base_project import BaseReportProject
from .base_context_menu import TreeContextMenu

class ProjectContextMenu(TreeContextMenu):
    def __init__(self, project: BaseReportProject) -> None:
        self.project = project
