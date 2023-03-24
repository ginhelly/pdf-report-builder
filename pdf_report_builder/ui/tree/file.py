import wx
import os
from pdf_report_builder.structure.files.input_pdf import PDFFile
from .base_context_menu import *
from pdf_report_builder.ui.dialogs.error_message import ErrorDialog
from pdf_report_builder.project.event_channel import EventChannel
from pdf_report_builder.ui.dialogs.delete_item_dialog import DeletePrompt


class FileContextMenu(TreeContextMenu):
    def __init__(self, tree: wx.TreeCtrl, file: PDFFile) -> None:
        super().__init__(tree)
        self.file = file
        self.OPTIONS = [
            MenuOption('Открыть', self.open_file),
            MenuOption('-', lambda: ...),
            MenuOption('Удалить файл из списка', self.remove_file)
        ]
    
    def open_file(self):
        if self.file.path.exists() and self.file.path.is_file():
            os.startfile(str(self.file.path))
        else:
            dlg = ErrorDialog(None, 'Невозможно открыть файл')
            dlg.ShowModal()
            dlg.Destroy()
    
    def remove_file(self):
        with DeletePrompt(None) as dlg:
            if dlg.ShowModal() != wx.ID_YES:
                return
        EventChannel().publish('remove_file', self.file)
        EventChannel().publish('tree_update')