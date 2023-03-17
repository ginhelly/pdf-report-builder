import os
import subprocess
from pathlib import Path

def open_docs(docs_name: str):
    if not docs_name[-4:] == '.pdf':
        docs_name = docs_name + '.pdf'
    cwd = Path(os.getcwd())
    docs_folder = cwd / 'pdf_report_builder' / 'data' / 'docs'
    doc_file = docs_folder / docs_name
    if doc_file.exists() and doc_file.is_file():
        os.startfile(str(doc_file))
