from typing import List

from pdf_report_builder.structure.structural_elements.computed import ComputedElement
from pdf_report_builder.project.storage import ProjectStorage
from pdf_report_builder.structure.structural_elements.base import StructuralElement


def _collect_computed_recursive(elements: List[StructuralElement]) -> List[ComputedElement]:
    computed = []
    for el in elements:
        if isinstance(el, ComputedElement):
            computed.append(el)
        computed = computed + _collect_computed_recursive(el.subelements)
    return computed

def collect_computed() -> List[ComputedElement]:
    project = ProjectStorage().project
    ver = project.get_current_version()
    computed = []
    for tome in ver.tomes:
        computed = computed + _collect_computed_recursive(tome.structural_elements)
    return computed
