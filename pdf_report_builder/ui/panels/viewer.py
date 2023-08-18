import wx

import fitz

from pdf_report_builder.structure.files.input_pdf import PDFFile
from pdf_report_builder.project.event_channel import EventChannel


class PDFViewer:
    def __init__(self, parent) -> None:
        self.parent = parent
        self.panel = parent.viewer_panel
        EventChannel().subscribe('file_updated', self.on_file_change)
    
    def on_file_change(self, payload):
        self.change_file(payload[0])
        self.set_page(payload[0].subset_list[0])
    
    def change_file(self, file: PDFFile):
        self._file = file
        # if file not valid: blankify and gtfo
        self._doc = fitz.open(file.path)
        print(self._doc)
    
    def clear_page(self):
        if hasattr(self, 'static_bitmap'):
            self.static_bitmap.Destroy()
    
    def set_page(self, page_number: int):
        page = self._doc[page_number]

        self.clear_page()
        pix = page.get_pixmap()
        if pix.alpha:
            bitmap = wx.Bitmap.FromBufferRGBA(pix.width, pix.height, pix.samples)
        else:
            bitmap = wx.Bitmap.FromBuffer(pix.width, pix.height, pix.samples)
        
        self.static_bitmap = wx.StaticBitmap(self.panel, wx.ID_ANY, bitmap)
        sizer = self.panel.GetSizer()
        sizer.Add(self.static_bitmap, wx.EXPAND | wx.ALL, border=10)