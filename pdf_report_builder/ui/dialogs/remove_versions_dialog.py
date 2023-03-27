import wx
from pdf_report_builder.ui.form_builder.main import BaseRemoveVersionsDialog
from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.structure.version import Version

class RemoveVersionsDialog(BaseRemoveVersionsDialog):
    def __init__(self, parent, project: ReportProject):
        super().__init__(parent)
        self.project = project
        self.populate_listbox(project.versions)
        self.toggle_remove_button()

    def populate_listbox(self, versions: list[Version]):
        self.listbox_versions.Clear()
        for ver in versions:
            self.listbox_versions.Append(ver.name)
    
    def toggle_remove_button(self, event=None):
        if len(self.project.versions) <= 1 \
            or len(self.listbox_versions.GetSelections()) == len(self.project.versions):
            self.btn_remove_versions.Disable()
        else:
            self.btn_remove_versions.Enable()
    
    def on_remove_selected(self, event):
        sel = self.listbox_versions.GetSelections()
        self.project.remove_versions(sel)
        self.populate_listbox(self.project.versions)
        self.toggle_remove_button()