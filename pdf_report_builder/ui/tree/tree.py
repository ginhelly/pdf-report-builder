import wx
from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.structure.version import Version
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.ui.tree.tree_icons import get_tree_images
from .tree_node import *
from pdf_report_builder.project.event_channel import EventChannel

class Tree(wx.TreeCtrl):
    def __init__(self, parent, project = None):
        super().__init__(
            parent,
            wx.ID_ANY,
            style=wx.TR_DEFAULT_STYLE
        )
        self.AssignImageList(get_tree_images())
        self.Bind(wx.EVT_TREE_ITEM_MENU, self.on_context_menu)
        if not project is None:
            self.redraw_tree(project)
            EventChannel().subscribe(
                'tree_update',
                lambda: self.redraw_tree(self.project)
            )
    
    def parse_project_structure(self, project: ReportProject):
        self.nodes = {}
        self.root = self.AddRoot(
            project.get_current_version().code
        )
        self.nodes[self.root] = get_tree_node(self, project, self.root, None)
        self.SetItemImage(self.root, 0, wx.TreeItemIcon_Normal)
        self._parse_tomes(project.get_current_version())
        self.ExpandAll()
    
    def _parse_tomes(self, version: Version):
        for tome in version.tomes:
            tome_id = self.AppendItem(
                self.root,
                f'[{tome.basename}] {tome.human_readable_name}'
            )
            tome_node = get_tree_node(
                self,
                tome,
                tome_id,
                self.nodes[self.root]
            )
            self.nodes[tome_id] = tome_node
            self._parse_elements(tome_id, tome_node, tome)
            self.SetItemImage(tome_id, 1, wx.TreeItemIcon_Normal)
    
    def _parse_elements(self, parent: wx.TreeItemId, parent_node: TreeNode, tome: Tome):
        for el in tome.structural_elements:
            el_id = self.AppendItem(
                parent,
                f'[{el.code_attr}] {el.name}'
            )
            el_node = get_tree_node(self, el, el_id, parent_node)
            self.nodes[el_id] = el_node
            self.SetItemImage(el_id, 2, wx.TreeItemIcon_Normal)
            self._parse_files(el_id, el_node, el)
        return
    
    def _parse_files(
            self,
            parent: wx.TreeItemId,
            parent_node: TreeNode,
            element: StructuralElement
        ):
        for file in element.files:
            file_name = f'({file.subset}) {file.path.name}' \
                if len(str(file.subset)) > 0 \
                else str(file.path.name)
            file_id = self.AppendItem(
                parent,
                file_name
            )
            self.nodes[file_id] = get_tree_node(
                self,
                file,
                file_id,
                parent_node
            )
            self.SetItemImage(file_id, 3, wx.TreeItemIcon_Normal)
        return
    
    def redraw_tree(self, project: ReportProject):
        self.DeleteAllItems()
        self.project = project
        self.parse_project_structure(project)
    
    def on_context_menu(self, event):
        self.nodes[event.Item].context_menu.show_menu(event)