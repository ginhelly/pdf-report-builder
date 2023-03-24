import wx
from typing import NamedTuple, Callable

class MenuOption(NamedTuple):
    name: str
    handle: Callable


class TreeContextMenu:
    def __init__(self, tree: wx.TreeCtrl) -> None:
        self.tree = tree
        self.OPTIONS: list[MenuOption] = []
        
    def show_menu(self, event):
        self.popupmenu = wx.Menu()
        self.populate_menu(event)
        self.tree.Bind(wx.EVT_MENU, self.onSelectContext)
        self.tree.PopupMenu(self.popupmenu, event.GetPoint())
        self.popupmenu.Destroy()
    
    def populate_menu(self, event):
        for option in self.OPTIONS:
            if len(option.name) >= 3:
                item = self.popupmenu.Append(-1, option.name)
            else:
                self.popupmenu.AppendSeparator()
    
    def onSelectContext(self, event):
        item = self.popupmenu.FindItemById(event.GetId())
        label_text = item.GetItemLabelText()
        for option in self.OPTIONS:
            if option.name == label_text:
                option.handle()
    
    def handle_option(self):
        raise NotImplementedError('Отсутствует обработчик')