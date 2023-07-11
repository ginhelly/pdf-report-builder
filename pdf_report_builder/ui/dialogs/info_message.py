import wx

class InfoDialog(wx.MessageDialog):
    def __init__(self, parent, message = None, caption = None):
        if not isinstance(message, str) or len(message) == 0:
            message = 'Проект успешно сохранен'
        if not isinstance(caption, str) or len(caption) == 0:
            caption = 'Информация'
        style = wx.OK | wx.ICON_INFORMATION
        super().__init__(parent, message, caption, style)