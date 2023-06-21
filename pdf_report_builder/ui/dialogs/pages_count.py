import os
from pathlib import Path

import wx

from pdf_report_builder.ui.form_builder.main import BasePagesCountDialog
from pdf_report_builder.project.storage import ProjectStorage
from pdf_report_builder.algorithms.parse_pages_count import parse_project_for_pages, ParseReportNode, NodeType

def get_pagescount_imagelist():
    imagelist = wx.ImageList(width=16, height=16)
    bitmap = wx.Bitmap(width=16, height=16, depth=32)
    bitmap.LoadFile(str(
        Path(os.getcwd()) / 'pdf_report_builder' / 'data' / 'error.png'
    ))
    imagelist.Add(bitmap)

    ICONS_FOLDER = Path(os.getcwd()) / 'pdf_report_builder' \
    / 'data' / 'icons_tree_16'
    for file in ICONS_FOLDER.iterdir():
        new_bitmap = wx.Bitmap(width=24, height=24, depth=32)
        new_bitmap.LoadFile(
            str(file)
        )
        imagelist.Add(new_bitmap)
    return imagelist

def _get_icon_image(node: ParseReportNode):
    if node.type == NodeType.VERSION:
        return 1
    elif node.type == NodeType.TOME:
        return 2
    elif node.type == NodeType.ELEMENT:
        return 3
    return -1

class PagesCountDialog(BasePagesCountDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.project = ProjectStorage().project
        print(self.project)
        if self.project is None:
            return
        root_node = parse_project_for_pages(self.project)
        #self.treelist.DeleteAllItems()
        root_item = self.treelist.GetRootItem()

        self.treelist.AssignImageList(get_pagescount_imagelist())
        self.treelist.AppendColumn('Кол-во листов')
        self.treelist.AppendColumn('Экв. А4')
        self.add_node_recursive(root_node, root_item)
        self.treelist.SetColumnWidth(0, 300)
        self.treelist.Expand(root_item)
        
    def add_node_recursive(self, node: ParseReportNode, parent_item):
        new_item = self.treelist.AppendItem(parent_item, node.name)
        self.treelist.SetItemText(new_item, 1, str(node.pages_native))
        if abs(node.pages_a4 - round(node.pages_a4)) > 0.1:
            a4_res = str(node.pages_a4)
        else:
            a4_res = str(round(node.pages_a4))
        self.treelist.SetItemText(new_item, 2, a4_res)
        for child in node.children:
            self.add_node_recursive(child, new_item)
        if node.type != NodeType.VERSION and node.pages_a4 >= 300:
            self.treelist.SetItemImage(new_item, 0, 0)
        else:
            icon = _get_icon_image(node)
            self.treelist.SetItemImage(new_item, icon, icon)
        self.treelist.Expand(new_item)
    
    def on_close(self, event):
        self.Close()