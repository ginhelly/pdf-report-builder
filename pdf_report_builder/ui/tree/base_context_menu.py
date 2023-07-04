import wx
from typing import NamedTuple, Callable

class MenuOption(NamedTuple):
    name: str
    handle: Callable
    condition_show: Callable = lambda: True
    condition_enable: Callable = lambda: True


class TreeContextMenu:
    def __init__(self, tree: wx.TreeCtrl) -> None:
        self.tree = tree
        self.OPTIONS: list[MenuOption] = []
        
    def show_menu(self, event, node):
        self.node = node
        self.popupmenu = wx.Menu()
        self.populate_menu(event)
        self.tree.Bind(wx.EVT_MENU, self.onSelectContext)
        self.tree.PopupMenu(self.popupmenu, event.GetPoint())
        self.popupmenu.Destroy()
    
    def populate_menu(self, event):
        for option in self.OPTIONS:
            if not option.condition_show():
                continue
            if len(option.name) >= 3:
                item = self.popupmenu.Append(-1, option.name)
                if not option.condition_enable():
                    item.Enable(False)
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