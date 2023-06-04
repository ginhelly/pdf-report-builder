from pypdf import PdfWriter

from pdf_report_builder.structure.tome import Tome
    
def add_bookmarks(
        writer: PdfWriter,
        tome: Tome
    ):
    page_number = 0
    print('-----')
    for element in tome.structural_elements:
        writer.add_outline_item(
            element.name,
            page_number
        )
        page_number = page_number + element.pages_number
        print(element.pages_number)