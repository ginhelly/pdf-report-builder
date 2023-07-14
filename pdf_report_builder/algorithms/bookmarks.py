from pypdf import PdfWriter

from pdf_report_builder.algorithms.parse_pages_count import ParseReportNode

def _add_bookmarks_recursive(
        writer: PdfWriter,
        node: ParseReportNode,
        parent,
        logger
    ):
    for child in node.children:
        if child.create_bookmark:
            kin = writer.add_outline_item(
                child.name,
                child.page_number_in_pdf_tome,
                parent
            )
            logger.writeline(f'  Добавил закладку {child.name} на странице {child.page_number_in_pdf_tome + 1}')
        else:
            kin = parent
        _add_bookmarks_recursive(writer, child, kin, logger)

    
def add_bookmarks(
        writer: PdfWriter,
        tome_node: ParseReportNode,
        logger
    ):
    for child in tome_node.children:
        if child.create_bookmark:
            parent = writer.add_outline_item(
                child.name,
                child.page_number_in_pdf_tome
            )
            logger.writeline(f'  Добавил закладку {child.name} на странице {child.page_number_in_pdf_tome + 1}')
        else:
            parent = None
        _add_bookmarks_recursive(writer, child, parent, logger)
