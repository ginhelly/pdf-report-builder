from pdf_report_builder.ui.form_builder.main import AboutDialog

class PRBAboutDialog(AboutDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.rt_about.Clear()
        self.rt_about.BeginBold()
        self.rt_about.WriteText('PDF Report Builder')
        self.rt_about.EndBold()
        self.rt_about.WriteText(' – программа для формирования техотчетов')
        self.rt_about.AddParagraph('E-mail: ')
        self.rt_about.MoveEnd()
        self.rt_about.BeginURL('mailto:info@gkurg.ru')
        self.rt_about.WriteText('info@gkurg.ru')
        self.rt_about.EndURL()