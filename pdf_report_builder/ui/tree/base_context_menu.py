import wx

class TreeContextMenu:
    def __init__(self, tree: wx.TreeCtrl) -> None:
        self.tree = tree
        self.OPTIONS = {
            'Тест': self.handle_option
        }
        
    def show_menu(self, event):
        self.popupmenu = wx.Menu()
        self.populate_menu(event)
        self.tree.Bind(wx.EVT_MENU, self.onSelectContext)
        self.tree.PopupMenu(self.popupmenu, event.GetPoint())
        self.popupmenu.Destroy()
    
    def populate_menu(self, event):
        for text in self.OPTIONS:
            item = self.popupmenu.Append(-1, text)
    
    def onSelectContext(self, event):
        item = self.popupmenu.FindItemById(event.GetId())
        label_text = item.GetItemLabelText()
        print(f"Select context: {label_text}")
        if label_text in self.OPTIONS:
            self.OPTIONS[label_text]()
    
    def handle_option(self):
        raise NotImplementedError('Отсутствует обработчик')