import wx
from pdf_report_builder.structure.tome import Tome
from .base_context_menu import TreeContextMenu

class TomeContextMenu(TreeContextMenu):
    def __init__(self, tome: Tome) -> None:
        self.tome = tome