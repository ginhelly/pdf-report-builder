from pathlib import Path

import wx

from pdf_report_builder.algorithms.merge import merge
from pdf_report_builder.project.project import ReportProject
from pdf_report_builder.ui.about import PRBAboutDialog
from pdf_report_builder.ui.dialogs.error_message import ErrorDialog
from pdf_report_builder.ui.dialogs.remove_versions_dialog import \
    RemoveVersionsDialog
from pdf_report_builder.ui.form_builder.main import MainFrame
from pdf_report_builder.ui.tree.tree import Tree
from pdf_report_builder.ui.panels.book import Book
from pdf_report_builder.utils.docs import open_docs
from pdf_report_builder.project.event_channel import EventChannel
from pdf_report_builder.project.storage import ProjectStorage


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
        ProjectStorage().set_project(self.project)
        self.tree_component = Tree(self.tree_container, self.project)
        self.tree_container.GetSizer().Add(self.tree_component, 1, wx.ALL|wx.EXPAND)
        self.tree_component.Bind(wx.EVT_TREE_SEL_CHANGED, self.on_tree_sel_changed)
        self.book = Book(
            self.properties_panel,
            style=wx.EXPAND
        )
        sizer = self.properties_panel.GetSizer()
        sizer.Add(self.book, 1, wx.EXPAND)
        self.book.parse_item(self.project)
        self.populate_choice_current_version()
        EventChannel().subscribe('version_name_update', self.populate_choice_current_version)
        EventChannel().subscribe('project_changed', self.on_project_change)
        #self.tree_component.Bind(wx.EVT_TREE_BEGIN_DRAG, self.)
    
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
        EventChannel().publish('project_changed', self.project)
    
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
                print(e)
                on_exception(str(type(e)), 'Не удалось прочитать файл проекта')
                return
            EventChannel().publish('project_changed', self.project)
    
    def on_project_change(self, payload):
        project = payload[0]
        self.lbl_project_name.SetLabelText(project.settings.name)
        self.populate_choice_current_version()
        if hasattr(self, 'tree_component'):
            self.tree_component.redraw_tree(project)
        self.book.parse_item(project)
        
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
            self.tree_component.redraw_tree(self.project)
            self.book.parse_item(self.project)
    
    def set_current_version(self, event):
        new_ver_id = self.choice_current_version.GetCurrentSelection()
        self.project.set_current_version_id(new_ver_id)
        self.tree_component.redraw_tree(self.project)
        self.book.parse_item(self.project)

    def clone_current_version(self, event):
        with wx.TextEntryDialog(
            self,
            "Название новой версии"
        ) as dlg:
            if dlg.ShowModal() == wx.ID_CANCEL:
                return
            self.project.clone_current_version(dlg.GetValue())
            self.populate_choice_current_version()
            self.tree_component.redraw_tree(self.project)
            self.book.parse_item(self.project)
    
    def on_project_name_change(self, event):
        with wx.TextEntryDialog(
            self,
            "Новое название проекта"
        ) as dlg:
            dlg.SetValue(self.project.settings.name)
            if dlg.ShowModal() == wx.ID_CANCEL:
                return
            self.project.settings.name = dlg.GetValue()
            self.lbl_project_name.SetLabelText(self.project.settings.name)
    
    def on_remove_versions(self, event):
       dlg = RemoveVersionsDialog(None, self.project)
       dlg.ShowModal()
       dlg.Destroy()
       self.populate_choice_current_version()
       self.tree_component.redraw_tree(self.project)
    
    def on_tree_sel_changed(self, event):
        self.toggle_up_down_buttons(event)
        item = self.tree_component.nodes[event.Item].item
        self.book.parse_item(item)
    
    def toggle_up_down_buttons(self, event):
        self._toggle_button(event, self.btn_up, 0)
        self._toggle_button(event, self.btn_down, -1)
    
    def _toggle_button(self, event, btn, i):
        tree_node = self.tree_component.nodes[event.Item]
        if tree_node.parent is None:
            btn.Disable()
            return
        if tree_node.parent.children[i] == tree_node:
            btn.Disable()
            return
        btn.Enable()
    
    def on_up(self, event):
        item_id = self.tree_component.GetSelection()
        node1 = self.tree_component.nodes[item_id]
        node2 = node1.prev
        self.tree_component.swap(node1, node2)
        self.tree_component.SelectItem(
            node1.item_id
        )

    def on_down(self, event):
        item_id = self.tree_component.GetSelection()
        node1 = self.tree_component.nodes[item_id]
        node2 = node1.next
        self.tree_component.swap(node1, node2)
        self.tree_component.SelectItem(
            node1.item_id
        )
        
    def make_reports(self, event):
        try:
            merge(self.project)
            dlg = wx.MessageDialog(
                None,
                'Успешно сформировано!',
                'Успех!',
                wx.OK | wx.ICON_EXCLAMATION
            )
            dlg.ShowModal()
            dlg.Destroy()
        except Exception as e:
            dlg = ErrorDialog(None, str(e))
            dlg.ShowModal()
            dlg.Destroy()