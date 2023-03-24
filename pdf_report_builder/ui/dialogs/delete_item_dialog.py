import wx

class DeletePrompt(wx.MessageDialog):
    def __init__(self, parent, message=''):
        if len(message) == 0:
            message = 'Вы подтверждаете удаление?'
        caption = 'Точно удалить?'
        style = wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING
        super().__init__(parent, message, caption, style)
        self.SetYesNoLabels('Удалить!', 'Не удалять')
