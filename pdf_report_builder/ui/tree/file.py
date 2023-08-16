import os
import json
import subprocess

import pyperclip
import wx

from pdf_report_builder.project.event_channel import EventChannel
from pdf_report_builder.project.io.json_serializer import serialize_level
from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.ui.dialogs.delete_item_dialog import DeletePrompt
from pdf_report_builder.ui.dialogs.error_message import ErrorDialog

from .base_context_menu import *


class FileContextMenu(TreeContextMenu):
    def __init__(self, tree: wx.TreeCtrl, file: PDFFile) -> None:
        super().__init__(tree)
        self.file = file
        self.OPTIONS = [
            MenuOption('Открыть', self.open_file, condition_enable=self.file_is_valid),
            MenuOption('Открыть папку с файлом', self.open_folder, condition_enable=self.file_is_valid),
            MenuOption('-', lambda: ...),
            MenuOption('Вырезать', self.cut_to_clipboard, condition_enable=self.parent_isnt_computed),
            MenuOption('Копировать', self.copy_to_clipboard, condition_enable=self.parent_isnt_computed),
            MenuOption('-', lambda: ...),
            MenuOption('Удалить файл из проекта', self.remove_file, condition_enable=self.parent_isnt_computed)
        ]
    
    def file_is_valid(self):
        if self.file.path.exists() and self.file.path.is_file():
            return True
        return False

    def parent_isnt_computed(self):
        if self.file.parent.is_computed:
            return False
        return True
    
    def open_file(self):
        if self.file.path.exists() and self.file.path.is_file():
            os.startfile(str(self.file.path))
        else:
            dlg = ErrorDialog(None, 'Невозможно открыть файл')
            dlg.ShowModal()
            dlg.Destroy()
    
    def open_folder(self):
        folder = self.file.path.parent
        if folder.exists() and folder.is_dir():
            subprocess.Popen(f'explorer "{folder}"')
        else:
            dlg = ErrorDialog(None, 'Невозможно открыть папку')
            dlg.ShowModal()
            dlg.Destroy()

    
    def remove_file(self):
        with DeletePrompt(None) as dlg:
            if dlg.ShowModal() != wx.ID_YES:
                return
        self.node.parent.item.remove_file(self.file)
        EventChannel().publish('modified')
        EventChannel().publish('tree_update')
    
    def copy_to_clipboard(self):
        ser = serialize_level(self.file)
        s = json.dumps(ser, ensure_ascii=False)
        pyperclip.copy(f'LEVEL=3{s}')
    
    def cut_to_clipboard(self):
        ser = serialize_level(self.file)
        s = json.dumps(ser, ensure_ascii=False)
        pyperclip.copy(f'LEVEL=3{s}')
        self.node.parent.item.remove_file(self.file)
        EventChannel().publish('modified')
        EventChannel().publish('tree_update')