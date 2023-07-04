import json

import pyperclip
import wx

from pdf_report_builder.project.event_channel import EventChannel
from pdf_report_builder.structure.structural_elements.list import *
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.ui.dialogs.add_element_dialog import AddElementDialog
from pdf_report_builder.ui.dialogs.delete_item_dialog import DeletePrompt
from pdf_report_builder.project.io.json_serializer import serialize_level

from .base_context_menu import *


class TomeContextMenu(TreeContextMenu):
    def __init__(self, tree: wx.TreeCtrl, tome: Tome) -> None:
        super().__init__(tree)
        self.tome = tome
        self.OPTIONS = [
            MenuOption('Добавить структурный элемент...', self.add_element),
            MenuOption('-', lambda: ...),
            MenuOption('Вырезать', self.cut_to_clipboard),
            MenuOption('Копировать', self.copy_to_clipboard),
            MenuOption('Вставить', self.paste, self.peek_clipboard),
            MenuOption('-', lambda: ...),
            MenuOption('Удалить том', self.remove_tome)
        ]
    
    def add_element(self):
        with AddElementDialog(None) as dlg:
            if dlg.ShowModal() == wx.ID_CANCEL:
                return
            scheme = dlg.get_element_scheme()
            self.tome.create_element_by_scheme(scheme)
            EventChannel().publish('tree_update')
    
    def remove_tome(self):
        with DeletePrompt(None) as dlg:
            if dlg.ShowModal() != wx.ID_YES:
                return
        self.node.parent.item.handle_tome_remove([self.tome])
        EventChannel().publish('modified')
        EventChannel().publish('tree_update')
    
    def peek_clipboard(self) -> bool:
        content = pyperclip.paste()
        if not (7 < len(content) < 5242880):
            return False
        if not content[:7] == 'LEVEL=2':
            return False
        try:
            self.clipboard_content = json.loads(content[7:])
        except Exception:
            return False
        return True
    
    def paste(self):
        new_el = StructuralElement.from_dict(self.clipboard_content)
        self.tome.add_element(new_el)
        EventChannel().publish('tree_update')
    
    def copy_to_clipboard(self):
        ser = serialize_level(self.tome)
        s = json.dumps(ser, ensure_ascii=False)
        pyperclip.copy(f'LEVEL=1{s}')
    
    def cut_to_clipboard(self):
        self.copy_to_clipboard()
        self.node.parent.item.handle_tome_remove([self.tome])
        EventChannel().publish('modified')
        EventChannel().publish('tree_update')