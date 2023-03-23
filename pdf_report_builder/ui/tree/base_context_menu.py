import wx

class TreeContextMenu:
    def show_menu(self, event, tree: wx.TreeCtrl):
        self.popupmenu = wx.Menu()
        self.populate_menu(event)
        tree.PopupMenu(self.popupmenu, event.GetPoint())
        self.popupmenu.Destroy()
    
    def populate_menu(self, event):
        for text in "Add Delete Edit".split():
            item = self.popupmenu.Append(-1, text)