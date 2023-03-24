import wx
from pathlib import Path
from pdf_report_builder.project.base_project import BaseReportProject
from .base_context_menu import *
from pdf_report_builder.project.event_channel import EventChannel

class ProjectContextMenu(TreeContextMenu):
    def __init__(self, tree: wx.TreeCtrl, project: BaseReportProject) -> None:
        super().__init__(tree)
        self.project = project
        self.OPTIONS = [
            MenuOption('Добавить том...', self.add_tome)
        ]
    
    def add_tome(self):
        ver = self.project.get_current_version()
        with wx.TextEntryDialog(
            None,
            "Шифр тома"
        ) as dlg:
            if dlg.ShowModal() == wx.ID_CANCEL:
                return
            basename = dlg.GetValue()
        with wx.FileDialog(
            None,
            "Путь для сохранения результата",
            wildcard="PDF-документы (.pdf)|*.pdf",
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        ) as open_dialog:
            if open_dialog.ShowModal() == wx.ID_CANCEL:
                return
            path = Path(open_dialog.GetPath())
        ver.create_tome(basename, path.stem, path)
        EventChannel().publish('tree_update')