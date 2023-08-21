from .tome_contents import TomeContentsElement, TomeContentsPropsPanel
from pdf_report_builder.structure.structural_elements.computed import ComputedElement

def get_computed_props_panel(element: ComputedElement, parent):
    if isinstance(element, TomeContentsElement):
        return TomeContentsPropsPanel(element, parent)
    return None