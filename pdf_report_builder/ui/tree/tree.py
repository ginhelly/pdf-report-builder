import wx
from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.structure.version import Version
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.ui.tree.tree_icons import get_tree_images
from .context_menu_factory import get_context_menu

class Tree:
    def __init__(self, base: wx.TreeCtrl, project: ReportProject | None = None):
        self.base = base
        self.base.AssignImageList(get_tree_images())
        self.base.Bind(wx.EVT_TREE_ITEM_MENU, self.on_context_menu)
        if not project is None:
            self.project = ReportProject
            self.parse_project_structure(project)
    
    def parse_project_structure(self, project: ReportProject):
        self._item_ids = {}
        self.root = self.base.AddRoot(
            'Проект'
        )
        self._item_ids[self.root] = get_context_menu(self.base, project)
        self.base.SetItemImage(self.root, 0, wx.TreeItemIcon_Normal)
        self._parse_tomes(project.get_current_version())
        self.base.ExpandAll()
    
    def _parse_tomes(self, version: Version):
        for tome in version.tomes:
            tome_id = self.base.AppendItem(
                self.root,
                tome.human_readable_name
            )
            self._item_ids[tome_id] = get_context_menu(self.base, tome)
            self._parse_elements(tome_id, tome)
            self.base.SetItemImage(tome_id, 1, wx.TreeItemIcon_Normal)
    
    def _parse_elements(self, parent: wx.TreeItemId, tome: Tome):
        for el in tome.structural_elements:
            el_id = self.base.AppendItem(
                parent,
                el.name
            )
            self._item_ids[el_id] = get_context_menu(self.base, el)
            self.base.SetItemImage(el_id, 2, wx.TreeItemIcon_Normal)
            self._parse_files(el_id, el)
        return
    
    def _parse_files(self, parent: wx.TreeItemId, element: StructuralElement):
        for file in element.files:
            file_id = self.base.AppendItem(
                parent,
                str(file.path.name)
            )
            self._item_ids[file_id] = get_context_menu(self.base, file)
            self.base.SetItemImage(file_id, 3, wx.TreeItemIcon_Normal)
        return
    
    def redraw_tree(self, project: ReportProject):
        self.base.DeleteAllItems()
        self.project = project
        self.parse_project_structure(project)
    
    def on_context_menu(self, event):
        print(self._item_ids[event.Item])
        self._item_ids[event.Item].show_menu(event)