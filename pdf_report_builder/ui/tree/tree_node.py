from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

import wx

from .base_context_menu import TreeContextMenu
from pdf_report_builder.structure.level import BaseLevel
from pdf_report_builder.project.base_project import BaseReportProject
from pdf_report_builder.ui.tree.context_menu_factory import get_context_menu

from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.structural_elements.base import StructuralElement

@dataclass
class TreeNode:
    item: BaseReportProject | BaseLevel
    item_id: wx.TreeItemId
    context_menu: TreeContextMenu
    parent: None | TreeNode = None
    children: List['TreeNode'] = field(default_factory=list)
    index: int = 0

    def _get_siblings_and_shift(self, node=None):
        shift = 0
        if isinstance(self.item, BaseReportProject):
            siblings = self.item.get_current_version().tomes
        elif isinstance(self.item, Tome):
            siblings = self.item.structural_elements
        elif isinstance(self.item, StructuralElement):
            if isinstance(node.item, StructuralElement):
                siblings = self.item.subelements
            else:
                siblings = self.item.files
                shift = len(self.item.subelements)
        return (siblings, shift)

    def swap(self, i: int, j: int, node=None):
        siblings, shift = self._get_siblings_and_shift(node)
        child_nodes = self.children
        siblings[i - shift], siblings[j - shift] = siblings[j - shift], siblings[i - shift]
        child_nodes[i], child_nodes[j] = child_nodes[j], child_nodes[i]
        child_nodes[i].index = i
        child_nodes[j].index = j
    
    def rearrange(self, old_i: int, new_i: int, node=None):
        siblings, shift = self._get_siblings_and_shift(node)
        child_nodes = self.children
        moving_sibling = siblings.pop(old_i - shift)
        siblings.insert(new_i - shift, moving_sibling)
        moving_node = child_nodes.pop(old_i)
        child_nodes.insert(new_i, moving_node)
        for i, node in enumerate(child_nodes):
            node.index = i
    
    def __repr__(self) -> str:
        item = str(type(self.item)).split('.')[-1]
        parent = '-' if self.parent is None else str(type(self.parent.item)).split('.')[-1]
        index = self.index
        lc = len(self.children)
        return f'TreeNode({item}#{index}, parent={parent}, child_count={lc})'
    
    @property
    def next(self):
        if self.parent is None:
            return None
        if len(self.parent.children) - 1 == self.index:
            return None
        return self.parent.children[self.index + 1]
    
    @property
    def prev(self):
        if self.parent is None:
            return None
        if self.index == 0:
            return None
        return self.parent.children[self.index - 1]

def get_tree_node(
        tree: wx.TreeCtrl,
        level: BaseReportProject | BaseLevel,
        item: wx.TreeItemId,
        parent: TreeNode | None = None
    ):
        context_menu = get_context_menu(tree, level)
        new_node = TreeNode(
            level,
            item,
            context_menu,
            parent
        )
        if not parent is None:
            parent.children.append(new_node)
            new_node.index = len(parent.children) - 1
        return new_node