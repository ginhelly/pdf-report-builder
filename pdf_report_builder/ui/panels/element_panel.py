import os
from pathlib import Path

import wx
from pdf_report_builder.ui.form_builder.main import BaseElementPanel
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.structure.structural_elements.computed import ComputedElement
from pdf_report_builder.ui.panels.computed.panel_factory import get_computed_props_panel
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
        if not element.enumeration_include:
            self.cb_enumeration_print.SetValue(False)
            self.element.enumeration_print = False
            self.cb_enumeration_print.Disable()
        else:
            self.cb_enumeration_print.Enable()
        if element.is_computed:
            if hasattr(self, '_current_panel'):
                self._current_panel.update_element(element)
            self.panel_computed.Show()
            self.parse_computed_element(element)
            # вешайся нахуй
            self.Freeze()
            new_panel = get_computed_props_panel(element, self.computed_props_container)
            if not new_panel is None:
                sizer = self.computed_props_container.GetSizer()
                if hasattr(self, '_current_panel'):
                    sizer.Remove(0)
                    self.Layout()
                    self.Refresh()
                    self.Update()
                self.computed_props_container.GetSizer().Add(new_panel, 1, wx.EXPAND | wx.ALL)
                self._current_panel = new_panel
            self.Layout()
            self.Thaw()
            print(self._current_panel.fp_template_docx.Path)
        else:
            self.panel_computed.Hide()
            self.Update()
            self.Layout()
    
    def parse_computed_element(self, element: ComputedElement):
        self.fp_pdf_temp_path.SetPath(str(element.pdf_temp_path))
    
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