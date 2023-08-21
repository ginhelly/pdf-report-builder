from pathlib import Path

import wx
from pdf_report_builder.ui.form_builder.main import BaseTomeContentsPropsPanel
from pdf_report_builder.structure.structural_elements.tome_contents import TomeContentsElement
from pdf_report_builder.ui.dialogs.error_message import ErrorDialog

class TomeContentsPropsPanel(BaseTomeContentsPropsPanel):
    def __init__(self, element: TomeContentsElement, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        super().__init__(parent, id, pos, size, style, name)
        self.update_element(element)
    
    def update_element(self, element: TomeContentsElement):
        self._element = element
        self.fp_template_docx.SetPath(str(element.doc_template))
        self.fp_template_docx.GetPickerCtrl().SetLabel('Шаблон...')
        self.Layout()
        self.Refresh()
        self.Update()

    def on_template_docx_change(self, event):
        print('change', self._element)
        try:
            val = Path(self.fp_template_docx.GetPath())
            if not val.parent.exists():
                raise ValueError('Некорректный путь')
            self._element.doc_template = val
            print(self._element.doc_template)
        except Exception:
            dlg = ErrorDialog(None, 'Не удалось установить путь', 'Неправильный путь')
            dlg.ShowModal()
            dlg.Close()