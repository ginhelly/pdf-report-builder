from pathlib import Path
from PyPDF2 import PdfReader
from .pages_subset import PagesSubset

class PDFFile:
    """
    Класс для работы с PDF-файлом на диске.
    По умолчанию при создании читает файл через PyPDF2.PdfReader
    
    Свойства:
    path - путь до файла (pathlib.Path)
    pages_number - число страниц в файле
    pdf_reader - PyPDF2.PdfReader
    subset - подмножество страниц файла (PagesSubset)
    """
    def __init__(self, path: Path, subset: str | PagesSubset = '', instant_read: bool = True) -> None:
        if not path.exists():
            raise FileNotFoundError()
        if not (path.is_file() and path.suffix == '.pdf'):
            raise ValueError('Поддерживаются только PDF-файлы')
        self.path = path
        self._subset_str = subset
        if instant_read:
            self.read_file()
    
    def read_file(self):
        with open(self.path, 'rb') as file:
            self.pdf_reader = PdfReader(file)
            self.pages_number = len(self.pdf_reader.pages)
        self._parse_subset(self._subset_str)
    
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