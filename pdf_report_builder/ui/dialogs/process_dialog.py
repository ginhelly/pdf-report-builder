import subprocess

from pdf_report_builder.algorithms.merge import merge
from pdf_report_builder.project.base_project import BaseReportProject
from pdf_report_builder.ui.form_builder.main import BaseProcessingDialog
from pdf_report_builder.utils.logger import ProcessingLogger

class ProcessingDialog(BaseProcessingDialog):
    def __init__(self, parent, project: BaseReportProject):
        super().__init__(parent)
        self._project = project
        self._with_bookmarks = True
        self._enumerate = True
        self._break_on_missing = True
        ver = self._project.get_current_version()
        self.folders = set(tome.savepath.parent for tome in ver.tomes)
        if len(self.folders) > 1:
            self.btn_open_folders.SetLabel('Открыть выходные папки')
        else:
            self.btn_open_folders.SetLabel('Открыть выходную папку')
    
    def toggle_bookmarks(self, event):
        self._with_bookmarks = not self._with_bookmarks
    
    def toggle_enumerate(self, event):
        self._enumerate = not self._enumerate
    
    def toggle_break_on_missing(self, event):
        self._break_on_missing = not self._break_on_missing
    
    def open_folders(self, event):
        for folder in self.folders:
            subprocess.Popen(f'explorer "{folder}"')
    
    def process(self, event):
        self.logger = ProcessingLogger(self.text_logger, self.progress_bar)
        try:
            merge(
                self._project,
                logger=self.logger,
                break_on_missing=self._break_on_missing,
                with_bookmarks=self._with_bookmarks,
                enumerate=self._enumerate
            )
        except Exception as e:
            self.logger.writeline(f'Ошибка: {e}')
            self.logger.writeline(f'Выполнение программы прервано.')