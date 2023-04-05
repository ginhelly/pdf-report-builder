# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PDF Report Builder", pos = wx.DefaultPosition, size = wx.Size( 900,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 500,450 ), wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.menu_project = wx.Menu()
        self.menu_project_new = wx.MenuItem( self.menu_project, wx.ID_ANY, u"Новый проект\tCtrl+N", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_project.Append( self.menu_project_new )

        self.menu_open_template = wx.Menu()
        self.menu_project.AppendSubMenu( self.menu_open_template, u"Открыть из шаблона" )

        self.menu_project_open = wx.MenuItem( self.menu_project, wx.ID_ANY, u"Открыть проект...\tCtrl+O", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_project_open.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_MENU ) )
        self.menu_project.Append( self.menu_project_open )

        self.menu_project.AppendSeparator()

        self.menu_project_save = wx.MenuItem( self.menu_project, wx.ID_ANY, u"Сохранить проект\tCtrl+S", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_project_save.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_MENU ) )
        self.menu_project.Append( self.menu_project_save )

        self.menu_project_save_as = wx.MenuItem( self.menu_project, wx.ID_ANY, u"Сохранить как...\tCtrl+Shift+S", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_project_save_as.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE_AS, wx.ART_MENU ) )
        self.menu_project.Append( self.menu_project_save_as )

        self.menu_project.AppendSeparator()

        self.m_close = wx.MenuItem( self.menu_project, wx.ID_ANY, u"Выход из программы"+ u"\t" + u"Ctrl+Q", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_close.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_QUIT, wx.ART_MENU ) )
        self.menu_project.Append( self.m_close )

        self.m_menubar1.Append( self.menu_project, u"&Проект" )

        self.menu_versions = wx.Menu()
        self.menu_versions_new = wx.MenuItem( self.menu_versions, wx.ID_ANY, u"Новая версия", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_versions.Append( self.menu_versions_new )

        self.m_menuItem18 = wx.MenuItem( self.menu_versions, wx.ID_ANY, u"Клонировать текущую", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_versions.Append( self.m_menuItem18 )

        self.menu_versions.AppendSeparator()

        self.m_menuItem19 = wx.MenuItem( self.menu_versions, wx.ID_ANY, u"Удалить...", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_versions.Append( self.m_menuItem19 )

        self.m_menubar1.Append( self.menu_versions, u"&Версии" )

        self.menu_about = wx.Menu()
        self.menu_about_about = wx.MenuItem( self.menu_about, wx.ID_ANY, u"О программе", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_about_about.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_HELP_PAGE, wx.ART_MENU ) )
        self.menu_about.Append( self.menu_about_about )

        self.menu_about.AppendSeparator()

        self.m_menu1 = wx.Menu()
        self.menu_about_gost101 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"ГОСТ Р 21.101–2020", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.menu_about_gost101 )

        self.menu_about_gost301 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"ГОСТ Р 21.301–2021", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.menu_about_gost301 )

        self.menu_about_gost105 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"ГОСТ Р 2.105–2019", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.menu_about_gost105 )

        self.m_menu1.AppendSeparator()

        self.menu_about_sp47 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"СП 47.13330.2016", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.menu_about_sp47 )

        self.menu_about_sp317 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"СП 317.1325800.2017", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu1.Append( self.menu_about_sp317 )

        self.menu_about.AppendSubMenu( self.m_menu1, u"Нормативная документация" )

        self.m_menubar1.Append( self.menu_about, u"&Справка" )

        self.SetMenuBar( self.m_menubar1 )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.lbl_project_name = wx.StaticText( self, wx.ID_ANY, u"Название проекта", wx.DefaultPosition, wx.DefaultSize, wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
        self.lbl_project_name.SetLabelMarkup( u"Название проекта" )
        self.lbl_project_name.Wrap( -1 )

        self.lbl_project_name.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer4.Add( self.lbl_project_name, 1, wx.ALIGN_CENTER|wx.LEFT, 5 )

        self.btn_open_project_settings = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

        self.btn_open_project_settings.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_EDIT, wx.ART_BUTTON ) )
        bSizer4.Add( self.btn_open_project_settings, 0, wx.ALL, 5 )


        bSizer2.Add( bSizer4, 0, wx.EXPAND, 5 )

        bSizer20 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        bSizer3.SetMinSize( wx.Size( 250,-1 ) )
        bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer21.SetMinSize( wx.Size( -1,33 ) )
        self.lbl_version1 = wx.StaticText( self, wx.ID_ANY, u"Свойства", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_version1.Wrap( -1 )

        self.lbl_version1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer21.Add( self.lbl_version1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer3.Add( bSizer21, 0, wx.EXPAND, 5 )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer3.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        self.properties_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer18 = wx.BoxSizer( wx.VERTICAL )


        self.properties_panel.SetSizer( bSizer18 )
        self.properties_panel.Layout()
        bSizer18.Fit( self.properties_panel )
        bSizer3.Add( self.properties_panel, 1, wx.EXPAND |wx.ALL, 5 )

        self.btn_merge = wx.Button( self, wx.ID_ANY, u"Сформировать отчеты!", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.btn_merge, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer20.Add( bSizer3, 1, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        bSizer6.SetMinSize( wx.Size( 300,-1 ) )
        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.lbl_version = wx.StaticText( self, wx.ID_ANY, u"Текущая версия:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_version.Wrap( -1 )

        self.lbl_version.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer5.Add( self.lbl_version, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        choice_current_versionChoices = []
        self.choice_current_version = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_current_versionChoices, 0 )
        self.choice_current_version.SetSelection( 0 )
        bSizer5.Add( self.choice_current_version, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.btn_clone_version = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

        self.btn_clone_version.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_COPY, wx.ART_BUTTON ) )
        self.btn_clone_version.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )

        bSizer5.Add( self.btn_clone_version, 0, wx.ALL, 5 )


        bSizer13.Add( bSizer5, 2, wx.EXPAND, 5 )


        bSizer13.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_up = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

        self.btn_up.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_UP, wx.ART_BUTTON ) )
        self.btn_up.Enable( False )

        bSizer13.Add( self.btn_up, 0, wx.ALL, 5 )

        self.btn_down = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

        self.btn_down.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_DOWN, wx.ART_BUTTON ) )
        self.btn_down.Enable( False )

        bSizer13.Add( self.btn_down, 0, wx.ALL, 5 )


        bSizer6.Add( bSizer13, 0, wx.EXPAND, 5 )

        self.tree_container = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        tree_sizer = wx.BoxSizer( wx.VERTICAL )


        self.tree_container.SetSizer( tree_sizer )
        self.tree_container.Layout()
        tree_sizer.Fit( self.tree_container )
        bSizer6.Add( self.tree_container, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer20.Add( bSizer6, 2, wx.EXPAND, 5 )


        bSizer2.Add( bSizer20, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.onExit )
        self.Bind( wx.EVT_MENU, self.create_new_project, id = self.menu_project_new.GetId() )
        self.Bind( wx.EVT_MENU, self.open_project, id = self.menu_project_open.GetId() )
        self.Bind( wx.EVT_MENU, self.save_project, id = self.menu_project_save.GetId() )
        self.Bind( wx.EVT_MENU, self.save_project_as, id = self.menu_project_save_as.GetId() )
        self.Bind( wx.EVT_MENU, self.onExit, id = self.m_close.GetId() )
        self.Bind( wx.EVT_MENU, self.create_new_version, id = self.menu_versions_new.GetId() )
        self.Bind( wx.EVT_MENU, self.clone_current_version, id = self.m_menuItem18.GetId() )
        self.Bind( wx.EVT_MENU, self.on_remove_versions, id = self.m_menuItem19.GetId() )
        self.Bind( wx.EVT_MENU, self.onAbout, id = self.menu_about_about.GetId() )
        self.Bind( wx.EVT_MENU, self.onDocsOpen101, id = self.menu_about_gost101.GetId() )
        self.Bind( wx.EVT_MENU, self.onDocsOpen301, id = self.menu_about_gost301.GetId() )
        self.Bind( wx.EVT_MENU, self.onDocsOpen105, id = self.menu_about_gost105.GetId() )
        self.Bind( wx.EVT_MENU, self.onDocsOpen47, id = self.menu_about_sp47.GetId() )
        self.Bind( wx.EVT_MENU, self.onDocsOpen317, id = self.menu_about_sp317.GetId() )
        self.btn_open_project_settings.Bind( wx.EVT_BUTTON, self.on_project_name_change )
        self.btn_merge.Bind( wx.EVT_BUTTON, self.make_reports )
        self.choice_current_version.Bind( wx.EVT_CHOICE, self.set_current_version )
        self.btn_clone_version.Bind( wx.EVT_BUTTON, self.clone_current_version )
        self.btn_up.Bind( wx.EVT_BUTTON, self.on_up )
        self.btn_down.Bind( wx.EVT_BUTTON, self.on_down )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onExit( self, event ):
        event.Skip()

    def create_new_project( self, event ):
        event.Skip()

    def open_project( self, event ):
        event.Skip()

    def save_project( self, event ):
        event.Skip()

    def save_project_as( self, event ):
        event.Skip()


    def create_new_version( self, event ):
        event.Skip()

    def clone_current_version( self, event ):
        event.Skip()

    def on_remove_versions( self, event ):
        event.Skip()

    def onAbout( self, event ):
        event.Skip()

    def onDocsOpen101( self, event ):
        event.Skip()

    def onDocsOpen301( self, event ):
        event.Skip()

    def onDocsOpen105( self, event ):
        event.Skip()

    def onDocsOpen47( self, event ):
        event.Skip()

    def onDocsOpen317( self, event ):
        event.Skip()

    def on_project_name_change( self, event ):
        event.Skip()

    def make_reports( self, event ):
        event.Skip()

    def set_current_version( self, event ):
        event.Skip()


    def on_up( self, event ):
        event.Skip()

    def on_down( self, event ):
        event.Skip()


###########################################################################
## Class BaseElementPanel
###########################################################################

class BaseElementPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer24 = wx.BoxSizer( wx.VERTICAL )

        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Шифр:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        bSizer23.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer23.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer23.Add( self.m_textCtrl2, 2, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer24.Add( bSizer23, 0, wx.EXPAND, 5 )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Название структурного элемента", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        bSizer24.Add( self.m_staticText16, 0, wx.ALL, 5 )

        self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer24.Add( self.m_textCtrl5, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Официальный", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer24.Add( self.m_checkBox1, 0, wx.ALL, 5 )


        self.SetSizer( bSizer24 )
        self.Layout()
        bSizer24.Fit( self )

    def __del__( self ):
        pass


###########################################################################
## Class BaseFilePanel
###########################################################################

class BaseFilePanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer24 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Путь к файлу:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        bSizer24.Add( self.m_staticText16, 0, wx.ALL, 5 )

        self.m_filePicker2 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Путь к файлу", u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
        bSizer24.Add( self.m_filePicker2, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText161 = wx.StaticText( self, wx.ID_ANY, u"Название файла:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText161.Wrap( -1 )

        bSizer24.Add( self.m_staticText161, 0, wx.ALL, 5 )

        self.m_textCtrl51 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        bSizer24.Add( self.m_textCtrl51, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Всего страниц в файле:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        bSizer23.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer23.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY )
        bSizer23.Add( self.m_textCtrl2, 2, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer24.Add( bSizer23, 0, wx.EXPAND, 5 )

        bSizer231 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText131 = wx.StaticText( self, wx.ID_ANY, u"Подмножество страниц:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText131.Wrap( -1 )

        bSizer231.Add( self.m_staticText131, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer231.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        bSizer231.Add( self.m_textCtrl21, 2, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer24.Add( bSizer231, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer24 )
        self.Layout()
        bSizer24.Fit( self )

    def __del__( self ):
        pass


###########################################################################
## Class BaseProjectPanel
###########################################################################

class BaseProjectPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer22 = wx.BoxSizer( wx.VERTICAL )

        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Шифр объекта:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        bSizer23.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.text_code = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        self.text_code.SetMaxLength( 35 )
        bSizer23.Add( self.text_code, 2, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer22.Add( bSizer23, 0, wx.EXPAND, 5 )

        self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Название текущей версии", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )

        bSizer22.Add( self.m_staticText23, 0, wx.ALL, 5 )

        self.text_current_version_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        bSizer22.Add( self.text_current_version_name, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Папка для работы по умолчанию", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        bSizer22.Add( self.m_staticText12, 0, wx.ALL, 5 )

        self.dp_default_save = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        bSizer22.Add( self.dp_default_save, 0, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer22 )
        self.Layout()
        bSizer22.Fit( self )

        # Connect Events
        self.text_code.Bind( wx.EVT_TEXT_ENTER, self.on_code_change )
        self.text_current_version_name.Bind( wx.EVT_TEXT_ENTER, self.on_version_name_change )
        self.dp_default_save.Bind( wx.EVT_DIRPICKER_CHANGED, self.on_default_dir_change )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_code_change( self, event ):
        event.Skip()

    def on_version_name_change( self, event ):
        event.Skip()

    def on_default_dir_change( self, event ):
        event.Skip()


###########################################################################
## Class BaseTomePanel
###########################################################################

class BaseTomePanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer24 = wx.BoxSizer( wx.VERTICAL )

        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Шифр тома:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        bSizer23.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer23.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.lbl_prefix = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_prefix.Wrap( -1 )

        bSizer23.Add( self.lbl_prefix, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.text_tome_code = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.TE_PROCESS_ENTER )
        self.text_tome_code.SetMaxLength( 15 )
        bSizer23.Add( self.text_tome_code, 2, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer24.Add( bSizer23, 0, wx.EXPAND, 5 )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Название тома", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        bSizer24.Add( self.m_staticText16, 0, wx.ALL, 5 )

        self.text_tome_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        bSizer24.Add( self.text_tome_name, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Путь сохранения", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        bSizer31.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer31.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_to_default = wx.Button( self, wx.ID_ANY, u"В папку по умолчанию", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer31.Add( self.btn_to_default, 0, wx.ALL, 5 )


        bSizer24.Add( bSizer31, 0, wx.EXPAND, 5 )

        self.fp_save = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Выберите путь сохранения", u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OVERWRITE_PROMPT|wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
        bSizer24.Add( self.fp_save, 0, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer24 )
        self.Layout()
        bSizer24.Fit( self )

        # Connect Events
        self.text_tome_code.Bind( wx.EVT_TEXT_ENTER, self.on_tome_code_change )
        self.text_tome_name.Bind( wx.EVT_TEXT_ENTER, self.on_tome_name_change )
        self.btn_to_default.Bind( wx.EVT_BUTTON, self.on_move_to_default_folder )
        self.fp_save.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_save_file_change )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_tome_code_change( self, event ):
        event.Skip()

    def on_tome_name_change( self, event ):
        event.Skip()

    def on_move_to_default_folder( self, event ):
        event.Skip()

    def on_save_file_change( self, event ):
        event.Skip()


###########################################################################
## Class AboutDialog
###########################################################################

class AboutDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_CLOSE, title = u"О программе", pos = wx.DefaultPosition, size = wx.Size( 630,419 ), style = wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

        self.rt_about = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
        bSizer1.Add( self.rt_about, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class BaseAddElementDialog
###########################################################################

class BaseAddElementDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добавить структурный элемент", pos = wx.DefaultPosition, size = wx.Size( 403,157 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Структурный элемент:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer9.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        element_typeChoices = []
        self.element_type = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, element_typeChoices, 0 )
        self.element_type.SetSelection( 0 )
        bSizer9.Add( self.element_type, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer7.Add( bSizer9, 0, wx.EXPAND, 5 )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Шифр:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer8.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer8.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.element_code = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.element_code, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer7.Add( bSizer8, 0, wx.EXPAND, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer10.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button2 = wx.Button( self, wx.ID_OK, u"ОК", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_button2, 0, wx.ALL, 5 )

        self.m_button3 = wx.Button( self, wx.ID_CANCEL, u"Отмена", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_button3, 0, wx.ALL, 5 )


        bSizer7.Add( bSizer10, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer7 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class BaseRemoveVersionsDialog
###########################################################################

class BaseRemoveVersionsDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Удалить версии проекта...", pos = wx.DefaultPosition, size = wx.Size( 516,251 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Список версий:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        bSizer11.Add( self.m_staticText5, 0, wx.ALL, 5 )

        listbox_versionsChoices = []
        self.listbox_versions = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, listbox_versionsChoices, wx.LB_MULTIPLE )
        bSizer11.Add( self.listbox_versions, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer12.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_remove_versions = wx.Button( self, wx.ID_ANY, u"Удалить версии", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.btn_remove_versions, 0, wx.ALL, 5 )

        self.m_button6 = wx.Button( self, wx.ID_CANCEL, u"ОК", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button6, 0, wx.ALL, 5 )


        bSizer11.Add( bSizer12, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.listbox_versions.Bind( wx.EVT_LISTBOX, self.toggle_remove_button )
        self.btn_remove_versions.Bind( wx.EVT_BUTTON, self.on_remove_selected )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def toggle_remove_button( self, event ):
        event.Skip()

    def on_remove_selected( self, event ):
        event.Skip()


