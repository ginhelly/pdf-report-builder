from pdf_report_builder.ui.form_builder.main import MainFrame
from pdf_report_builder.ui.about import PRBAboutDialog
from pdf_report_builder.utils.docs import open_docs
from pdf_report_builder.project.project import ReportProject

class PDFReportBuilderFrame(MainFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_new_project()
    
    def onExit(self, event):
        self.Close(True)
    
    def onAbout(self, event):
        about = PRBAboutDialog(self)
        about.ShowModal()
        about.Destroy()
    
    def onDocsOpen101(self, event):
        open_docs('GOST101')
    
    def onDocsOpen105(self, event):
        open_docs('GOST105')
    
    def onDocsOpen301(self, event):
        open_docs('GOST301')
    
    def onDocsOpen47(self, event):
        open_docs('SP47')
    
    def onDocsOpen317(self, event):
        open_docs('SP317')
    
    def create_new_project(self):
        self.project = ReportProject()
        self.lbl_project_name.SetLabelText(self.project.settings.name)