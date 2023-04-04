from pathlib import Path
import json

import pyperclip
import wx

from pdf_report_builder.project.event_channel import EventChannel
from pdf_report_builder.structure.structural_elements.base import \
    StructuralElement
from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.ui.dialogs.delete_item_dialog import DeletePrompt
from pdf_report_builder.ui.dialogs.error_message import ErrorDialog
from pdf_report_builder.project.io.json_serializer import serialize_level

from .base_context_menu import *


class ElementContextMenu(TreeContextMenu):
    def __init__(self, tree: wx.TreeCtrl, element: StructuralElement) -> None:
        super().__init__(tree)
        self.element = element
        self.OPTIONS = [
            MenuOption('Добавить файл...', self.add_file),
            MenuOption('-', lambda: ...),
            MenuOption('Вырезать', self.cut_to_clipboard),
            MenuOption('Копировать', self.copy_to_clipboard),
            MenuOption('-', lambda: ...),
            MenuOption('Удалить элемент', self.remove_element)
        ]
    
    def add_file(self):
        with wx.FileDialog(
            None,
            "Путь для PDF-файла",
            wildcard="PDF-документы (.pdf)|*.pdf",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        ) as open_dialog:
            if open_dialog.ShowModal() == wx.ID_CANCEL:
                return
            path = Path(open_dialog.GetPath())
        with wx.TextEntryDialog(
            None,
            "Какие страницы использовать? (пустая строка - все)"
        ) as dlg:
            if dlg.ShowModal() == wx.ID_CANCEL:
                return
            subset = dlg.GetValue()
        try:
            self.element.add_file(
                file_path=path,
                subset=subset
            )
        except Exception as e:
            dlg = ErrorDialog(None, str(e))
            dlg.ShowModal()
            dlg.Destroy()
        EventChannel().publish('tree_update')

    def remove_element(self):
        with DeletePrompt(None) as dlg:
            if dlg.ShowModal() != wx.ID_YES:
                return
        EventChannel().publish('remove_element', self.element)
        EventChannel().publish('tree_update')
    
    def populate_menu(self, event):
        super().populate_menu(event)
        self.peek_clipboard()
    
    def peek_clipboard(self):
        content = pyperclip.paste()
        if not (7 < len(content) < 5242880):
            print('len check')
            return
        if not content[:7] == 'LEVEL=3':
            print('level wrong')
            return
        try:
            self.clipboard_content = json.loads(content[7:])
        except Exception:
            print('parse error')
            return
        self.popupmenu.Insert(4, -1, 'Вставить')
        self.OPTIONS.append(MenuOption('Вставить', self.paste))

    def paste(self):
        new_file = PDFFile.from_dict(self.clipboard_content)
        self.element.add_file(new_file)
        EventChannel().publish('tree_update')
    
    def copy_to_clipboard(self):
        ser = serialize_level(self.element)
        s = json.dumps(ser, ensure_ascii=False)
        pyperclip.copy(f'LEVEL=2{s}')
    
    def cut_to_clipboard(self):
        ser = serialize_level(self.element)
        s = json.dumps(ser, ensure_ascii=False)
        pyperclip.copy(f'LEVEL=2{s}')
        EventChannel().publish('remove_element', self.element)
        EventChannel().publish('tree_update')