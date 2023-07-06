import wx
from pathlib import Path
from pdf_report_builder.ui.form_builder.main import BaseProjectPanel
from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.project.event_channel import EventChannel
from pdf_report_builder.ui.dialogs.error_message import ErrorDialog

class ProjectPanel(BaseProjectPanel):

    def parse_project(self, project: ReportProject):
        self.project = project
        ver = project.get_current_version()
        self.text_code.SetValue(ver.code)
        self.text_current_version_name.SetValue(ver.name)
        self.handle_cb_availability()
        self.cb_relative_paths.SetValue(project.settings.paths_relative)
        self.text_savepath.SetValue(str(project.settings.savepath.parent))
        self.text_comments.SetValue(ver.comments)
    
    def on_version_name_change(self, event):
        new_value = self.text_current_version_name.GetValue()
        self.project.get_current_version().name = new_value
        EventChannel().publish('version_name_update')
        
    def on_code_change(self, event):
        new_value = self.text_code.GetValue()
        self.project.get_current_version().code = new_value
        EventChannel().publish('tree_update')
        
    def handle_cb_availability(self):
        if self.project.all_paths_are_relative():
            self.cb_relative_paths.Enable()
        else:
            self.project.settings.paths_relative = False
            self.cb_relative_paths.SetValue(False)
            self.cb_relative_paths.Disable()
    
    def toggle_relative_paths(self, event):
        val = self.cb_relative_paths.GetValue()
        self.project.settings.paths_relative = val
    
    def on_text_comments(self, event):
        val = self.text_comments.GetValue()
        self.project.get_current_version().comments = val
