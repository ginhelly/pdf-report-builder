import wx

from pdf_report_builder.ui.form_builder.main import BaseAddElementDialog
from pdf_report_builder.structure.structural_elements.list import *

class AddElementDialog(BaseAddElementDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.element_type.Append(ELEMENT_NAMES)
        self.element_type.SetSelection(0)
    
