import csv
import wx

from pdf_report_builder.ui.form_builder.main import BaseCalculatorDialog
from pdf_report_builder.paperformats.format import PaperFormatStorage

def format_number(num):
    if num - int(num) > 0.1:
        return num
    return int(num)

class CalculatorDialog(BaseCalculatorDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_blocks.AutoSizeColumns()
        self._set_choice_editor()
        self.add_row()
    
    def OnCellRightClick(self, event):
        col = event.GetCol()
        
        menu = wx.Menu()
        menu.Append(wx.ID_ADD, "Добавить строку")
        self.Bind(wx.EVT_MENU, self.add_row, id=wx.ID_ADD)

        if self.grid_blocks.GetNumberRows() > 1 and len(self.grid_blocks.GetSelectedRows()) > 0:
            menu.Append(wx.ID_REMOVE, "Удалить")
            self.Bind(wx.EVT_MENU, self.OnRemoveRow, id=wx.ID_REMOVE)
        
        # Show the context menu
        self.PopupMenu(menu)
        menu.Destroy()
    
    def OnRemoveRow(self, event=None):
        rows = self.grid_blocks.GetSelectedRows()
        count = 0
        for row in rows:
            to_die = self.grid_blocks.GetCellEditor(row - count, 1)
            to_die.Destroy()
            to_die = self.grid_blocks.GetCellEditor(row - count, 2)
            to_die.Destroy()
            self.grid_blocks.DeleteRows(row - count)
            count = count + 1
        self.count_total()
        self.update_list_sheets()
    
    def on_close(self, event):
        for i in range(self.grid_blocks.GetNumberRows()):
            to_die = self.grid_blocks.GetCellEditor(i, 1)
            to_die.Destroy()
            to_die = self.grid_blocks.GetCellEditor(i, 2)
            to_die.Destroy()
        self.Close()
    
    def _set_choice_editor(self):
        P = PaperFormatStorage()
        choices = list(P._formats_dict.keys())
        self.formats = P._formats_dict
        self.choice_editor = wx.grid.GridCellChoiceEditor(choices)
        self.number_editor = wx.grid.GridCellNumberEditor()
    
    def add_row(self, event=None, contents=None):
        self.grid_blocks.AppendRows(1)
        n = self.grid_blocks.GetNumberRows()
        self.grid_blocks.SetCellEditor(n - 1, 1, self.choice_editor)
        self.grid_blocks.SetCellEditor(n - 1, 2, self.number_editor)
        if not (contents is None):
            self.grid_blocks.SetCellValue(n - 1, 0, contents[0])
            self.grid_blocks.SetCellValue(n - 1, 1, contents[1])
            self.grid_blocks.SetCellValue(n - 1, 2, contents[2])
            self.grid_blocks.SetCellValue(n - 1, 3, contents[3])
        else:
            self.grid_blocks.SetCellValue(n - 1, 2, '1')
        self.grid_blocks.SetReadOnly(n - 1, 3, True)
        self.count_total()
        self.update_list_sheets()
    
    def get_paper_format_a4(self, row):
        paper_format_name = self.grid_blocks.GetCellValue(row, 1)
        if not paper_format_name in self.formats:
            return 0
        return self.formats[paper_format_name].multiple_of_a4
    
    def grid_updated(self, event):
        self.grid_blocks.AutoSizeColumns()
        if event.GetCol() == 0:
            self.update_list_sheets()
            return
        self.count_total()
        row = event.GetRow()
        paper_format_a4 = self.get_paper_format_a4(row)
        multiply_by = int(self.grid_blocks.GetCellValue(row, 2))
        self.grid_blocks.SetCellValue(row, 3, str(format_number(paper_format_a4 * multiply_by)))
        self.grid_blocks.ForceRefresh()
        self.update_list_sheets()
    
    def count_total(self):
        sum_native = 0
        sum_a4 = 0
        for i in range(self.grid_blocks.GetNumberRows()):
            sum_native = sum_native + int(self.grid_blocks.GetCellValue(i, 2))
            paper_format_a4 = self.get_paper_format_a4(i)
            sum_a4 = sum_a4 + paper_format_a4 * int(self.grid_blocks.GetCellValue(i, 2))
        self.lbl_itogo.SetLabelText(
            f'{format_number(sum_native)} листов; {format_number(sum_a4)} эквивалентно формату A4'
        )
        self.lbl_selection.SetLabelText('0 листов; 0 эквивалентно формату A4')
    
    def update_list_sheets(self):
        self.list_sheets.Clear()
        for i in range(self.grid_blocks.GetNumberRows()):
            name = self.grid_blocks.GetCellValue(i, 0)
            if len(name) > 50:
                name = name[:50] + '...'
            paper_format_a4 = self.get_paper_format_a4(i)
            native_sheets = int(self.grid_blocks.GetCellValue(i, 2))
            list_items = [
                (f'({format_number(paper_format_a4)}*A4) {name}#{j+1}', paper_format_a4)
                for j in range(native_sheets)
            ]
            for item in list_items:
                self.list_sheets.Append(*item)
    
    def on_listbox_selection(self, event):
        selections = self.list_sheets.GetSelections()
        sum_native = len(selections)
        sum_a4 = 0
        for i in selections:
            paper_format_a4 = self.list_sheets.GetClientData(i)
            sum_a4 = sum_a4 + paper_format_a4
        self.lbl_selection.SetLabelText(
            f'{format_number(sum_native)} листов; {format_number(sum_a4)} эквивалентно формату A4'
        )
    
    def on_save(self, event):
        dlg = wx.FileDialog(
            self, message="Сохранить как", wildcard="CSV files (*.csv)|*.csv", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        )
        if dlg.ShowModal() == wx.ID_CANCEL:
            return
        filepath = dlg.GetPath()

        with open(filepath, 'w+', newline='') as csvfile:
            writer = csv.writer(csvfile)

            for row in range(self.grid_blocks.GetNumberRows()):
                row_data = []
                for col in range(self.grid_blocks.GetNumberCols()):
                    cell_value = self.grid_blocks.GetCellValue(row, col)
                    row_data.append(cell_value)
                writer.writerow(row_data)
        
    
    def on_load(self, event):
        dlg = wx.FileDialog(
            None,
            message="Открыть CSV-файл калькулятора",
            wildcard="CSV files (*.csv)|*.csv",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        )
        if dlg.ShowModal() == wx.ID_CANCEL:
            return
        filepath = dlg.GetPath()
        with open(filepath, 'r') as csvfile:
            reader = csv.reader(csvfile)
            rows = []
            for row in reader:
                rows.append(row)
        self.grid_blocks.ClearGrid()
        for i in range(self.grid_blocks.GetNumberRows()):
            self.grid_blocks.SelectRow(i, True)
        self.OnRemoveRow()

        for i in range(len(rows)):
            self.add_row(contents=rows[i])