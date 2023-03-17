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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PDF Report Builder", pos = wx.DefaultPosition, size = wx.Size( 942,756 ), style = wx.DEFAULT_FRAME_STYLE|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.menu_project = wx.Menu()
        self.menu_project_new = wx.MenuItem( self.menu_project, wx.ID_ANY, u"Новый проект\tCtrl+N", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_project.Append( self.menu_project_new )

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

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.lbl_project_name = wx.StaticText( self, wx.ID_ANY, u"Название проекта", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_project_name.SetLabelMarkup( u"Название проекта" )
        self.lbl_project_name.Wrap( -1 )

        self.lbl_project_name.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer4.Add( self.lbl_project_name, 0, wx.ALL, 5 )


        bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_bpButton2 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

        self.m_bpButton2.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_EDIT, wx.ART_BUTTON ) )
        bSizer4.Add( self.m_bpButton2, 0, wx.ALL, 5 )


        bSizer3.Add( bSizer4, 0, wx.EXPAND, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Текущая версия:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer5.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        m_choice1Choices = []
        self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        bSizer5.Add( self.m_choice1, 1, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

        self.m_bpButton1.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_COPY, wx.ART_BUTTON ) )
        bSizer5.Add( self.m_bpButton1, 0, wx.ALL, 5 )


        bSizer3.Add( bSizer5, 0, wx.EXPAND, 5 )

        self.m_treeCtrl1 = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        bSizer3.Add( self.m_treeCtrl1, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Сформировать отчеты!", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button2, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.onExit, id = self.m_close.GetId() )
        self.Bind( wx.EVT_MENU, self.onAbout, id = self.menu_about_about.GetId() )
        self.Bind( wx.EVT_MENU, self.onDocsOpen101, id = self.menu_about_gost101.GetId() )
        self.Bind( wx.EVT_MENU, self.onDocsOpen301, id = self.menu_about_gost301.GetId() )
        self.Bind( wx.EVT_MENU, self.onDocsOpen105, id = self.menu_about_gost105.GetId() )
        self.Bind( wx.EVT_MENU, self.onDocsOpen47, id = self.menu_about_sp47.GetId() )
        self.Bind( wx.EVT_MENU, self.onDocsOpen317, id = self.menu_about_sp317.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onExit( self, event ):
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


###########################################################################
## Class AboutDialog
###########################################################################

class AboutDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_CLOSE, title = u"О программе", pos = wx.DefaultPosition, size = wx.Size( 630,419 ), style = wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

        self.rt_about = wx.richtext.RichTextCtrl( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
        bSizer1.Add( self.rt_about, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


