import wx
from pdf_report_builder.ui.form_builder.main import BaseElementPanel
from pdf_report_builder.structure.structural_elements.base import StructuralElement
from pdf_report_builder.project.event_channel import EventChannel

class ElementPanel(BaseElementPanel):
    
    def parse_element(self, element: StructuralElement):
        self.element = element
        self.text_element_code.SetValue(element.code_attr)
        self.text_element_name.SetValue(element.name)
        self.cb_official.SetValue(element.official)
    
    def on_text_element_code_change(self, event):
        new_value = self.text_element_code.GetValue()
        self.element.code_attr = new_value
        EventChannel().publish('element_name_update')
    
    def on_text_element_name_change(self, event):
        new_value = self.text_element_name.GetValue()
        self.element.name = new_value
        EventChannel().publish('element_name_update')
    
    def on_toggle_official(self, event):
        val = self.cb_official.GetValue()
        self.element.official = val