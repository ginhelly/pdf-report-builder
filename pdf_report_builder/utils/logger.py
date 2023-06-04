from wx import TextCtrl
from wx import Gauge

class ProcessingLogger:

    def __init__(
        self,
        text_logger: TextCtrl,
        progress_bar: Gauge,
        size_limit: int = 100
    ):
        self.text_logger = text_logger
        self.progress_bar = progress_bar
        self.size_limit = size_limit
        self.clear()

    def writeline(self, message: str):
        if self.text_logger.NumberOfLines > self.size_limit:
            self.clear()
        self.text_logger.write(message + '\n')
    
    def set_progress_bar(self, value: int):
        if value < 0 or value > self.progress_bar.GetRange():
            return
        self.progress_bar.SetValue(value)
    
    def add_to_progress_bar(self, value: int):
        new_total = self.progress_bar.GetValue() + value
        self.set_progress_bar(new_total)
    
    def clear(self):
        self.text_logger.Clear()
        self.progress_bar.SetValue(0)