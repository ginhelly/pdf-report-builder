import wx
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from .base_context_menu import TreeContextMenu

class ElementContextMenu(TreeContextMenu):
    def __init__(self, element: StructuralElement) -> None:
        self.element = element