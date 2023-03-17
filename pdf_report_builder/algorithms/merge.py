from pypdf import PdfWriter
from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.files.input_pdf import PDFFile

def _merge_one_tome(tome: Tome):
    files_to_merge = []
    for element in tome.structural_elements:
        files_to_merge = files_to_merge + element.files
    merger = PdfWriter()
    inputs = [
        file.path for file in files_to_merge
    ]
    subsets = [
        list(file.subset) for file in files_to_merge
    ]
    for obj, subset in zip(inputs, subsets):
        if len(subset) == 0:
            merger.append(fileobj=obj)
        else:
            merger.append(fileobj=obj, pages=subset)
    with open(tome.savepath, 'wb') as output:
        merger.write(output)
        merger.close()

def merge(project: ReportProject):
    """Самое-самое главное, ради чего всё это затевалось"""
    ver = project.get_default_version()
    for tome in ver.tomes:
        _merge_one_tome(tome)