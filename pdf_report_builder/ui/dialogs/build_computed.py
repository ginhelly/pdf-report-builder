from typing import List

import wx

from pdf_report_builder.ui.form_builder.main import BaseBuildComputedDialog
from pdf_report_builder.structure.structural_elements.computed import ComputedElement
from pdf_report_builder.algorithms.collect_computed import collect_computed
from pdf_report_builder.utils.logger import ProcessingLogger
from pdf_report_builder.project.event_channel import EventChannel

class BuildComputedDialog(BaseBuildComputedDialog):
    def __init__(self, parent, elements: List[ComputedElement] | None = None):
        super().__init__(parent)
        if elements is None:
            self.computed = collect_computed()
        else:
            self.computed = elements
        self.populate_checklistbox()
        self.logger = ProcessingLogger(self.text_logs, self.m_gauge2)
        if len(self.computed) == 0:
            self.btn_process.Disable()
        self.on_select_all()
    
    def populate_checklistbox(self):
        self.cl_computed.Clear()
        for el in self.computed:
            el_name = f'{el.name} | Том: {el.tome.human_readable_name}'
            self.cl_computed.Append(el_name, el)
    
    def on_select_all(self, event = None):
        for i in range(self.cl_computed.Count):
            self.cl_computed.Check(i, True)

    def on_deselect_all(self, event):
        for i in range(self.cl_computed.Count):
            self.cl_computed.Check(i, False)

    def on_process(self, event):
        self.logger.clear()
        to_process = []
        for i in self.cl_computed.GetCheckedItems():
            to_process.append(self.cl_computed.GetClientData(i))
        
        self.logger.set_delta(int(100 / len(to_process)))
        errors = []
        for el in to_process:
            self.logger.writeline(f'Обрабатываю {el.name} | Том {el.tome.human_readable_name}')
            try:
                el.make_pdf(self.logger)
            except Exception as e:
                self.logger.writeline(' Ошибка! Не получилось сформировать PDF')
                self.logger.writeline(f' {e}')
                errors.append(el)
            self.logger.writeline('')
        
        self.logger.writeline('Обработка закончена.')
        if len(errors) > 0:
            self.logger.writeline('Не получилось обработать следующие элементы:')
            for el in errors:
                self.logger.writeline(f'- {el.name} | Том {el.tome.human_readable_name}')
            self.logger.writeline('Проверьте их настройки')
        else:
            self.logger.set_progress_bar(100)
        EventChannel().publish('modified')
        EventChannel().publish('tree_update')
        
    def on_close(self, event):
        self.Destroy()
    