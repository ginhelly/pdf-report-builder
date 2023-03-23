from .tome import TomeContextMenu, Tome
from .project import ProjectContextMenu, BaseReportProject
from .element import ElementContextMenu, StructuralElement
from .file import FileContextMenu, PDFFile

def get_context_menu(level):
    if isinstance(level, BaseReportProject):
        return ProjectContextMenu(level)
    elif isinstance(level, Tome):
        return TomeContextMenu(level)
    elif isinstance(level, StructuralElement):
        return ElementContextMenu(level)
    elif isinstance(level, PDFFile):
        return FileContextMenu(level)
    raise TypeError('Unknown context menu target!')