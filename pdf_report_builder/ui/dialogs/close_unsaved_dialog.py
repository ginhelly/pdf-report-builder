import wx

class CloseUnsavedDialog(wx.MessageDialog):
    def __init__(self, parent, pos=wx.DefaultPosition):
        message = 'Проект был изменен!\nСохранить изменения?'
        caption = 'Сохранить изменения?'
        style = wx.YES_NO | wx.CANCEL | wx.CANCEL_DEFAULT | wx.ICON_WARNING | wx.CENTRE
        super().__init__(parent, message, caption, style, pos)