from pypdf import PdfWriter

from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.structural_elements.base import StructuralElement

def _add_bookmarks_recursive(
        writer: PdfWriter,
        el: StructuralElement,
        parent,
        page_number
    ):
    for subel in el.subelements:
        if subel.create_bookmark:
            kin = writer.add_outline_item(
                subel.name,
                page_number,
                parent
            )
        else:
            kin = parent
        print(f'name={subel.name}, ADD_BOOKMARK={subel.create_bookmark} parent={el.name}|{parent}')
        page_number = _add_bookmarks_recursive(writer, subel, kin, page_number)
        page_number = page_number + subel.pages_number
    return page_number

    
def add_bookmarks(
        writer: PdfWriter,
        tome: Tome
    ):
    page_number = 0
    for element in tome.structural_elements:
        if element.create_bookmark:
            parent = writer.add_outline_item(
                element.name,
                page_number
            )
        else:
            parent = None
        page_number = page_number + _add_bookmarks_recursive(writer, element, parent, page_number)
        page_number = page_number + element.pages_number
