import subprocess

import wx

from pdf_report_builder.algorithms.merge import merge, MergeTask
from pdf_report_builder.algorithms.parse_pages_count import ParseReportNode, parse_project_for_pages
from pdf_report_builder.project.base_project import BaseReportProject
from pdf_report_builder.structure.tome import Tome
from pdf_report_builder.ui.form_builder.main import BaseProcessingDialog
from pdf_report_builder.utils.logger import ProcessingLogger

class ProcessingDialog(BaseProcessingDialog):
    def __init__(self, parent, project: BaseReportProject):
        super().__init__(parent)
        self._project = project
        self._with_bookmarks = True
        self._enumerate = True
        self._break_on_missing = True
        self._parse_project_root_node = parse_project_for_pages(project)
        self.populate_tomes_select()
        ver = self._project.get_current_version()
        self.folders = set(tome.savepath.parent for tome in ver.tomes)
        if len(self.folders) > 1:
            self.btn_open_folders.SetLabel('Открыть выходные папки')
        else:
            self.btn_open_folders.SetLabel('Открыть выходную папку')
    
    def populate_tomes_select(self):
        self.treelist_tomes.SetColumnWidth(0, 300)
        ver = self._project.get_current_version()
        for node, tome in zip(self._parse_project_root_node.children, ver.tomes):
            self._add_treelist_item(node, tome)

    def _add_treelist_item(self, node: ParseReportNode, tome: Tome):
        root_item = self.treelist_tomes.GetRootItem()
        new_item = self.treelist_tomes.AppendItem(root_item, node.name, data=tome)
        enumeration_start = node.current_page_number \
            if not tome.use_custom_enumeration_start \
            else tome.custom_enumeration_start
        self.treelist_tomes.SetItemText(new_item, 1, str(enumeration_start))
        self.treelist_tomes.CheckItem(new_item)
    
    def on_select_all_tomes(self, event):
        root_item = self.treelist_tomes.GetRootItem()
        self.treelist_tomes.CheckItemRecursively(root_item, wx.CHK_CHECKED)

    def on_deselect_all_tomes(self, event):
        root_item = self.treelist_tomes.GetRootItem()
        self.treelist_tomes.CheckItemRecursively(root_item, wx.CHK_UNCHECKED)
    
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
        def make_task(item):
            tome = self.treelist_tomes.GetItemData(item)
            start = int(self.treelist_tomes.GetItemText(item, 1))
            return MergeTask(tome, start)
        
        tasks = []
        item = self.treelist_tomes.GetFirstItem()
        if self.treelist_tomes.GetCheckedState(item) == wx.CHK_CHECKED:
            tasks.append(make_task(item))
        while True:
            item = self.treelist_tomes.GetNextItem(item)
            if not item.IsOk():
                break
            if self.treelist_tomes.GetCheckedState(item) == wx.CHK_CHECKED:
                tasks.append(make_task(item))

        self.logger = ProcessingLogger(self.text_logger, self.progress_bar)
        try:
            merge(
                tasks,
                self._project.get_current_version().name,
                logger=self.logger,
                break_on_missing=self._break_on_missing,
                with_bookmarks=self._with_bookmarks,
                enumerate=self._enumerate
            )
        except Exception as e:
            self.logger.writeline(f'Ошибка: {e}')
            self.logger.writeline(f'Выполнение программы прервано.')