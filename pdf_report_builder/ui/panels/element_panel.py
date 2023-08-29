import os
from pathlib import Path

import wx
from pdf_report_builder.ui.form_builder.main import BaseElementPanel
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.structure.structural_elements.computed_types import ComputedTypes
from pdf_report_builder.structure.structural_elements.tome_contents import TomeContentsElement
from pdf_report_builder.ui.dialogs.error_message import ErrorDialog
from pdf_report_builder.project.event_channel import EventChannel

class ElementPanel(BaseElementPanel):
    
    def parse_element(self, element: StructuralElement):
        self.element = element
        self.text_element_code.SetValue(element.code_attr)
        self.text_element_name.SetValue(element.name)
        self.cb_create_bookmark.SetValue(element.create_bookmark)
        self.cb_enumeration_include.SetValue(element.enumeration_include)
        self.cb_enumeration_print.SetValue(element.enumeration_print)
        self.cb_code_add.SetValue(element.code_add)
        self.cb_inner_enumeration.SetValue(element.inner_enumeration)
        self.fp_pdf_temp_path.GetPickerCtrl().SetLabel('Врем. PDF...')
        self.fp_template_docx.GetPickerCtrl().SetLabel('Шаблон...')
        if not element.enumeration_include:
            self.cb_enumeration_print.SetValue(False)
            self.element.enumeration_print = False
            self.cb_enumeration_print.Disable()
        else:
            self.cb_enumeration_print.Enable()
        if element.computed == ComputedTypes.TOME_CONTENTS.value:
            self.panel_computed.Show()
            self.parse_computed_element(element)
            self.Layout()
        else:
            self.panel_computed.Hide()
            self.Update()
            self.Layout()
    
    def parse_computed_element(self, element: TomeContentsElement):
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
        print('change', self.element)
        try:
            val = Path(self.fp_template_docx.GetPath())
            if not val.parent.exists():
                raise ValueError('Некорректный путь')
            self.element.doc_template = val
            print(self.element.doc_template)
        except Exception:
            dlg = ErrorDialog(None, 'Не удалось установить путь', 'Неправильный путь')
            dlg.ShowModal()
            dlg.Close()
    
    def on_text_element_code_change(self, event):
        new_value = self.text_element_code.GetValue()
        self.element.code_attr = new_value
        EventChannel().publish('element_name_update')
    
    def on_text_element_name_change(self, event):
        new_value = self.text_element_name.GetValue()
        self.element.name = new_value
        EventChannel().publish('element_name_update')
    
    def on_toggle_include(self, event):
        val = self.cb_enumeration_include.GetValue()
        self.element.enumeration_include = val
        if not val:
            self.cb_enumeration_print.SetValue(False)
            self.element.enumeration_print = False
            self.cb_enumeration_print.Disable()
        else:
            self.cb_enumeration_print.Enable()
    
    def on_toggle_print(self, event):
        val = self.cb_enumeration_print.GetValue()
        self.element.enumeration_print = val
    
    def on_toggle_bookmark_creation(self, event):
        val = self.cb_create_bookmark.GetValue()
        self.element.create_bookmark = val
    
    def on_toggle_code_add(self, event):
        val = self.cb_code_add.GetValue()
        self.element.code_add = val

    def on_toggle_inner_enumeration(self, event):
        val = self.cb_inner_enumeration.GetValue()
        self.element.inner_enumeration = val