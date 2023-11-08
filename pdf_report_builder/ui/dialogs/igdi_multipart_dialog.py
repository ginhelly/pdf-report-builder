import os
from pathlib import Path

from pdf_report_builder.ui.form_builder.main import BaseIGDIMultipartDialog
from pdf_report_builder.ui.dialogs.error_message import ErrorDialog
from pdf_report_builder.utils.app_settings import AppSettings

class IGDIMultipartDialog(BaseIGDIMultipartDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.fp_save_location.GetPickerCtrl().SetLabel('Обзор...')
        self.fp_tome_contents_template.GetPickerCtrl().SetLabel('Обзор...')
        default_template = AppSettings.get('DATA_PATH') / 'computed_elements_templates' / 'tome_contents'
        self.fp_tome_contents_template.value = str(default_template)
        self.save_location = Path(os.path.expanduser('~/documents/ИГДИ.reportprj'))
        self.tome_contents_template = default_template
        self.n_tomes = 1
        self.max_km = 0
        self.taps = []
    
    def on_save_location_change(self, event):
        new_loc = Path(self.fp_save_location.GetPath())
        if not new_loc.parent.exists():
            dlg = ErrorDialog(None, 'Не удалось установить путь', 'Неправильный путь')
            dlg.ShowModal()
            dlg.Close()
            return
        folder = new_loc.parent / 'Сборка'
        print(folder, folder.exists())
        if folder.exists():
            dlg = ErrorDialog(None, 'Существующая папка "Сборка" будет переписана!', 'Примите меры по защите своих файлов')
            dlg.ShowModal()
            dlg.Close()
        self.save_location = new_loc
    
    def on_contents_template_change(self, event):
        file = Path(self.fp_tome_contents_template.GetPath())
        if not file.exists() and file.is_file():
            dlg = ErrorDialog(None, 'Файл шаблона не найден', 'Ошибка файла')
            dlg.ShowModal()
            dlg.Close()
        self.tome_contents_template = file
    
    def on_n_tomes_change(self, event):
        self.n_tomes = self.spin_n_tomes.GetValue()
    
    def on_max_km_change(self, event):
        self.max_km = self.spin_max_km.GetValue()
    
    def on_taps_enter(self, event):
        try:
            self.taps = self.text_taps.GetValue().split(',')
            for tap in self.taps:
                tap = tap.strip()
        except Exception:
            dlg = ErrorDialog(None, 'Не получилось распарсить названия отводов', 'Некорректный ввод')
            dlg.ShowModal()
            dlg.Close()
