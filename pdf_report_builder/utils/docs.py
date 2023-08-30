import os
from pathlib import Path
from pdf_report_builder.utils.app_settings import AppSettings

def open_docs(docs_name: str):
    if not docs_name[-4:] == '.pdf':
        docs_name = docs_name + '.pdf'
    docs_folder = AppSettings.get('DATA_PATH') / 'docs'
    doc_file = docs_folder / docs_name
    if doc_file.exists() and doc_file.is_file():
        os.startfile(str(doc_file))
