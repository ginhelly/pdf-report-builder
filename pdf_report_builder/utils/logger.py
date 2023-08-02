from wx import TextCtrl
from wx import Gauge

class ProcessingLogger:

    def __init__(
        self,
        text_logger: TextCtrl,
        progress_bar: Gauge,
        size_limit: int = 100,
        delta: int = 1,
        fraction: int = 1
    ):
        self.text_logger = text_logger
        self.progress_bar = progress_bar
        self.size_limit = size_limit
        self.delta = delta
        self.fraction = fraction
        self._times_fraction_added = 0
        self.clear()
    
    def set_delta(self, delta: int):
        self.delta = delta
        self._times_fraction_added = 0
    
    def set_fraction(self, fraction: int):
        if self._times_fraction_added > 0:
            self.delta = self.delta - self.fraction * self._times_fraction_added
        self.fraction = fraction
        self._times_fraction_added = 0
    
    def add_delta(self):
        self.add_to_progress_bar(self.delta)
    
    def add_fraction(self):
        self.add_to_progress_bar(int(self.delta / self.fraction))
        self._times_fraction_added += 1

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