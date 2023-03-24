import wx

class ErrorDialog(wx.MessageDialog):
    def __init__(self, parent, message = None, caption = None):
        if not isinstance(message, str) or len(message) == 0:
            message = 'Не удалось выполнить действие'
        if not isinstance(caption, str) or len(caption) == 0:
            caption = 'Ошибка!'
        style = wx.OK | wx.ICON_ERROR
        super().__init__(parent, message, caption, style)