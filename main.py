from pdf_report_builder.ui.main import PDFReportBuilderFrame
import wx

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = PDFReportBuilderFrame(None)

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()