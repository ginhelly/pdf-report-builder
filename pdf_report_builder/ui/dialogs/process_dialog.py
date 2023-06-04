from pdf_report_builder.algorithms.merge import merge
from pdf_report_builder.project.base_project import BaseReportProject
from pdf_report_builder.ui.form_builder.main import BaseProcessingDialog
from pdf_report_builder.utils.logger import ProcessingLogger

class ProcessingDialog(BaseProcessingDialog):
    def __init__(self, parent, project: BaseReportProject):
        super().__init__(parent)
        self._project = project
        self._with_bookmarks = True
        self._break_on_missing = True
    
    def toggle_bookmarks(self, event):
        self._with_bookmarks = not self._with_bookmarks
    
    def toggle_break_on_missing(self, event):
        self._break_on_missing = not self._break_on_missing
    
    def process(self, event):
        self.logger = ProcessingLogger(self.text_logger, self.progress_bar)
        try:
            merge(
                self._project,
                logger=self.logger,
                break_on_missing=self._break_on_missing,
                with_bookmarks=self._with_bookmarks
            )
        except Exception as e:
            self.logger.writeline(f'Ошибка: {e}')
            self.logger.writeline(f'Выполнение программы прервано.')