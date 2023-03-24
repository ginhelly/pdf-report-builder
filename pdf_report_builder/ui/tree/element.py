import wx
from pathlib import Path
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from .base_context_menu import *
from pdf_report_builder.ui.dialogs.delete_item_dialog import DeletePrompt
from pdf_report_builder.project.event_channel import EventChannel
from pdf_report_builder.ui.dialogs.error_message import ErrorDialog

class ElementContextMenu(TreeContextMenu):
    def __init__(self, tree: wx.TreeCtrl, element: StructuralElement) -> None:
        super().__init__(tree)
        self.element = element
        self.OPTIONS = [
            MenuOption('Добавить файл...', self.add_file),
            MenuOption('-', lambda: ...),
            MenuOption('Удалить элемент', self.remove_element)
        ]
    
    def add_file(self):
        with wx.FileDialog(
            None,
            "Путь для PDF-файла",
            wildcard="PDF-документы (.pdf)|*.pdf",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        ) as open_dialog:
            if open_dialog.ShowModal() == wx.ID_CANCEL:
                return
            path = Path(open_dialog.GetPath())
        with wx.TextEntryDialog(
            None,
            "Какие страницы использовать? (пустая строка - все)"
        ) as dlg:
            if dlg.ShowModal() == wx.ID_CANCEL:
                return
            subset = dlg.GetValue()
        try:
            self.element.add_file(
                file_path=path,
                subset=subset
            )
        except Exception as e:
            dlg = ErrorDialog(None, str(e))
            dlg.ShowModal()
            dlg.Destroy()
        EventChannel().publish('tree_update')

    def remove_element(self):
        with DeletePrompt(None) as dlg:
            if dlg.ShowModal() != wx.ID_YES:
                return
        EventChannel().publish('remove_element', self.element)
        EventChannel().publish('tree_update')