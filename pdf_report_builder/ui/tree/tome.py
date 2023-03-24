import wx
from pdf_report_builder.structure.tome import Tome
from .base_context_menu import *
from pdf_report_builder.structure.structural_elements.list import *
from pdf_report_builder.ui.dialogs.add_element_dialog import AddElementDialog
from pdf_report_builder.project.event_channel import EventChannel
from pdf_report_builder.ui.dialogs.delete_item_dialog import DeletePrompt

class TomeContextMenu(TreeContextMenu):
    def __init__(self, tree: wx.TreeCtrl, tome: Tome) -> None:
        super().__init__(tree)
        self.tome = tome
        self.OPTIONS = [
            MenuOption('Добавить структурный элемент...', self.add_element),
            MenuOption('-', lambda: ...),
            MenuOption('Удалить том', self.remove_tome)
        ]
    
    def add_element(self):
        with AddElementDialog(None) as dlg:
            if dlg.ShowModal() == wx.ID_CANCEL:
                return
            selected_type = dlg.element_type.GetSelection()
            code = dlg.element_code.GetLineText(0)
        if selected_type == 0:
            name, official, code2 = 'Структурный элемент', False, ''
        else:
            name, official, code2 = ELEMENTS[selected_type - 1]
        if len(code) == 0:
            code = code2
        self.tome.create_element(name, official, code)
        EventChannel().publish('tree_update')
    
    def remove_tome(self):
        with DeletePrompt(None) as dlg:
            if dlg.ShowModal() != wx.ID_YES:
                return
        EventChannel().publish('remove_tome', self.tome)
        EventChannel().publish('tree_update')