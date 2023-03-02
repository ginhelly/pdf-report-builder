import unittest
import os
from pathlib import Path
from pdf_report_builder.structure.files.input_pdf import PDFFile

class TestInputPDF(unittest.TestCase):
    cwd = Path(os.getcwd())
    report_113pages = cwd / 'tests' / 'sample_pdf' / 'sample_report.pdf'
    survey_net = cwd / 'tests' / 'sample_pdf' / 'sample_survey_net.pdf'
    ktgi = cwd / 'tests' / 'sample_pdf' / 'sample_ktgi.pdf'

    def test_init(self):
        path = self.report_113pages
        self.assertEqual(
            PDFFile(path).pages,
            113
        )
    
    def test_subset_correct(self):
        path = self.survey_net
        self.assertListEqual(
            list(PDFFile(path, '3-5,10').subset),
            [3,4,5,10]
        )
    
    def test_subset_raises_value_error(self):
        path = self.survey_net
        x = lambda: PDFFile(path, '3-5,50')
        self.assertRaises(ValueError, x)
    
    def test_single_page(self):
        f = PDFFile(self.ktgi, '1')
        self.assertEqual(f.pages, 1)
    
    def test_single_page_raises_value_error(self):
        x = lambda: PDFFile(self.ktgi, '1-2')
        self.assertRaises(ValueError, x)
