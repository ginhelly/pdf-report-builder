from dataclasses import dataclass, field
from pathlib import Path
from typing import List

from pypdf import PdfReader

from .pages_subset import PagesSubset
from pdf_report_builder.structure.level import BaseLevel

@dataclass
class PDFFile(BaseLevel):
    """
    Класс для работы с PDF-файлом на диске.
    По умолчанию при создании читает файл через PyPDF.PdfReader
    
    Свойства:
    path - путь до файла (pathlib.Path)
    pages_number - число страниц в файле
    pdf_reader - PyPDF.PdfReader
    subset - подмножество страниц файла (PagesSubset)
    """
    path: Path
    subset: str | PagesSubset = '',
    instant_read: bool = True

    def __post_init__(self) -> None:
        if not self.path.exists():
            self.valid = False
        elif not (self.path.is_file() and self.path.suffix == '.pdf'):
            self.valid = False
        else:
            self.valid = True
        if (not type(self.subset) == str) and (not isinstance(self.subset, PagesSubset)):
            self.subset = ''
        if self.instant_read and self.valid:
            self.read_file()
    
    def read_file(self):
        with open(self.path, 'rb') as file:
            pdf_reader = PdfReader(file)
            self.pages_number = len(pdf_reader.pages)
        self._parse_subset(self.subset)
    
    def change_file(self, path: Path):
        assert path.is_file() and path.suffix == '.pdf'
        self.path = path
        self.subset = ''
        self.read_file()
    
    def _parse_subset(self, subset: str | PagesSubset):
        if isinstance(subset, PagesSubset):
            self.subset = subset
            return
        if subset in ('', 'all', '__all__', '.'):
            self.subset = PagesSubset(max_page_num=self.pages_number)
        else:
            self.subset = PagesSubset.from_string(
                subset,
                max_page_num=self.pages_number
            )
    
    def change_subset(self, subset: str | PagesSubset):
        self._parse_subset(subset)
    
    @property
    def subset_pages_number(self):
        return len(self.subset)
    
    @staticmethod
    def from_dict(d: dict):
        if 'path' in d:
            d['path'] = Path(d['path'])
        change_subset = False
        if 'subset' in d:
            subset = d['subset']
            del d['subset']
            change_subset = True
        d['instant_read'] = True \
            if not 'instant_read' in d or d['instant_read'] == 'True' \
            else False
        valid = ['path', 'subset', 'instant_read']
        for key in list(d.keys()):
            if not key in valid:
                del d[key]
        file = PDFFile(**d)
        if change_subset:
            file.change_subset(subset)
        return file