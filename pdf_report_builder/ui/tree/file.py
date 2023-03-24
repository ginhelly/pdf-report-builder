import wx
from pdf_report_builder.structure.files.input_pdf import PDFFile
from .base_context_menu import TreeContextMenu

class FileContextMenu(TreeContextMenu):
    def __init__(self, tree: wx.TreeCtrl, file: PDFFile) -> None:
        super().__init__(tree)
        self.file = file