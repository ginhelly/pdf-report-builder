import unittest
import os
from pathlib import Path
from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.algorithms.merge import merge

class TestMerge(unittest.TestCase):
    cwd = Path(os.getcwd())

    def test_merge_tomes(self):
        project2path = Path(os.getcwd()) / 'tests' / 'sample_pdf' / 'sample_project2.reportprj'
        project3path = Path(os.getcwd()) / 'tests' / 'sample_pdf' / 'sample_project3.reportprj'
        proj = ReportProject.open(project2path)
        print(proj)
        print(list(proj.versions[0].tomes[0].structural_elements[1].files[0].subset))
        merge(proj)
        