import os
import wx
from pathlib import Path

from pdf_report_builder.structure.structural_elements.tome_contents import TomeContentsElement
from .element_panel import ElementPanel
from pdf_report_builder.ui.dialogs.error_message import ErrorDialog
from pdf_report_builder.project.event_channel import EventChannel

class TomeContentsPanel(ElementPanel):
    def parse_element(self, element: TomeContentsElement):
        super().parse_element(element)
        bSizer24 = self.GetSizer()
        self.m_staticline99 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer24.Add( self.m_staticline99, 0, wx.EXPAND |wx.ALL, 5 )
        self.fp_pdf_temp_path = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Место сохранения генерируемого PDF-документа", u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OVERWRITE_PROMPT|wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
        bSizer24.Add( self.fp_pdf_temp_path, 0, wx.ALL|wx.EXPAND, 5 )
        self.fp_template_docx = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Шаблон для генерации", u"Word Documents (*.doc;*.docx)|*.doc;*.docx", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer24.Add( self.fp_template_docx, 0, wx.ALL|wx.EXPAND, 5 )
        self.fp_pdf_temp_path.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_pdf_temp_path_change )
        self.fp_template_docx.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_template_docx_change )

        self.fp_pdf_temp_path.GetPickerCtrl().SetLabel('Место генерации PDF...')
        self.fp_template_docx.GetPickerCtrl().SetLabel('Шаблон...')
        self.fp_pdf_temp_path.SetPath(str(element.pdf_temp_path))
        self.fp_template_docx.SetPath(str(element.doc_template))
    
    def on_pdf_temp_path_change(self, event):
        try:
            val = Path(self.fp_pdf_temp_path.GetPath())
            if not val.parent.exists():
                raise ValueError('Некорректный путь')
            previous_path = self.element.pdf_temp_path
            if previous_path.exists() and previous_path.is_file():
                os.remove(previous_path)
            self.element.pdf_temp_path = val
            EventChannel().publish('tree_update')
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