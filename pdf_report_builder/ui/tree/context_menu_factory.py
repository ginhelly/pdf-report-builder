from .tome import TomeContextMenu, Tome
from .project import ProjectContextMenu, BaseReportProject
from .element import ElementContextMenu, StructuralElement
from .file import FileContextMenu, PDFFile

def get_context_menu(tree, level):
    if isinstance(level, BaseReportProject):
        return ProjectContextMenu(tree, level)
    elif isinstance(level, Tome):
        return TomeContextMenu(tree, level)
    elif isinstance(level, StructuralElement):
        return ElementContextMenu(tree, level)
    elif isinstance(level, PDFFile):
        return FileContextMenu(tree, level)
    raise TypeError('Unknown context menu target!')