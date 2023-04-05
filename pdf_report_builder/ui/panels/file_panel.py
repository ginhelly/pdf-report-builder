import wx
from pathlib import Path
from pdf_report_builder.ui.form_builder.main import BaseFilePanel
from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.project.event_channel import EventChannel
from pdf_report_builder.ui.dialogs.error_message import ErrorDialog

class FilePanel(BaseFilePanel):
    def parse_file(self, file: PDFFile):
        self.file = file
        self.fp_file.SetPath(
            str(file.path)
        )
        self._update_fields()
    
    def _update_fields(self):
        self.text_file_name.SetValue(self.file.path.name)
        self.text_pages_number.SetValue(str(self.file.pages_number))
        self.text_subset.SetValue(str(self.file.subset))
    
    def on_file_change(self, event):
        try:
            path = Path(self.fp_file.GetPath())
            self.file.change_file(path)
            self._update_fields()
            EventChannel().publish('file_name_update')
        except Exception as e:
            dlg = ErrorDialog(None, str(e), 'Не удалось открыть файл')
            dlg.ShowModal()
            dlg.Close()