from pathlib import Path
from PyPDF2 import PdfReader
from .pages_subset import PagesSubset

class PDFFile:
    def __init__(self, path: Path, subset: str | PagesSubset = '') -> None:
        if not path.exists():
            raise FileNotFoundError()
        if not (path.is_file() and path.suffix == '.pdf'):
            raise ValueError('Поддерживаются только PDF-файлы')
        self.path = path
        with open(path, 'rb') as file:
            self.pdf_reader = PdfReader(file)
            self.pages = len(self.pdf_reader.pages)
        self._parse_subset(subset)
    
    def _parse_subset(self, subset: str | PagesSubset):
        if isinstance(subset, PagesSubset):
            self.subset = subset
            return
        if subset in ('', 'all', '__all__'):
            self.subset = PagesSubset(max_page_num=self.pages)
        else:
            self.subset = PagesSubset.from_string(
                subset,
                max_page_num=self.pages
            )
    
    def change_subset(self, subset: str | PagesSubset):
        self._parse_subset(subset)