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
        self.dp_default_save.SetPath(str(ver.default_folder))
        self.text_code.SetValue(ver.code)
        self.text_current_version_name.SetValue(ver.name)
    
    def on_version_name_change(self, event):
        new_value = self.text_current_version_name.GetValue()
        self.project.get_current_version().name = new_value
        EventChannel().publish('version_name_update')
        
    def on_code_change(self, event):
        new_value = self.text_code.GetValue()
        self.project.get_current_version().code = new_value
        EventChannel().publish('tree_update')
    
    def on_default_dir_change(self, event):
        try:
            path = Path(self.dp_default_save.GetPath())
            assert path.exists() and path.is_dir()
            self.project.get_current_version().default_folder = path
        except Exception:
            dlg = ErrorDialog(None, 'Не удалось установить путь', 'Неправильный путь')
            dlg.ShowModal()
            dlg.Close()