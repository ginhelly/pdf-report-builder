import wx
from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.structure.version import Version
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.ui.tree_icons import get_tree_images

class Tree:
    def __init__(self, base: wx.TreeCtrl, project: ReportProject | None = None):
        self.base = base
        self.base.AssignImageList(get_tree_images())
        if not project is None:
            self.project = ReportProject
            self.parse_project_structure(project)
    
    def parse_project_structure(self, project: ReportProject):
        self.root = self.base.AddRoot(
            'Проект'
        )
        self.base.SetItemImage(self.root, 0, wx.TreeItemIcon_Normal)
        self._parse_tomes(project.get_current_version())
        self.base.ExpandAll()
    
    def _parse_tomes(self, version: Version):
        self._tomes = []
        for tome in version.tomes:
            tome_id = self.base.AppendItem(
                self.root,
                tome.human_readable_name
            )
            elements = self._parse_elements(tome_id, tome)
            self.base.SetItemImage(tome_id, 1, wx.TreeItemIcon_Normal)
            self._tomes.append({
                'tome_id': tome_id,
                'elements': elements
            })
    
    def _parse_elements(self, parent: wx.TreeItemId, tome: Tome):
        elements = []
        for el in tome.structural_elements:
            el_id = self.base.AppendItem(
                parent,
                el.name
            )
            self.base.SetItemImage(el_id, 2, wx.TreeItemIcon_Normal)
            files = self._parse_files(el_id, el)
            elements.append({
                'el_id': el_id,
                'files': files
            })
        return elements
    
    def _parse_files(self, parent: wx.TreeItemId, element: StructuralElement):
        files = []
        for file in element.files:
            file_id = self.base.AppendItem(
                parent,
                str(file.path.name)
            )
            self.base.SetItemImage(file_id, 3, wx.TreeItemIcon_Normal)
            files.append({
                'file_id': file
            })
        return files
    
    def redraw_tree(self, project: ReportProject):
        self.base.DeleteAllItems()
        self.project = project
        self.parse_project_structure(project)