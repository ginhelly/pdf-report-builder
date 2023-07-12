import io
import json
import os
import unittest
from dataclasses import asdict
from pathlib import Path

from pdf_report_builder.structure.factory.project_factory import ReportProject
from pdf_report_builder.project.io.base_serializer import BaseSerializer
from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.structure.files.pages_subset import PagesSubset
from pdf_report_builder.structure.structural_elements.base import \
    StructuralElement
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.structure.version import Version

from pdf_report_builder.project.io.json_serializer import *

class TestPagesSubset(unittest.TestCase):
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
        new_path = Path(os.getcwd()) / 'tests' / 'sample_pdf' / 'sample_project.reportprj'
        self.project.save_as(new_path)

"""    
    def test_parse_settings(self):
        project2path = Path(os.getcwd()) / 'tests' / 'sample_pdf' / 'sample_project2.reportprj'
        project3path = Path(os.getcwd()) / 'tests' / 'sample_pdf' / 'sample_project3.reportprj'
        proj = ProjectFactory.open(project2path)
        print('MODIFIED 1 (FALSE): ', proj.modified)
        print(list(proj.versions[0].tomes[0].structural_elements[0].files[0].subset))
        proj.versions[0].tomes[0].structural_elements[0].name = 'Новое классное имя!'
        print('MODIFIED 2 (TRUE): ', proj.modified)
        proj.save_as(project3path)
        print('MODIFIED 3 (FALSE): ', proj.modified)
