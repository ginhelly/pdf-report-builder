import json
from pathlib import Path

import pyperclip
import wx

from pdf_report_builder.project.base_project import BaseReportProject
from pdf_report_builder.project.event_channel import EventChannel
from pdf_report_builder.structure.tome import Tome

from .base_context_menu import *


class ProjectContextMenu(TreeContextMenu):
    def __init__(self, tree: wx.TreeCtrl, project: BaseReportProject) -> None:
        super().__init__(tree)
        self.project = project
        self.OPTIONS = [
            MenuOption('Добавить том...', self.add_tome),
            MenuOption('Вставить', self.paste, self.peek_clipboard)
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
    
    def peek_clipboard(self):
        content = pyperclip.paste()
        if not (7 < len(content) < 5242880):
            return False
        if not content[:7] == 'LEVEL=1':
            return False
        try:
            self.clipboard_content = json.loads(content[7:])
        except Exception:
            return False
        return True
    
    def paste(self):
        new_tome = Tome.from_dict(self.clipboard_content)
        self.project.get_current_version().append_tome(new_tome)
        EventChannel().publish('tree_update')