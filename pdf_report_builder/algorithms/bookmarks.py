from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import List, Optional, Any

from pypdf import PdfWriter
import fitz

from pdf_report_builder.algorithms.parse_pages_count import ParseReportNode
from pdf_report_builder.structure.level_enum import NodeType

@dataclass
class Bookmark:
    name: str
    pageref: int
    level: int = 1
    data: Any = None
    parent: Optional['Bookmark'] = None
    _children: List['Bookmark'] = field(default_factory=lambda: [])

    def is_root(self):
        return self.parent is None
    
    def add_child(self, child: 'Bookmark'):
        self._children.append(child)
        child.parent = self

    @property
    def children(self):
        return list(sorted(
            self._children,
            key = lambda child: child.pageref
        ))
    
    def __repr__(self) -> str:
        def repr_recursive(bookmark):
            vis = [f'{" " * bookmark.level}Bookmark(pageref={bookmark.pageref}, lvl={bookmark.level}): {bookmark.name}']
            if len(bookmark.children) > 0:
                vis.append(f'{" " * bookmark.level}children:')
                vis = vis + [repr_recursive(child) for child in bookmark.children]
            return '\n'.join(vis)
        return repr_recursive(self)
    

class BookmarkAddingLibrary(Enum):
    PYPDF = 0
    FITZ = 1


class BookmarkManager:
    def __init__(self) -> None:
        self._current_level = 0
        self._root = Bookmark('root', 0, 0)
        self._stack = [self._root]
        self._last_added = self._root
    
    def add_bookmark(self, bookmark: Bookmark, parent: Bookmark | None = None):
        if parent is None:
            parent = self._stack[-1]
        bookmark.level = parent.level + 1
        parent.add_child(bookmark)
        self._last_added = bookmark
    
    def create_bookmark(self, name: str, pageref: int, parent: Bookmark | None = None):
        bookmark = Bookmark(name, pageref)
        self.add_bookmark(bookmark, parent)
        return bookmark
    
    def set_last_bookmark_as_parent(self):
        self._stack.append(self._last_added)
    
    def lower_level(self, delta: int):
        if len(self._stack) <= delta:
            raise ValueError('The stack has less values than the delta provided!')
        for i in range(delta):
            self._stack.pop()
    
    def parse_pymupdf_toc(
            self,
            toc: list,
            start_page: int,
            node: ParseReportNode | None = None,
            parent_bookmark: Bookmark | None = None
        ):
        if parent_bookmark is None:
            parent_bookmark = self._root
        if not parent_bookmark in self._stack:
            self._stack.append(parent_bookmark)
        prev_lvl = 1
        for entry in toc:
            lvl, title, page = entry
            if not node is None:
                page = node.level.page_subset_index(page)
                if page is None:
                    continue
            if page < 1:
                page = start_page
            else:
                page = page + start_page - 1

            delta = lvl - prev_lvl
            if delta > 0:
                self.set_last_bookmark_as_parent()
            elif delta < 0:
                self.lower_level(-delta)
            self.create_bookmark(title, page)
            prev_lvl = lvl
    
    def _migrate_bookmarks_from_text_report(
        self,
        start_page: int,
        source_report_node: ParseReportNode,
        parent_bookmark: Bookmark | None = None
    ):
        '''https://pymupdf.readthedocs.io/en/latest/document.html#Document.get_toc'''
        if parent_bookmark is None:
            parent_bookmark = self._root
        doc = fitz.open(source_report_node.level.path)
        source_toc = doc.get_toc()
        self.parse_pymupdf_toc(source_toc, start_page, source_report_node, parent_bookmark)
    
    def parse_tome_node(self, tome_node: ParseReportNode):
        def parse_node_recursive(
                node: ParseReportNode,
                parent_bookmark: Bookmark | None = None
            ):
            if node.type == NodeType.FILE \
                and node.parent.create_bookmark \
                and 'текстовая часть' in node.parent.level.name.lower():
                self._migrate_bookmarks_from_text_report(
                    node.page_number_in_pdf_tome,
                    node,
                    parent_bookmark
                )
            if node.create_bookmark:
                new_bookmark = self.create_bookmark(
                    node.name, node.page_number_in_pdf_tome, parent_bookmark
                )
                new_parent = new_bookmark
            else:
                new_parent = parent_bookmark
            for child in node.children:
                parse_node_recursive(child, new_parent)
        parse_node_recursive(tome_node, self._root)
        print('~~~~~~~~~~~~~~~~~~~~~~~')
        #print(self._root)
    
    def write_bookmarks(self, library: BookmarkAddingLibrary, **kwargs):
        if library == BookmarkAddingLibrary.FITZ:
            raise NotImplementedError
        self._write_bookmarks_pypdf(**kwargs)
    
    def _write_bookmarks_pypdf(self, **kwargs):
        if not 'writer' in kwargs:
            raise AttributeError('BookmarkManager needs a pypdf.PdfWriter object to add bookmarks to')
        
        self._writer = kwargs['writer']
        def pypdf_callback(bookmark: Bookmark):
            if bookmark.parent is None:
                return
            parent_item = bookmark.parent.data
            outline_item = self._writer.add_outline_item(
                bookmark.name,
                bookmark.pageref,
                parent_item
            )
            bookmark.data = outline_item
            return

        self._iterate_over_bookmarks_recursive(
            self._root,
            pypdf_callback
        )
    
    def _iterate_over_bookmarks_recursive(self, start: Bookmark, callback: callable):
        callback(start)
        for child in start.children:
            self._iterate_over_bookmarks_recursive(child, callback)


def _add_bookmarks_recursive(
        writer: PdfWriter,
        node: ParseReportNode,
        parent,
        logger
    ):

    if node.create_bookmark:
        kin = writer.add_outline_item(
            node.name,
            node.page_number_in_pdf_tome,
            parent
        )
        
        logger.writeline(f'  Добавил закладку {node.name} на странице {node.page_number_in_pdf_tome + 1}')
    else:
        kin = parent
    for child in node.children:
        _add_bookmarks_recursive(writer, child, kin, logger)

    
def add_bookmarks(
        writer: PdfWriter,
        tome_node: ParseReportNode,
        logger
    ):
    bm = BookmarkManager()
    bm.parse_tome_node(tome_node)
    bm.write_bookmarks(BookmarkAddingLibrary.PYPDF, writer=writer)
    #for child in tome_node.children:
    #    _add_bookmarks_recursive(writer, child, None, logger)
