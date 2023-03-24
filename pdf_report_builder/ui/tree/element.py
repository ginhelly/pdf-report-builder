import wx
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from .base_context_menu import TreeContextMenu

class ElementContextMenu(TreeContextMenu):
    def __init__(self, tree: wx.TreeCtrl, element: StructuralElement) -> None:
        super().__init__(tree)
        self.element = element