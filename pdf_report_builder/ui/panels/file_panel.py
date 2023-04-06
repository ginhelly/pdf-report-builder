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
        if hasattr(self.file, 'pages_number'):
            self.text_pages_number.SetValue(str(self.file.pages_number))
        self.text_subset.SetValue(str(self.file.subset))
        if not hasattr(self.file, 'modified_datetime'):
            return
        self.lbl_modified_datetime.SetLabelText(
            self.file.modified_datetime.strftime('%d.%m.%Y %H:%M:%S')
        )
    
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
    
    def on_subset_change(self, event):
        try:
            new_subset = self.text_subset.GetValue()
            self.file.change_subset(new_subset)
            EventChannel().publish('file_name_update')
        except Exception as e:
            if 'invalid' in str(e):
                e = 'Некорректный ввод'
            dlg = ErrorDialog(None, str(e), 'Не удалось изменить подмножество')
            dlg.ShowModal()
            dlg.Close()