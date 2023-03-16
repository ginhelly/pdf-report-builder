import io
import json
import os
import unittest
from dataclasses import asdict
from pathlib import Path

from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.project.io.base_serializer import BaseSerializer
from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.structure.files.pages_subset import PagesSubset
from pdf_report_builder.structure.structural_elements.base import \
    StructuralElement
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.version import Version

from pdf_report_builder.project.io.json_serializer import *

class TestPagesSubset(unittest.TestCase):
    subset = PagesSubset.from_string('10-15,18,20-22')
    file = PDFFile(
        Path(os.getcwd()) / 'tests' / 'sample_pdf' / 'sample_report.pdf',
        '10-12,15,110-.'
    )
    el = StructuralElement(
        'Картограмма',
        False,
        'КТГИ',
        [file]
    )
    tome = Tome(
        'ИГДИ1-Т',
        'Текстовая часть',
        [el]
    )
    ver = Version(
        'Версия для промгаза',
        [tome]
    )
    project = ReportProject(
        [ver]
    )
    """
    def test_serialize_level_subset(self):
        print('=====> SUBSET: ', type(serialize_level(self.subset)))
    
    def test_serialize_level_file(self):
        print('=====> FILE: ', serialize_level(self.file))
    
    def test_serialize_level_StructuralElement(self):
        print('=====> ELEMENT: ', serialize_level(self.el))
    
    def test_serialize_level_Tome(self):
        print('=====> TOME: ', serialize_level(self.tome))
    
    def test_serialize_level_Version(self):
        print('=====> VERSION: ', serialize_level(self.ver))
    
    def test_serialize_level_project(self):
        print('=====> PROJECT: ', serialize_level(self.project))
    
    def test_write_to_file(self):
        self.project.save()
    
    def test_saveas(self):
        new_path = Path(os.getcwd()) / 'tests' / 'sample_pdf' / 'sample_project.json'
        self.project.save_as(new_path)
"""
    
    def test_parse_settings(self):
        project2path = Path(os.getcwd()) / 'tests' / 'sample_pdf' / 'sample_project2.json'
        project3path = Path(os.getcwd()) / 'tests' / 'sample_pdf' / 'sample_project3.json'
        project = ReportProject.open(project2path)
        project.save_as(project3path)
