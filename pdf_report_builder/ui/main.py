from pdf_report_builder.ui.form_builder.main import MainFrame
from pdf_report_builder.ui.about import PRBAboutDialog

class PDFReportBuilderFrame(MainFrame):
    def __init__(self, parent):
        super().__init__(parent)
    
    def onExit(self, event):
        self.Close(True)
    
    def onAbout(self, event):
        about = PRBAboutDialog(self)
        about.ShowModal()
        about.Destroy()