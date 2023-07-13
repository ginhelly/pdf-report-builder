from os.path import getmtime
from datetime import datetime
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

#from pypdf import PdfReader
import fitz

from .pages_subset import PagesSubset
from pdf_report_builder.structure.level import BaseLevel
from pdf_report_builder.project.storage_settings import SettingsStorage

@dataclass
class PDFFile(BaseLevel):
    """
    Класс для работы с PDF-файлом на диске.
    По умолчанию при создании читает файл через PyPDF.PdfReader
    
    Свойства:
    path - путь до файла (pathlib.Path)
    pages_number - число страниц в файле
    subset_pages_number - число страниц в подмножестве
    modified_datetime - дата и время изменения
    pdf_reader - PyPDF.PdfReader
    subset - подмножество страниц файла (PagesSubset)
    valid - найден ли PDF на диске
    file_modified - изменился ли файл
    """
    path: Path
    subset: str | PagesSubset = '',
    instant_read: bool = True
    expanded: bool = True

    def __post_init__(self) -> None:
        super().__post_init__()
        self.check_validity()
        self.modified = False
        if (not type(self.subset) == str) and (not isinstance(self.subset, PagesSubset)):
            self.subset = ''
        if self.instant_read and self.valid:
            self.read_file()

    def check_validity(self):
        if not self.path.exists():
            self.valid = False
        elif not (self.path.is_file() and self.path.suffix.lower() == '.pdf'):
            self.valid = False
        else:
            self.valid = True
    
    def read_file(self):
        self.modified_datetime = datetime.fromtimestamp(
            getmtime(self.path)
        )
        doc = fitz.open(self.path)
        self.pages_number = doc.page_count
        self._parse_subset(self.subset)
    
    def change_file(self, path: Path):
        assert path.is_file() and path.suffix == '.pdf'
        self.path = path
        self.subset = ''
        self.read_file()
    
    def on_deleted(self):
        self.valid = False
        self.subset = ''
        self.pages_number = 0

    def on_modified(self):
        self.check_validity()
        if self.instant_read and self.valid:
            self.read_file()
        if hasattr(self, 'subset') and type(self.subset) == PagesSubset:
            self.subset.update_max_page_num(self.pages_number)
        #self.modified = True
    
    def on_moved(self, new_path: str | Path):
        self.path = Path(new_path)
        self.modified = True
    
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
        len_subset = len(self.subset)
        if len_subset > 0:
            return len_subset
        try:
            pages_number = getattr(self, 'pages_number')
            return pages_number
        except AttributeError:
            return 0
    
    @property
    def code(self):
        return ''
