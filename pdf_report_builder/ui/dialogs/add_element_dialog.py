import wx

from pdf_report_builder.ui.form_builder.main import BaseAddElementDialog
from pdf_report_builder.structure.structural_elements.list import *

class AddElementDialog(BaseAddElementDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.redraw_treelist(ELEMENTS_BY_SCHEME)
        ac = [(wx.ACCEL_NORMAL, wx.WXK_RETURN, wx.ID_OK)]
        tbl = wx.AcceleratorTable(ac)
        self.SetAcceleratorTable(tbl)
        self.Bind(wx.EVT_BUTTON, self.on_close, id=wx.ID_OK)

    def redraw_treelist(self, elements):
        self.treelist_elements.DeleteAllItems()
        for el_type in elements:
            category = self.treelist_elements.AppendItem(
                self.treelist_elements.GetRootItem(),
                el_type.value.upper()
            )
            for el_scheme in elements[el_type]:
                self.treelist_elements.AppendItem(
                    category,
                    el_scheme.dialog_name,
                    data=el_scheme
                )
            self.treelist_elements.Expand(category)
    
    def update_filter(self, event):
        text = self.search_bar.GetValue()
        self.redraw_treelist(
            filter_schemes(ELEMENTS_BY_SCHEME, text)
        )
    
    def on_sel_changed(self, event):
        sel = self.treelist_elements.GetSelection()
        item_data = self.treelist_elements.GetItemData(sel)
        self.update_code(item_data)
        self.toggle_ok_button(item_data)
    
    def toggle_ok_button(self, item_data):
        if item_data is None:
            self.btn_ok.Disable()
        else:
            self.btn_ok.Enable()
    
    def update_code(self, item_data):
        code = '' if item_data is None else item_data.code_attr
        self.element_code.SetValue(code)
    
    def get_element(self):
        sel = self.treelist_elements.GetSelection()
        scheme = self.treelist_elements.GetItemData(sel)
        if self.element_code.GetValue() != scheme.code_attr:
            scheme = ElementScheme(
                scheme.dialog_name,
                scheme.element_type,
                scheme.name,
                scheme.official,
                self.element_code.GetValue()
            )
        return scheme
    
    def on_close(self, event):
        sel = self.treelist_elements.GetSelection()
        if self.treelist_elements.GetItemData(sel) is None:
            return
        event.Skip()
