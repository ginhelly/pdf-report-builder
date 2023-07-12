from pdf_report_builder.project.base_project import BaseReportProject
from pdf_report_builder.structure.version import Version
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.structure.files.input_pdf import PDFFile

def _reload_element_files(el: StructuralElement):
    for file in el.files:
        file.on_modified()
    for subel in el.subelements:
        _reload_element_files(subel)

def reload_files(project: BaseReportProject):
    ver = project.get_current_version()
    for tome in ver.tomes:
        for el in tome.structural_elements:
            _reload_element_files(el)