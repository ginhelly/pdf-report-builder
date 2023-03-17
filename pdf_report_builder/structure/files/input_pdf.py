from dataclasses import dataclass, field
from pathlib import Path
from typing import List

from pypdf import PdfReader

from .pages_subset import PagesSubset
from pdf_report_builder.utils.parsing import continue_on_key_error

@dataclass
class PDFFile:
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
            raise FileNotFoundError()
        if not (self.path.is_file() and self.path.suffix == '.pdf'):
            raise ValueError('Поддерживаются только PDF-файлы')
        
        if (not type(self.subset) == str) and (not isinstance(self.subset, PagesSubset)):
            self.subset = ''
        if self.instant_read:
            self.read_file()
    
    def read_file(self):
        with open(self.path, 'rb') as file:
            self.pdf_reader = PdfReader(file)
            self.pages_number = len(self.pdf_reader.pages)
        self._parse_subset(self.subset)
    
    def _parse_subset(self, subset: str | PagesSubset):
        if isinstance(subset, PagesSubset):
            self.subset = subset
            return
        if subset in ('', 'all', '__all__'):
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
    
    @continue_on_key_error
    @staticmethod
    def from_dict(d: dict):
        d['path'] = Path(d['path'])
        subset = d['subset']
        del d['subset']
        d['instant_read'] = True if d['instant_read'] == 'True' else False
        file = PDFFile(**d)
        file.change_subset(subset)
        return file