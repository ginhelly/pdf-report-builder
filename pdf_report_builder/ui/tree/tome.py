import wx
from pdf_report_builder.structure.tome import Tome
from .base_context_menu import TreeContextMenu

class TomeContextMenu(TreeContextMenu):
    def __init__(self, tree: wx.TreeCtrl, tome: Tome) -> None:
        super().__init__(tree)
        self.tome = tome
    
    def populate_menu(self, event):
        self.popupmenu.Append(-1, 'Добавить структурный элемент...')
        self.popupmenu.Append(-1, 'Свойства...')
        self.popupmenu.AppendSeparator()
        delete_tome = self.popupmenu.Append(-1, 'Удалить том')
        delete_tome_font = delete_tome.GetFont().Bold()
        delete_tome.SetFont(delete_tome_font)
        delete_tome.SetBackgroundColour(wx.Colour(240, 0, 0))