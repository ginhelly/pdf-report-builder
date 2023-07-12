from pathlib import Path

from pdf_report_builder.project.base_project import BaseReportProject
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.structure.structural_elements.computed_types import ComputedTypes


def _check_computed(el: StructuralElement, root_path: Path):
    if el.computed == ComputedTypes.TOME_CONTENTS.value:
        if not el.doc_template.is_relative_to(root_path):
            return False
    return True

def _check_element(el: StructuralElement, root_path: Path):
    if el.computed > 0:
        if not el.pdf_temp_path.is_relative_to(root_path):
            return False
        if not _check_computed(el, root_path):
            return False
    for file in el.files:
        if not file.path.is_relative_to(root_path):
            return False
    for subel in el.subelements:
        if not _check_element(subel, root_path):
            return False
    return True
        

def _check_tome(tome: Tome, root_path: Path):
    if not tome.savepath.is_relative_to(root_path):
        print(f'{tome.savepath} is not relative to {root_path}')
        return False
    for el in tome.structural_elements:
        if not _check_element(el, root_path):
            return False
    return True

def all_paths_are_relative(project: BaseReportProject):
    root_path = project.settings.savepath.parent
    for ver in project.versions:
        for tome in ver.tomes:
            all_in_tome_relative = _check_tome(tome, root_path)
            if not all_in_tome_relative:
                return False
    return True