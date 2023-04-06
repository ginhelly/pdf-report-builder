import wx
from pathlib import Path
from pdf_report_builder.ui.form_builder.main import BaseProjectPanel
from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.project.event_channel import EventChannel
from pdf_report_builder.ui.dialogs.error_message import ErrorDialog

class ProjectPanel(BaseProjectPanel):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        super().__init__(parent, id, pos, size, style, name)
        self.dp_default_save.GetPickerCtrl().SetLabel('Обзор...')

    def parse_project(self, project: ReportProject):
        self.project = project
        ver = project.get_current_version()
        self.dp_default_save.SetPath(str(ver.default_folder))
        self.text_code.SetValue(ver.code)
        self.text_current_version_name.SetValue(ver.name)
        self.handle_cb_availability()
        self.cb_relative_paths.SetValue(project.settings.paths_relative)

    def all_paths_are_relative(self):
        for ver in self.project.versions:
            default_folder = Path(ver.default_folder)
            for tome in ver.tomes:
                for el in tome.structural_elements:
                    for file in el.files:
                        if not file.path.is_relative_to(default_folder):
                            return False
        return True
    
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
            self.handle_cb_availability()
        except Exception:
            dlg = ErrorDialog(None, 'Не удалось установить путь', 'Неправильный путь')
            dlg.ShowModal()
            dlg.Close()
        
    def handle_cb_availability(self):
        if self.all_paths_are_relative():
            self.cb_relative_paths.Enable()
        else:
            self.project.settings.paths_relative = False
            self.cb_relative_paths.SetValue(False)
            self.cb_relative_paths.Disable()
    
    def toggle_relative_paths(self, event):
        val = self.cb_relative_paths.GetValue()
        self.project.settings.paths_relative = val
    
    def set_project_file_folder(self, event):
        folder = self.project.settings.savepath.parent
        self.project.get_current_version().default_folder = folder
        self.dp_default_save.SetPath(str(folder))