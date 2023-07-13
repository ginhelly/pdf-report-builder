import wx

from pdf_report_builder.structure.level import BaseLevel
from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.structure.structural_elements.tome_contents import TomeContentsElement
#from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.ui.tree.tree_node import TreeNode

from .project_panel import ProjectPanel
from .tome_panel import TomePanel
from .element_panel import ElementPanel
from .file_panel import FilePanel
from .tome_contents_panel import TomeContentsPanel

class Book(wx.Simplebook):
    def __init__(
            self,
            parent,
            id=wx.ID_ANY,
            pos=wx.DefaultPosition,
            size=wx.DefaultSize, 
            style=0,
            name='The Book'):
        super().__init__(parent, id, pos, size, style, name)
        self.panels = [
            ProjectPanel(self),
            TomePanel(self),
            ElementPanel(self),
            FilePanel(self),
            TomeContentsPanel(self)
        ]
        self.AddPage(self.panels[0], 'Настройки проекта')
        self.AddPage(self.panels[1], 'Настройки тома')
        self.AddPage(self.panels[2], 'Настройки элемента')
        self.AddPage(self.panels[3], 'Настройки файла')
        self.AddPage(self.panels[4], 'Tome Contents')
        self.SetSelection(0)
    
    def parse_item(self,
            item: BaseLevel
        ):
        if isinstance(item, ReportProject):
            self.SetSelection(0)
            self.panels[0].parse_project(item)
        elif isinstance(item, Tome):
            self.panels[1].parse_tome(item)
            self.SetSelection(1)
        elif isinstance(item, TomeContentsElement):
            self.panels[4].parse_element(item)
            self.SetSelection(4)
        elif isinstance(item, StructuralElement):
            self.panels[2].parse_element(item)
            self.SetSelection(2)
        else:
            self.panels[3].parse_file(item)
            self.SetSelection(3)
    