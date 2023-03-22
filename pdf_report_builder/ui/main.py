import wx
import sys
import traceback
from pathlib import Path

from pdf_report_builder.ui.form_builder.main import MainFrame
from pdf_report_builder.ui.about import PRBAboutDialog
from pdf_report_builder.utils.docs import open_docs
from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.ui.tree import Tree

def on_exception(exception_type, text: str = ""):
    msg = text or "Произошла ошибка.\n\n"
    dlg=wx.MessageDialog(
        None, 
        msg, 
        str(exception_type), 
        wx.OK|wx.ICON_ERROR
    )
    dlg.ShowModal()
    dlg.Destroy()

class PDFReportBuilderFrame(MainFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_new_project()
        self.tree_component = Tree(self.tree, self.project)
    
    def onExit(self, event):
        if self.project.modified:
            if wx.MessageBox(
                "Всё равно закрыть?",
                "Проект был изменен",
                wx.ICON_WARNING | wx.YES_NO
            ) != wx.YES:
                if isinstance(event, wx.CloseEvent) and event.CanVeto():
                    event.Veto()
                return
        self.project.close()
        self.Destroy()
    
    def onAbout(self, event):
        about = PRBAboutDialog(self)
        about.ShowModal()
        about.Destroy()
    
    def onDocsOpen101(self, event):
        open_docs('GOST101')
    
    def onDocsOpen105(self, event):
        open_docs('GOST105')
    
    def onDocsOpen301(self, event):
        open_docs('GOST301')
    
    def onDocsOpen47(self, event):
        open_docs('SP47')
    
    def onDocsOpen317(self, event):
        open_docs('SP317')
    
    def previous_project_willing_to_close(self):
        if self.project.modified:
            if wx.MessageBox(
                "Отменить изменения?",
                "Проект был изменен",
                wx.ICON_WARNING | wx.YES_NO
            ) != wx.YES:
                return False
        return True
    
    def create_new_project(self, event = None):
        if hasattr(self, 'project'):
            if not self.previous_project_willing_to_close():
                return
            self.project.close()
        self.project = ReportProject()
        self.lbl_project_name.SetLabelText(self.project.settings.name)
        self.populate_choice_current_version()
        if hasattr(self, 'tree_component'):
            self.tree_component.redraw_tree(self.project)
    
    def open_project(self, event):
        if hasattr(self, 'project'):
            if not self.previous_project_willing_to_close():
                return
            self.project.close()
        with wx.FileDialog(
            self,
            "Открыть файл проекта",
            wildcard="Файлы PDF Report Builder (.reportprj)|*.reportprj",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        ) as open_dialog:
            if open_dialog.ShowModal() == wx.ID_CANCEL:
                return
            path = Path(open_dialog.GetPath())
            try:
                self.project = ReportProject.open(path)
            except Exception as e:
                on_exception(str(type(e)), 'Не удалось прочитать файл проекта')
                return
            self.lbl_project_name.SetLabelText(self.project.settings.name)
            self.populate_choice_current_version()
            self.tree_component.redraw_tree(self.project)
        
    def save_project(self, event):
        try:
            self.project.save()
        except Exception as e:
            on_exception(type(e), 'Не удалось сохранить проект')
        
    def save_project_as(self, event):
        with wx.FileDialog(
            self,
            "Сохранить как",
            wildcard="Файлы PDF Report Builder (.reportprj)|*.reportprj",
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
        ) as save_dialog:
            if save_dialog.ShowModal() == wx.ID_CANCEL:
                return
            path = Path(save_dialog.GetPath())

            try:
                self.project.save_as(path)
            except Exception as e:
                on_exception(str(type(e)), 'Не удалось сохранить проект')
    
    def populate_choice_current_version(self):
        choice = self.choice_current_version
        choice.Clear()
        for version in self.project.versions:
            choice.Append(version.name)
        choice.SetSelection(self.project.settings.current_version_id)
    
    def create_new_version(self, event):
        with wx.TextEntryDialog(
            self,
            "Название новой версии"
        ) as dlg:
            if dlg.ShowModal() == wx.ID_CANCEL:
                return
            self.project.create_new_version(dlg.GetValue())
            self.populate_choice_current_version()
    
    def set_current_version(self, event):
        new_ver_id = self.choice_current_version.GetCurrentSelection()
        self.project.set_current_version_id(new_ver_id)
        self.tree_component.redraw_tree(self.project)

    def clone_current_version(self, event):
        with wx.TextEntryDialog(
            self,
            "Название новой версии"
        ) as dlg:
            if dlg.ShowModal() == wx.ID_CANCEL:
                return
            self.project.clone_current_version(dlg.GetValue())
            self.populate_choice_current_version()