import wx
from dataclasses import asdict
from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.structure.version import Version
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.ui.tree.tree_icons import get_tree_images
from .tree_node import *
from pdf_report_builder.project.event_channel import EventChannel
from pdf_report_builder.structure.level_enum import NodeType

def get_tome_name(tome: Tome):
    return f'[{tome.basename}] {tome.human_readable_name}'

def get_element_name(el: StructuralElement):
    return f'[{el.code_attr}] {el.name}'

def get_file_name(file: PDFFile):
    if not (file.path.exists() and file.path.is_file()):
        return f'[ПОТЕРЯН] {file.path.name}'
    return f'({file.subset}) {file.path.name}' \
            if len(str(file.subset)) > 0 \
            else str(file.path.name)

class Tree(wx.TreeCtrl):
    def __init__(self, parent, project = None):
        super().__init__(
            parent,
            wx.ID_ANY,
            style=wx.TR_DEFAULT_STYLE
        )
        self.AssignImageList(get_tree_images())
        self.Bind(wx.EVT_TREE_ITEM_MENU, self.on_context_menu)
        self.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.set_expanded)
        self.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.set_expanded)
        self._programmatic_collapse = False
        if not project is None:
            self.redraw_tree(project)
            EventChannel().subscribe(
                'tree_update',
                lambda: self.redraw_tree(self.project)
            )
        EventChannel().subscribe('tome_name_update', self.update_selected_tome_name)
        EventChannel().subscribe('element_name_update', self.update_selected_el_name)
        EventChannel().subscribe('file_name_update', self.update_selected_file_name)
        self.Bind(wx.EVT_TREE_BEGIN_DRAG, self.on_drag_start)
        self.Bind(wx.EVT_TREE_END_DRAG, self.on_drag_end)
        self._drag_item = None
    
    def parse_project_structure(self, project: ReportProject):
        self.nodes = {}
        self.root = self.AddRoot(
            project.get_current_version().code
        )
        self.nodes[self.root] = get_tree_node(self, project, self.root, None)
        self.SetItemImage(self.root, 0, wx.TreeItemIcon_Normal)
        self._parse_tomes(project.get_current_version())
        self.manage_expanded()
    
    def manage_expanded(self):
        self._programmatic_collapse = True
        self.ExpandAll()
        for item_id in self.nodes:
            level = self.nodes[item_id].item
            if not type(level) == ReportProject and not self.nodes[item_id].item.is_expanded:
                self.Collapse(item_id)
            else:
                self.Expand(item_id)
        self._programmatic_collapse = False
    
    def _parse_tomes(self, version: Version):
        for tome in version.tomes:
            tome_id = self.create_tome_item_id(tome, self.root)
            tome_node = get_tree_node(
                self,
                tome,
                tome_id,
                self.nodes[self.root]
            )
            self.nodes[tome_id] = tome_node
            self._parse_elements(tome_id, tome_node, tome)
    
    def _parse_elements(self, parent: wx.TreeItemId, parent_node: TreeNode, tome: Tome):
        for el in tome.structural_elements:
            el_id = self.create_element_item_id(el, parent)
            el_node = get_tree_node(self, el, el_id, parent_node)
            self.nodes[el_id] = el_node
            self._parse_subelements(el_id, el_node, el)
            self._parse_files(el_id, el_node, el)
        return

    def _parse_subelements(self, parent: wx.TreeItemId, parent_node: TreeNode, el: StructuralElement):
        if len(el.subelements) == 0:
            return
        for subel in el.subelements:
            subel_id = self.create_element_item_id(subel, parent)
            subel_node = get_tree_node(self, subel, subel_id, parent_node)
            self.nodes[subel_id] = subel_node
            self._parse_subelements(subel_id, subel_node, subel)
            self._parse_files(subel_id, subel_node, subel)
        return
    
    def _parse_files(
            self,
            parent: wx.TreeItemId,
            parent_node: TreeNode,
            element: StructuralElement
        ):
        for file in element.files:
            file_id = self.create_file_item_id(file, parent)
            self.nodes[file_id] = get_tree_node(
                self,
                file,
                file_id,
                parent_node
            )
        return
    
    def redraw_tree(self, project: ReportProject):
        self.DeleteAllItems()
        self.project = project
        self.Freeze()
        self.parse_project_structure(project)
        self.Thaw()
    
    def on_context_menu(self, event):
        self.nodes[event.Item].context_menu.show_menu(event, self.nodes[event.Item])
    
    def create_item_id(
            self,
            parent_id,
            previous=None,
            name='New Item',
            image=-1,
            expanded=True
        ):
        if previous is None:
            item_id = self.AppendItem(parent_id, name, image)
        else:
            item_id = self.InsertItem(parent_id, previous, name, image)
        return item_id
    
    def create_file_item_id(self, file: PDFFile, parent_id, previous=None):
        file_name = get_file_name(file)
        new_item = self.create_item_id(parent_id, previous, file_name, 3, file.is_expanded)
        if not (file.path.exists() and file.path.is_file()):
            self.SetItemBold(new_item)
            self.SetItemTextColour(new_item, wx.Colour(255,0,0))
        if file.modified:
            self.SetItemBackgroundColour(new_item, wx.Colour(0, 240, 240))
        return new_item
    
    def create_element_item_id(self, el: StructuralElement, parent_id, previous=None):
        el_name = get_element_name(el)
        icon = 4 if el.computed > 0 else 2
        return self.create_item_id(parent_id, previous, el_name, icon, el.is_expanded)
    
    def create_tome_item_id(self, tome: Tome, parent_id, previous=None):
        tome_name = get_tome_name(tome)
        return self.create_item_id(parent_id, previous, tome_name, 1, tome.is_expanded)
    
    def swap(self, node_i: TreeNode, node_j: TreeNode):
        parent = node_i.parent # проверка на бездуховность
        parent2 = node_j.parent
        if parent2 != parent:
            raise ValueError('Айтемы должны быть одного уровня!')
        # Делает своп внутри дерева и в модели
        self.Freeze()
        parent.swap(node_i.index, node_j.index, node_i)
        def redraw_item_by_node(tree, node, parent_node):
            del tree.nodes[node.item_id]
            tree.Delete(node.item_id)
            if isinstance(node.item, PDFFile):
                new_id = self.create_file_item_id(node.item, parent_node.item_id, node.index)
            elif isinstance(node.item, StructuralElement):
                new_id = self.create_element_item_id(node.item, parent_node.item_id, node.index)
            elif isinstance(node.item, Tome):
                new_id = self.create_tome_item_id(node.item, parent_node.item_id, node.index)
            tree.nodes[new_id] = node
            node.item_id = new_id
        to_swap = sorted(
            (node_i, node_j),
            key=lambda node: node.index,
            reverse=True
        )
        for n in to_swap:
            redraw_item_by_node(self, n, parent)
            if isinstance(n.item, StructuralElement):
                n.children = []
                self._parse_subelements(n.item_id, n, n.item)
                self._parse_files(n.item_id, n, n.item)
            elif isinstance(n.item, Tome):
                n.children = []
                self._parse_elements(n.item_id, n, n.item)
        EventChannel().publish('modified')
        self.manage_expanded()
        self.Thaw()
    
    def rearrange(self, source_node: TreeNode, target_node: TreeNode):
        self.Freeze()
        parent = source_node.parent
        parent.rearrange(source_node.index, target_node.index, source_node)
        self.redraw_tree(self.project)
        EventChannel().publish('modified')
        self.manage_expanded()
        self.Thaw()

    def append_as_child(self, source_node: TreeNode, target_node: TreeNode):
        self.Freeze()
        source_item = source_node.item
        source_parent = source_node.parent.item
        source_parent.remove_child(source_item)
        target_item = target_node.item
        target_item.append_child(source_item)
        self.redraw_tree(self.project)
        EventChannel().publish('modified')
        self.manage_expanded()
        self.Thaw()
    
    def update_selected_tome_name(self):
        item_id = self.GetSelection()
        tome = self.nodes[item_id].item
        new_name = get_tome_name(tome)
        self.SetItemText(item_id, new_name)
    
    def update_selected_el_name(self):
        item_id = self.GetSelection()
        el = self.nodes[item_id].item
        new_name = get_element_name(el)
        self.SetItemText(item_id, new_name)

    def update_selected_file_name(self):
        item_id = self.GetSelection()
        file = self.nodes[item_id].item
        new_name = get_file_name(file)
        self.SetItemText(item_id, new_name)
        if file.path.exists() and file.path.is_file():
            self.SetItemBold(item_id, False)
            self.SetItemTextColour(item_id, wx.Colour(0,0,0))
    
    def set_expanded(self, event: wx.TreeEvent):
        if self._programmatic_collapse:
            return
        item_id = event.GetItem()
        level = self.nodes[item_id].item
        is_itemid_expanded = self.IsExpanded(item_id)
        if type(level) == ReportProject:
            return
        if is_itemid_expanded:
            level.set_expanded(True)
        else:
            level.set_expanded(False)

    def _same_level(self, node1: TreeNode, node2: TreeNode):
        return node1.item.level == node2.item.level \
            and node1.parent == node2.parent
    
    def _can_append_as_child(self, parent: TreeNode, child: TreeNode):
        def is_not_a_computed_element(item):
            if item.level == NodeType.ELEMENT and item.is_computed:
                return False
            return True
        if parent.item.level == NodeType.ELEMENT\
            and is_not_a_computed_element(parent.item) \
            and child.item.level == NodeType.ELEMENT:
            return True
        if (child.item.level.value - parent.item.level.value == 1) \
            and is_not_a_computed_element(parent.item) \
            and is_not_a_computed_element(child.parent.item):
            return True
        return False
    
    def on_drag_start(self, event):
        event.Allow()
        self._drag_item = event.GetItem()

    def on_drag_end(self, event):
        dragged_item = self._drag_item
        target_item = event.GetItem()
        dragged_node = self.nodes[dragged_item]
        target_node = self.nodes[target_item]
        
        same_level = self._same_level(dragged_node, target_node)
        can_append_as_child = self._can_append_as_child(target_node, dragged_node)
        rearrange = lambda: self.rearrange(dragged_node, target_node)
        append_as_child = lambda: self.append_as_child(dragged_node, target_node)

        if same_level and can_append_as_child:
            def menu_handler(event):
                id = event.GetId()
                if id == 0:
                    append_as_child()
                elif id == 1:
                    rearrange()

            menu = wx.Menu()
            menu.Append(0, 'Внутрь')
            menu.Append(1, 'На его место')
            self.Bind(wx.EVT_MENU, menu_handler)
            self.PopupMenu(menu, event.GetPoint())
            menu.Destroy()
        elif self._same_level(dragged_node, target_node):
            self.rearrange(dragged_node, target_node)
        elif self._can_append_as_child(target_node, dragged_node):
            self.append_as_child(dragged_node, target_node)
