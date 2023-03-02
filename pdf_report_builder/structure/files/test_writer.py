import unittest
import os
from pathlib import Path
from PyPDF2 import PdfWriter
from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.structure.files.pages_subset import PagesSubset

class TestMerge(unittest.TestCase):
    cwd = Path(os.getcwd())
    report_113pages = cwd / 'tests' / 'sample_pdf' / 'sample_report.pdf'
    survey_net = cwd / 'tests' / 'sample_pdf' / 'sample_survey_net.pdf'
    ktgi = cwd / 'tests' / 'sample_pdf' / 'sample_ktgi.pdf'
    res_dir = cwd / 'tests' / 'sample_pdf' / 'res'

    def test_merge_pdfs(self):
        merger = PdfWriter()

        input1 = open(self.survey_net, 'rb')
        input2 = open(self.ktgi, 'rb')

        subset1 = list(PagesSubset.from_string('3-5,10'))
        merger.append(fileobj=input1, pages=subset1)

        merger.append(fileobj=input2)

        # Write to an output PDF document
        output = open(self.res_dir / 'merge.pdf', 'wb')
        merger.write(output)

        # Close File Descriptors
        merger.close()
        output.close()

    def test_merge_pdfs_failure(self):
        def for_test():
            merger = PdfWriter()

            input1 = open(self.survey_net, 'rb')
            input2 = open(self.ktgi, 'rb')

            subset1 = list(PagesSubset.from_string('3-5,40', 13))
            merger.append(fileobj=input1, pages=subset1)

            merger.append(fileobj=input2)

            # Write to an output PDF document
            output = open(self.res_dir / 'merge.pdf', 'wb')
            merger.write(output)

            # Close File Descriptors
            merger.close()
            output.close()
        self.assertRaises(ValueError, for_test)