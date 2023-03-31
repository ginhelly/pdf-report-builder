from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

import wx

from .base_context_menu import TreeContextMenu
from pdf_report_builder.structure.level import BaseLevel
from pdf_report_builder.project.base_project import BaseReportProject
from pdf_report_builder.ui.tree.context_menu_factory import get_context_menu

@dataclass
class TreeNode:
    item: BaseReportProject | BaseLevel
    context_menu: TreeContextMenu
    parent: None | TreeNode = None
    children: List['TreeNode'] = field(default_factory=list)

def get_tree_node(
        tree: wx.TreeCtrl,
        level: BaseReportProject | BaseLevel,
        item: wx.TreeItemId,
        parent: TreeNode | None = None
    ):
        context_menu = get_context_menu(tree, level)
        new_node = TreeNode(
            item,
            context_menu,
            parent
        )
        if not parent is None:
            parent.children.append(new_node)
        return new_node