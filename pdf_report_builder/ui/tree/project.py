import wx
from pdf_report_builder.project.base_project import BaseReportProject
from .base_context_menu import TreeContextMenu

class ProjectContextMenu(TreeContextMenu):
    def __init__(self, tree: wx.TreeCtrl, project: BaseReportProject) -> None:
        super().__init__(tree)
        self.project = project

    def populate_menu(self, event):
        self.popupmenu.Append(-1, 'Добавить том...')