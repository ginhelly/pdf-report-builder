import unittest
import os
from pathlib import Path
from pdf_report_builder.structure.structural_elements.base import *

class TestStructuralElementBase(unittest.TestCase):
    cwd = Path(os.getcwd())
    report_pdf_path = cwd / 'tests' / 'sample_pdf' / 'report2.pdf'
    subset = '130-133,135-138'

    def test_add_file(self):
        report = StructuralElement(
            'Отчет', True, 'ТЧ'
        )
        report.add_file(
            file_path=self.report_pdf_path,
            subset=self.subset
        )
    
    def test_add_file2(self):
        report = StructuralElement(
            'Отчет', True, 'ТЧ'
        )
        descr = FileDescription(
            self.report_pdf_path,
            self.subset
        )
        report.add_file(
            file_description=descr
        )
    
    def test_pages_number(self):
        report = StructuralElement(
            'Отчет', True, 'ТЧ'
        )
        report.add_file(
            file_path=self.report_pdf_path,
            subset=self.subset
        )
        self.assertEqual(
            report.pages_number,
            8
        )
        