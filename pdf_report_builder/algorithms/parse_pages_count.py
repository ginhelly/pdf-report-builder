from enum import Enum
from pathlib import Path
from typing import List
from dataclasses import dataclass, field

from pypdf import PdfReader

from pdf_report_builder.paperformats.format import PaperFormatStorage
from pdf_report_builder.project.base_project import BaseReportProject
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.structure.files.input_pdf import PDFFile

class NodeType(Enum):
    VERSION = 0
    TOME = 1
    ELEMENT = 2
    FILE = 3

@dataclass
class ParseReportNode:
    name: str
    type: NodeType
    pages_native: int = 0
    pages_a4: float = 0.0
    children: List['ParseReportNode'] = field(default_factory=lambda: [])

def _parse_pages_read_pdf(file: PDFFile):
    pages_native = file.subset_pages_number
    if not (file.path.exists() and file.path.is_file()):
        return (pages_native, 0)
    
    reader = PdfReader(file.path)
    P = PaperFormatStorage()
    pages_a4 = 0.0
    
    for page_number in list(file.subset):
        page = reader.pages[page_number]
        width = page.mediabox.width * page.user_unit * 25.4 / 72 
        height = page.mediabox.height * page.user_unit * 25.4 / 72 
        paper_format = P.find_format_by_size(width, height)
        pages_a4 = pages_a4 + paper_format.multiple_of_a4
    return (pages_native, pages_a4)
        

def _parse_pages_parse_file(file: PDFFile, parent: ParseReportNode):
    file_name = Path(file.path).name
    file_node = ParseReportNode(file_name, NodeType.FILE)
    parent.children.append(file_node)
    pages_native, pages_a4 = _parse_pages_read_pdf(file)
    file_node.pages_native = pages_native
    file_node.pages_a4 = pages_a4

def _parse_pages_parse_element(element: StructuralElement, parent: ParseReportNode):
    element_node = ParseReportNode(element.name, NodeType.ELEMENT)
    parent.children.append(element_node)
    for subel in element.subelements:
        _parse_pages_parse_element(subel, element_node)
    for file in element.files:
        _parse_pages_parse_file(file, element_node)
    element_node.pages_a4 += sum(
        node.pages_a4 for node in element_node.children if node.type == NodeType.FILE
    )
    element_node.pages_native += sum(
        node.pages_native for node in element_node.children if node.type == NodeType.FILE
    )
    element_node.pages_a4 += sum(
        node.pages_a4 for node in element_node.children if node.type == NodeType.ELEMENT
    )
    element_node.pages_native += sum(
        node.pages_native for node in element_node.children if node.type == NodeType.ELEMENT
    )


def _parse_pages_parse_tome(tome: Tome, parent: ParseReportNode):
    tome_node = ParseReportNode(tome.human_readable_name, NodeType.TOME)
    parent.children.append(tome_node)
    for element in tome.structural_elements:
        _parse_pages_parse_element(element, tome_node)
    tome_node.pages_a4 += sum(
        node.pages_a4 for node in tome_node.children
    )
    tome_node.pages_native += sum(
        node.pages_native for node in tome_node.children
    )

def parse_project_for_pages(project: BaseReportProject):
    ver = project.get_current_version()
    root_node = ParseReportNode(ver.name, NodeType.VERSION)
    for tome in ver.tomes:
        _parse_pages_parse_tome(tome, root_node)
    root_node.pages_a4 += sum(
        node.pages_a4 for node in root_node.children
    )
    root_node.pages_native += sum(
        node.pages_native for node in root_node.children
    )
    return root_node