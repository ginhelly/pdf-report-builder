import wx
from pathlib import Path
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.ui.form_builder.main import BaseTomePanel
from pdf_report_builder.ui.dialogs.error_message import ErrorDialog
from pdf_report_builder.project.storage import ProjectStorage
from pdf_report_builder.project.event_channel import EventChannel

class TomePanel(BaseTomePanel):
    def __init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.TAB_TRAVERSAL, name=wx.EmptyString):
        super().__init__(parent, id, pos, size, style, name)
        self.fp_save.GetPickerCtrl().SetLabel('Обзор...')

    def parse_tome(self, tome: Tome):
        self.tome = tome
        self.text_tome_code.SetValue(tome.basename)
        self.text_tome_name.SetValue(tome.human_readable_name)
        self.cb_use_custom_enumeration_start.SetValue(tome.use_custom_enumeration_start)
        self.spin_custom_enumeration_start.SetValue(tome.custom_enumeration_start)
        if tome.use_custom_enumeration_start:
            self.spin_custom_enumeration_start.Enable()
        else:
            self.spin_custom_enumeration_start.Disable()
        self.fp_save.SetPath(str(tome.savepath))
        prefix = ProjectStorage().project.get_current_version().code
        if len(prefix) > 20:
            prefix = f'...{prefix[-19:]}'
        self.lbl_prefix.SetLabelText(prefix)
        
    def on_save_file_change(self, event):
        try:
            path = Path(self.fp_save.GetPath())
            assert path.parent.exists()
            self.tome.savepath = path
        except Exception:
            dlg = ErrorDialog(None, 'Не удалось установить путь', 'Неправильный путь')
            dlg.ShowModal()
            dlg.Close()
    
    def on_move_to_default_folder(self, event):
        default_folder = Path(ProjectStorage().project.settings.savepath.parent)
        assert default_folder.exists() and default_folder.is_dir()
        self.tome.savepath = default_folder / self.tome.savepath.name
        self.fp_save.SetPath(str(self.tome.savepath))
    
    def on_tome_code_change(self, event):
        new_value = self.text_tome_code.GetValue()
        self.tome.basename = new_value
        EventChannel().publish('tree_update')
    
    def on_tome_name_change(self, event):
        new_value = self.text_tome_name.GetValue()
        self.tome.human_readable_name = new_value
        EventChannel().publish('tome_name_update')
    
    def toggle_use_custom_enum_start(self, event):
        val = self.cb_use_custom_enumeration_start.GetValue()
        self.tome.use_custom_enumeration_start = val
        if val:
            self.spin_custom_enumeration_start.Enable()
        else:
            self.spin_custom_enumeration_start.Disable()
    
    def on_custom_enum_start_update(self, event):
        val = int(self.spin_custom_enumeration_start.GetValue())
        self.tome.custom_enumeration_start = val