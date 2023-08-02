from pathlib import Path
import json

import pyperclip
import wx

from pdf_report_builder.project.event_channel import EventChannel
from pdf_report_builder.structure.structural_elements.base import \
    StructuralElement
from pdf_report_builder.structure.factory.element_factory import \
    StructuralElementFactory
from pdf_report_builder.structure.factory.file_factory import FileFactory
from pdf_report_builder.ui.dialogs.delete_item_dialog import DeletePrompt
from pdf_report_builder.ui.dialogs.error_message import ErrorDialog
from pdf_report_builder.project.io.json_serializer import serialize_level
from pdf_report_builder.ui.dialogs.add_element_dialog import AddElementDialog
from pdf_report_builder.ui.dialogs.build_computed import BuildComputedDialog

from .base_context_menu import *


class ElementContextMenu(TreeContextMenu):
    def __init__(self, tree: wx.TreeCtrl, element: StructuralElement) -> None:
        super().__init__(tree)
        self.element = element
        self.OPTIONS = [
            MenuOption('Добавить файл...', self.add_file, self.is_element_raw),
            MenuOption('Добавить вложенный элемент...', self.add_subelement, self.is_element_raw),
            MenuOption('Сформировать PDF', self.make_pdf, self.is_element_computed),
            MenuOption('-', lambda: ...),
            MenuOption('Вырезать', self.cut_to_clipboard),
            MenuOption('Копировать', self.copy_to_clipboard),
            MenuOption('Вставить', self.paste, self.peek_clipboard, self.is_element_raw),
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
    
    def add_subelement(self):
        with AddElementDialog(None) as dlg:
            if dlg.ShowModal() == wx.ID_CANCEL:
                return
            element = dlg.get_element()
            self.element.add_subelement(element)
            EventChannel().publish('tree_update')

    def remove_element(self):
        with DeletePrompt(None) as dlg:
            if dlg.ShowModal() != wx.ID_YES:
                return
        self.node.parent.item.remove_element(self.element)
        EventChannel().publish('modified')
        EventChannel().publish('tree_update')
    
    def peek_clipboard(self):
        content = pyperclip.paste()
        if not (7 < len(content) < 5242880):
            return False
        if not content[:7] in ('LEVEL=3', 'LEVEL=2'):
            return False
        try:
            self.clipboard_content = json.loads(content[7:])
            self.clipboard_type = 'file' if content[:7] == 'LEVEL=3' else 'subelement'
        except Exception:
            return False
        return True

    def paste(self):
        if self.clipboard_type == 'file':
            new_file = FileFactory.from_dict(self.clipboard_content)
            self.element.add_file(new_file)
        elif self.clipboard_type == 'subelement':
            new_el = StructuralElementFactory.from_dict(self.clipboard_content)
            self.element.add_subelement(new_el)
        EventChannel().publish('tree_update')
    
    def copy_to_clipboard(self):
        ser = serialize_level(self.element)
        s = json.dumps(ser, ensure_ascii=False)
        pyperclip.copy(f'LEVEL=2{s}')
    
    def cut_to_clipboard(self):
        ser = serialize_level(self.element)
        s = json.dumps(ser, ensure_ascii=False)
        pyperclip.copy(f'LEVEL=2{s}')
        self.node.parent.item.remove_element(self.element)
        EventChannel().publish('modified')
        EventChannel().publish('tree_update')
    
    def is_element_computed(self):
        return self.element.computed > 0
    
    def is_element_raw(self):
        return self.element.computed == 0
    
    def make_pdf(self):
        if self.is_element_raw():
            return
        dlg = BuildComputedDialog(None, [self.element])
        dlg.ShowModal()
        dlg.Destroy()