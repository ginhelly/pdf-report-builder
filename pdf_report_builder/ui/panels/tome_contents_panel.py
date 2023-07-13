import wx
from pathlib import Path

from pdf_report_builder.structure.structural_elements.tome_contents import TomeContentsElement
from .element_panel import ElementPanel
from pdf_report_builder.ui.form_builder.main import BaseTomeContentsPanel
from pdf_report_builder.ui.dialogs.error_message import ErrorDialog

class TomeContentsPanel(BaseTomeContentsPanel, ElementPanel):
    def parse_element(self, element: TomeContentsElement):
        super().parse_element(element)
        self.fp_pdf_temp_path.GetPickerCtrl().SetLabel('Обзор...')
        self.fp_template_docx.GetPickerCtrl().SetLabel('Обзор...')
        self.fp_pdf_temp_path.SetPath(str(element.pdf_temp_path))
        self.fp_template_docx.SetPath(str(element.doc_template))
    
    def on_pdf_temp_path_change(self, event):
        try:
            val = Path(self.fp_pdf_temp_path.GetPath())
            if not val.parent.exists():
                raise ValueError('Некорректный путь')
            self.element.pdf_temp_path = val
        except Exception:
            dlg = ErrorDialog(None, 'Не удалось установить путь', 'Неправильный путь')
            dlg.ShowModal()
            dlg.Close()
    
    def on_template_docx_change(self, event):
        try:
            val = Path(self.fp_template_docx.GetPath())
            if not val.parent.exists():
                raise ValueError('Некорректный путь')
            self.element.doc_template = val
        except Exception:
            dlg = ErrorDialog(None, 'Не удалось установить путь', 'Неправильный путь')
            dlg.ShowModal()
            dlg.Close()