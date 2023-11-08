# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.richtext
import wx.dataview

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PDF Report Builder", pos = wx.DefaultPosition, size = wx.Size( 1125,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 500,450 ), wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

        self.m_menubar1 = wx.MenuBar( 0 )
        self.menu_project = wx.Menu()
        self.menu_project_new = wx.MenuItem( self.menu_project, wx.ID_ANY, u"Новый проект\tCtrl+N", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_project.Append( self.menu_project_new )

        self.menu_open_template = wx.Menu()
        self.menu_project.AppendSubMenu( self.menu_open_template, u"Создать из шаблона" )

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

        self.menu_utils = wx.Menu()
        self.menu_utils_sheetscalc = wx.MenuItem( self.menu_utils, wx.ID_ANY, u"Калькулятор страниц", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_utils.Append( self.menu_utils_sheetscalc )

        self.menu_utils_pagescount = wx.MenuItem( self.menu_utils, wx.ID_ANY, u"Обзор структуры", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_utils.Append( self.menu_utils_pagescount )

        self.menu_utils.AppendSeparator()

        self.menu_utils_make_pdfs = wx.MenuItem( self.menu_utils, wx.ID_ANY, u"Сформировать PDF для всех автособираемых", wx.EmptyString, wx.ITEM_NORMAL )
        self.menu_utils.Append( self.menu_utils_make_pdfs )

        self.m_menubar1.Append( self.menu_utils, u"Инструменты" )

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

        bSizer3.SetMinSize( wx.Size( 320,-1 ) )
        bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer21.SetMinSize( wx.Size( -1,33 ) )
        self.lbl_version1 = wx.StaticText( self, wx.ID_ANY, u"Свойства", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_version1.Wrap( -1 )

        self.lbl_version1.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

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

        self.btn_merge = wx.Button( self, wx.ID_ANY, u"Сформировать отчеты...", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.btn_merge, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer20.Add( bSizer3, 0, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        bSizer6.SetMinSize( wx.Size( 300,-1 ) )
        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.lbl_version = wx.StaticText( self, wx.ID_ANY, u"Текущая версия:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_version.Wrap( -1 )

        self.lbl_version.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

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

        self.m_button15 = wx.Button( self, wx.ID_ANY, u"Обновить", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.m_button15.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_DIR_UP, wx.ART_BUTTON ) )
        self.m_button15.SetBitmapPosition( wx.RIGHT )
        bSizer13.Add( self.m_button15, 0, wx.ALL, 5 )

        self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        self.m_staticline6.SetToolTip( u"Перезагрузить проект" )
        self.m_staticline6.SetHelpText( u"Перезагрузить проект" )
        self.m_staticline6.SetMinSize( wx.Size( -1,20 ) )

        bSizer13.Add( self.m_staticline6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

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
        self.Bind( wx.EVT_MENU, self.open_sheets_calc, id = self.menu_utils_sheetscalc.GetId() )
        self.Bind( wx.EVT_MENU, self.open_pagescount, id = self.menu_utils_pagescount.GetId() )
        self.Bind( wx.EVT_MENU, self.open_buildcomputed, id = self.menu_utils_make_pdfs.GetId() )
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
        self.m_button15.Bind( wx.EVT_BUTTON, self.reload_project )
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

    def open_sheets_calc( self, event ):
        event.Skip()

    def open_pagescount( self, event ):
        event.Skip()

    def open_buildcomputed( self, event ):
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


    def reload_project( self, event ):
        event.Skip()

    def on_up( self, event ):
        event.Skip()

    def on_down( self, event ):
        event.Skip()


###########################################################################
## Class BaseCalculatorDialog
###########################################################################

class BaseCalculatorDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Калькулятор листов", pos = wx.DefaultPosition, size = wx.Size( 692,487 ), style = wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetExtraStyle( self.GetExtraStyle() | wx.WS_EX_TRANSIENT )

        bSizer32 = wx.BoxSizer( wx.VERTICAL )

        bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer36 = wx.BoxSizer( wx.VERTICAL )

        self.grid_blocks = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.grid_blocks.CreateGrid( 0, 4 )
        self.grid_blocks.EnableEditing( True )
        self.grid_blocks.EnableGridLines( True )
        self.grid_blocks.EnableDragGridSize( False )
        self.grid_blocks.SetMargins( 0, 0 )

        # Columns
        self.grid_blocks.SetColSize( 0, 195 )
        self.grid_blocks.SetColSize( 1, 115 )
        self.grid_blocks.SetColSize( 2, 94 )
        self.grid_blocks.SetColSize( 3, 73 )
        self.grid_blocks.AutoSizeColumns()
        self.grid_blocks.EnableDragColMove( False )
        self.grid_blocks.EnableDragColSize( True )
        self.grid_blocks.SetColLabelValue( 0, u"Название" )
        self.grid_blocks.SetColLabelValue( 1, u"Формат листов" )
        self.grid_blocks.SetColLabelValue( 2, u"Кол-во листов" )
        self.grid_blocks.SetColLabelValue( 3, u"Подитог" )
        self.grid_blocks.SetColLabelValue( 4, wx.EmptyString )
        self.grid_blocks.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.grid_blocks.EnableDragRowSize( True )
        self.grid_blocks.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.grid_blocks.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer36.Add( self.grid_blocks, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"ИТОГО: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText34.Wrap( -1 )

        self.m_staticText34.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer37.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.lbl_itogo = wx.StaticText( self, wx.ID_ANY, u"0 листов; 0 эквивалентно формату A4", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_itogo.Wrap( -1 )

        bSizer37.Add( self.lbl_itogo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer36.Add( bSizer37, 0, wx.EXPAND, 5 )

        bSizer371 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText341 = wx.StaticText( self, wx.ID_ANY, u"ВЫБОРКА:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText341.Wrap( -1 )

        self.m_staticText341.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer371.Add( self.m_staticText341, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.lbl_selection = wx.StaticText( self, wx.ID_ANY, u"0 листов; 0 эквивалентно формату A4", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_selection.Wrap( -1 )

        bSizer371.Add( self.lbl_selection, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer36.Add( bSizer371, 0, wx.EXPAND, 5 )


        bSizer34.Add( bSizer36, 3, wx.EXPAND, 5 )

        bSizer35 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer41 = wx.BoxSizer( wx.VERTICAL )

        list_sheetsChoices = []
        self.list_sheets = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, list_sheetsChoices, wx.LB_EXTENDED|wx.LB_HSCROLL|wx.LB_NEEDED_SB )
        bSizer41.Add( self.list_sheets, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer35.Add( bSizer41, 1, wx.EXPAND, 5 )


        bSizer34.Add( bSizer35, 2, wx.EXPAND, 5 )


        bSizer32.Add( bSizer34, 1, wx.EXPAND, 5 )

        bSizer33 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer33.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_save = wx.Button( self, wx.ID_ANY, u"Сохранить в файл", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer33.Add( self.btn_save, 0, wx.ALL, 5 )

        self.m_button11 = wx.Button( self, wx.ID_ANY, u"Загрузить из файла", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer33.Add( self.m_button11, 0, wx.ALL, 5 )

        self.btn_close = wx.Button( self, wx.ID_ANY, u"Закрыть", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer33.Add( self.btn_close, 0, wx.ALL, 5 )


        bSizer32.Add( bSizer33, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer32 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.grid_blocks.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.grid_updated )
        self.grid_blocks.Bind( wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.OnCellRightClick )
        self.list_sheets.Bind( wx.EVT_LISTBOX, self.on_listbox_selection )
        self.btn_save.Bind( wx.EVT_BUTTON, self.on_save )
        self.m_button11.Bind( wx.EVT_BUTTON, self.on_load )
        self.btn_close.Bind( wx.EVT_BUTTON, self.on_close )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def grid_updated( self, event ):
        event.Skip()

    def OnCellRightClick( self, event ):
        event.Skip()

    def on_listbox_selection( self, event ):
        event.Skip()

    def on_save( self, event ):
        event.Skip()

    def on_load( self, event ):
        event.Skip()

    def on_close( self, event ):
        event.Skip()


###########################################################################
## Class BaseElementPanel
###########################################################################

class BaseElementPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer24 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Структурный элемент", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText25.Wrap( -1 )

        self.m_staticText25.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer24.Add( self.m_staticText25, 0, wx.ALL, 5 )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Название структурного элемента", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        bSizer24.Add( self.m_staticText16, 0, wx.ALL, 5 )

        self.text_element_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        bSizer24.Add( self.text_element_name, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Шифр:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        bSizer23.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer23.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.text_element_code = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        bSizer23.Add( self.text_element_code, 2, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer24.Add( bSizer23, 0, wx.EXPAND, 5 )

        self.cb_code_add = wx.CheckBox( self, wx.ID_ANY, u"Добавлять полный шифр в готовый документ", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer24.Add( self.cb_code_add, 0, wx.ALL, 5 )

        self.m_staticText601 = wx.StaticText( self, wx.ID_ANY, u"(не распространяется на вложенные элементы)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText601.Wrap( -1 )

        self.m_staticText601.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer24.Add( self.m_staticText601, 0, wx.ALL, 5 )

        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel4.SetBackgroundColour( wx.Colour( 243, 231, 224 ) )

        bSizer49 = wx.BoxSizer( wx.VERTICAL )

        bSizer50 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText591 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Настройки закладок", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText591.Wrap( -1 )

        self.m_staticText591.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer50.Add( self.m_staticText591, 0, wx.ALL, 5 )


        bSizer50.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_bitmap1 = wx.StaticBitmap( self.m_panel4, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_ADD_BOOKMARK, wx.ART_OTHER ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer50.Add( self.m_bitmap1, 0, wx.ALL, 5 )


        bSizer49.Add( bSizer50, 0, wx.EXPAND, 5 )

        self.cb_create_bookmark = wx.CheckBox( self.m_panel4, wx.ID_ANY, u"Создавать закладку", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer49.Add( self.cb_create_bookmark, 0, wx.ALL, 5 )


        self.m_panel4.SetSizer( bSizer49 )
        self.m_panel4.Layout()
        bSizer49.Fit( self.m_panel4 )
        bSizer24.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_panel41 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.m_panel41.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

        bSizer491 = wx.BoxSizer( wx.VERTICAL )

        bSizer501 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText5911 = wx.StaticText( self.m_panel41, wx.ID_ANY, u"Настройки нумерации", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5911.Wrap( -1 )

        self.m_staticText5911.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer501.Add( self.m_staticText5911, 0, wx.ALL, 5 )


        bSizer501.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_bitmap11 = wx.StaticBitmap( self.m_panel41, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_LIST_VIEW, wx.ART_OTHER ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer501.Add( self.m_bitmap11, 0, wx.ALL, 5 )


        bSizer491.Add( bSizer501, 0, wx.EXPAND, 5 )

        self.m_staticText60 = wx.StaticText( self.m_panel41, wx.ID_ANY, u"(не распространяются на вложенные элементы)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText60.Wrap( -1 )

        self.m_staticText60.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer491.Add( self.m_staticText60, 0, wx.ALL, 5 )

        self.cb_inner_enumeration = wx.CheckBox( self.m_panel41, wx.ID_ANY, u"Нумеровать листы внутри элемента", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cb_inner_enumeration.SetValue(True)
        bSizer491.Add( self.cb_inner_enumeration, 0, wx.ALL, 5 )


        bSizer491.Add( ( 0, 10), 0, wx.EXPAND, 5 )

        self.cb_enumeration_include = wx.CheckBox( self.m_panel41, wx.ID_ANY, u"Включать в сквозную нумерацию", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer491.Add( self.cb_enumeration_include, 0, wx.ALL, 5 )

        self.cb_enumeration_print = wx.CheckBox( self.m_panel41, wx.ID_ANY, u"Добавить сквозную нумерацию в отчет", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer491.Add( self.cb_enumeration_print, 0, wx.ALL, 5 )


        self.m_panel41.SetSizer( bSizer491 )
        self.m_panel41.Layout()
        bSizer491.Fit( self.m_panel41 )
        bSizer24.Add( self.m_panel41, 0, wx.EXPAND |wx.ALL, 5 )

        self.panel_computed = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.panel_computed.SetBackgroundColour( wx.Colour( 223, 241, 255 ) )

        bSizer492 = wx.BoxSizer( wx.VERTICAL )

        bSizer502 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText5912 = wx.StaticText( self.panel_computed, wx.ID_ANY, u"Настройки автосбора", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5912.Wrap( -1 )

        self.m_staticText5912.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer502.Add( self.m_staticText5912, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer502.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_bitmap12 = wx.StaticBitmap( self.panel_computed, wx.ID_ANY, wx.ArtProvider.GetBitmap( wx.ART_EXECUTABLE_FILE, wx.ART_OTHER ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer502.Add( self.m_bitmap12, 0, wx.ALL, 5 )


        bSizer492.Add( bSizer502, 0, wx.EXPAND, 5 )

        self.fp_pdf_temp_path = wx.FilePickerCtrl( self.panel_computed, wx.ID_ANY, wx.EmptyString, u"Место генерации временного PDF", u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OVERWRITE_PROMPT|wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
        bSizer492.Add( self.fp_pdf_temp_path, 0, wx.ALL|wx.EXPAND, 5 )

        self.fp_template_docx = wx.FilePickerCtrl( self.panel_computed, wx.ID_ANY, wx.EmptyString, u"Шаблон для генерации", u"Word Documents (*.doc;*.docx)|*.doc;*.docx", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer492.Add( self.fp_template_docx, 0, wx.ALL|wx.EXPAND, 5 )


        self.panel_computed.SetSizer( bSizer492 )
        self.panel_computed.Layout()
        bSizer492.Fit( self.panel_computed )
        bSizer24.Add( self.panel_computed, 0, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer24 )
        self.Layout()
        bSizer24.Fit( self )

        # Connect Events
        self.text_element_name.Bind( wx.EVT_TEXT_ENTER, self.on_text_element_name_change )
        self.text_element_code.Bind( wx.EVT_TEXT_ENTER, self.on_text_element_code_change )
        self.cb_code_add.Bind( wx.EVT_CHECKBOX, self.on_toggle_code_add )
        self.cb_create_bookmark.Bind( wx.EVT_CHECKBOX, self.on_toggle_bookmark_creation )
        self.cb_inner_enumeration.Bind( wx.EVT_CHECKBOX, self.on_toggle_inner_enumeration )
        self.cb_enumeration_include.Bind( wx.EVT_CHECKBOX, self.on_toggle_include )
        self.cb_enumeration_print.Bind( wx.EVT_CHECKBOX, self.on_toggle_print )
        self.fp_pdf_temp_path.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_pdf_temp_path_change )
        self.fp_template_docx.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_template_docx_change )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_text_element_name_change( self, event ):
        event.Skip()

    def on_text_element_code_change( self, event ):
        event.Skip()

    def on_toggle_code_add( self, event ):
        event.Skip()

    def on_toggle_bookmark_creation( self, event ):
        event.Skip()

    def on_toggle_inner_enumeration( self, event ):
        event.Skip()

    def on_toggle_include( self, event ):
        event.Skip()

    def on_toggle_print( self, event ):
        event.Skip()

    def on_pdf_temp_path_change( self, event ):
        event.Skip()

    def on_template_docx_change( self, event ):
        event.Skip()


###########################################################################
## Class BaseTomeContentsPropsPanel
###########################################################################

class BaseTomeContentsPropsPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer64 = wx.BoxSizer( wx.VERTICAL )

        self.fp_template_docx = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Шаблон для генерации", u"Word Documents (*.doc;*.docx)|*.doc;*.docx", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer64.Add( self.fp_template_docx, 0, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer64 )
        self.Layout()
        bSizer64.Fit( self )

        # Connect Events
        self.fp_template_docx.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_template_docx_change )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_template_docx_change( self, event ):
        event.Skip()


###########################################################################
## Class BaseFilePanel
###########################################################################

class BaseFilePanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer24 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Файл", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText25.Wrap( -1 )

        self.m_staticText25.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer24.Add( self.m_staticText25, 0, wx.ALL, 5 )

        self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Путь к файлу:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText16.Wrap( -1 )

        bSizer24.Add( self.m_staticText16, 0, wx.ALL, 5 )

        self.fp_file = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Путь к файлу", u"*.pdf", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
        bSizer24.Add( self.fp_file, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText161 = wx.StaticText( self, wx.ID_ANY, u"Название файла:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText161.Wrap( -1 )

        bSizer24.Add( self.m_staticText161, 0, wx.ALL, 5 )

        self.text_file_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        bSizer24.Add( self.text_file_name, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Изменен:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText28.Wrap( -1 )

        bSizer32.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.lbl_modified_datetime = wx.StaticText( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.lbl_modified_datetime.Wrap( -1 )

        bSizer32.Add( self.lbl_modified_datetime, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer24.Add( bSizer32, 0, wx.EXPAND, 5 )

        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Всего страниц в файле:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        bSizer23.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer23.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.text_pages_number = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_READONLY )
        bSizer23.Add( self.text_pages_number, 2, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer24.Add( bSizer23, 0, wx.EXPAND, 5 )

        bSizer231 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText131 = wx.StaticText( self, wx.ID_ANY, u"Подмножество страниц:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText131.Wrap( -1 )

        bSizer231.Add( self.m_staticText131, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer231.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.text_subset = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_PROCESS_ENTER )
        bSizer231.Add( self.text_subset, 2, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer24.Add( bSizer231, 0, wx.EXPAND, 5 )

        self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Пример ввода: <b>2-5,10,12-.</b>", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText26.SetLabelMarkup( u"Пример ввода: <b>2-5,10,12-.</b>" )
        self.m_staticText26.Wrap( -1 )

        self.m_staticText26.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer24.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

        self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"где \".\" - значит \"До конца файла\"", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText27.Wrap( -1 )

        self.m_staticText27.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer24.Add( self.m_staticText27, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


        self.SetSizer( bSizer24 )
        self.Layout()
        bSizer24.Fit( self )

        # Connect Events
        self.fp_file.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_file_change )
        self.text_subset.Bind( wx.EVT_TEXT_ENTER, self.on_subset_change )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_file_change( self, event ):
        event.Skip()

    def on_subset_change( self, event ):
        event.Skip()


###########################################################################
## Class BaseProjectPanel
###########################################################################

class BaseProjectPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer22 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Проект", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText25.Wrap( -1 )

        self.m_staticText25.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer22.Add( self.m_staticText25, 0, wx.ALL, 5 )

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

        self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Место сохранения файла", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )

        bSizer22.Add( self.m_staticText31, 0, wx.ALL, 5 )

        self.text_savepath = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        bSizer22.Add( self.text_savepath, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"Комментарии к текущей версии", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText45.Wrap( -1 )

        bSizer22.Add( self.m_staticText45, 0, wx.ALL, 5 )

        self.text_comments = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
        self.text_comments.SetMaxLength( 1000 )
        self.text_comments.SetMinSize( wx.Size( -1,80 ) )

        bSizer22.Add( self.text_comments, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer22.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

        self.cb_relative_paths = wx.CheckBox( self, wx.ID_ANY, u"Сохранять относительные пути", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cb_relative_paths.SetValue(True)
        bSizer22.Add( self.cb_relative_paths, 0, wx.ALL, 5 )


        self.SetSizer( bSizer22 )
        self.Layout()
        bSizer22.Fit( self )

        # Connect Events
        self.text_code.Bind( wx.EVT_TEXT_ENTER, self.on_code_change )
        self.text_current_version_name.Bind( wx.EVT_TEXT_ENTER, self.on_version_name_change )
        self.text_comments.Bind( wx.EVT_TEXT, self.on_text_comments )
        self.cb_relative_paths.Bind( wx.EVT_CHECKBOX, self.toggle_relative_paths )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_code_change( self, event ):
        event.Skip()

    def on_version_name_change( self, event ):
        event.Skip()

    def on_text_comments( self, event ):
        event.Skip()

    def toggle_relative_paths( self, event ):
        event.Skip()


###########################################################################
## Class BaseTomePanel
###########################################################################

class BaseTomePanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer24 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Том техотчета", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText25.Wrap( -1 )

        self.m_staticText25.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer24.Add( self.m_staticText25, 0, wx.ALL, 5 )

        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Шифр тома:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        bSizer23.Add( self.m_staticText13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer23.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.lbl_prefix = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
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

        self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer24.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText59 = wx.StaticText( self, wx.ID_ANY, u"Настройки сквозной нумерации", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText59.Wrap( -1 )

        self.m_staticText59.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer24.Add( self.m_staticText59, 0, wx.ALL, 5 )

        self.cb_use_custom_enumeration_start = wx.CheckBox( self, wx.ID_ANY, u"Задавать номер первой страницы руками", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer24.Add( self.cb_use_custom_enumeration_start, 0, wx.ALL, 5 )

        bSizer42 = wx.BoxSizer( wx.HORIZONTAL )

        self.spin_custom_enumeration_start = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 99999, 0 )
        bSizer42.Add( self.spin_custom_enumeration_start, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"№ первой страницы тома", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText39.Wrap( -1 )

        bSizer42.Add( self.m_staticText39, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer24.Add( bSizer42, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer24 )
        self.Layout()
        bSizer24.Fit( self )

        # Connect Events
        self.text_tome_code.Bind( wx.EVT_TEXT_ENTER, self.on_tome_code_change )
        self.text_tome_name.Bind( wx.EVT_TEXT_ENTER, self.on_tome_name_change )
        self.btn_to_default.Bind( wx.EVT_BUTTON, self.on_move_to_default_folder )
        self.fp_save.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_save_file_change )
        self.cb_use_custom_enumeration_start.Bind( wx.EVT_CHECKBOX, self.toggle_use_custom_enum_start )
        self.spin_custom_enumeration_start.Bind( wx.EVT_SPINCTRL, self.on_custom_enum_start_update )
        self.spin_custom_enumeration_start.Bind( wx.EVT_TEXT_ENTER, self.on_custom_enum_start_update )

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

    def toggle_use_custom_enum_start( self, event ):
        event.Skip()

    def on_custom_enum_start_update( self, event ):
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
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Добавить структурный элемент", pos = wx.DefaultPosition, size = wx.Size( 403,413 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Поиск:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer9.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.search_bar = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.search_bar.ShowSearchButton( True )
        self.search_bar.ShowCancelButton( False )
        bSizer9.Add( self.search_bar, 1, wx.ALL, 5 )


        bSizer7.Add( bSizer9, 0, wx.EXPAND, 5 )

        self.treelist_elements = wx.dataview.TreeListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )
        self.treelist_elements.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        self.treelist_elements.AppendColumn( u"Структурный элемент", wx.COL_WIDTH_AUTOSIZE, wx.ALIGN_LEFT, wx.COL_RESIZABLE )

        bSizer7.Add( self.treelist_elements, 1, wx.EXPAND |wx.ALL, 5 )

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

        self.btn_ok = wx.Button( self, wx.ID_OK, u"ОК", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.btn_ok, 0, wx.ALL, 5 )

        self.m_button3 = wx.Button( self, wx.ID_CANCEL, u"Отмена", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_button3, 0, wx.ALL, 5 )


        bSizer7.Add( bSizer10, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer7 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.on_close )
        self.search_bar.Bind( wx.EVT_TEXT, self.update_filter )
        self.treelist_elements.Bind( wx.dataview.EVT_TREELIST_SELECTION_CHANGED, self.on_sel_changed )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_close( self, event ):
        event.Skip()

    def update_filter( self, event ):
        event.Skip()

    def on_sel_changed( self, event ):
        event.Skip()


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


###########################################################################
## Class BaseProcessingDialog
###########################################################################

class BaseProcessingDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Формирование PDF-файлов...", pos = wx.DefaultPosition, size = wx.Size( 1015,466 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer29 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer44 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_THEME|wx.TAB_TRAVERSAL )
        bSizer30 = wx.BoxSizer( wx.VERTICAL )

        bSizer43 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText38 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Тома:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText38.Wrap( -1 )

        self.m_staticText38.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer43.Add( self.m_staticText38, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer43.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_select_all_tomes = wx.Button( self.m_panel3, wx.ID_ANY, u"Выбрать все", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer43.Add( self.btn_select_all_tomes, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.btn_deselect_all_tomes = wx.Button( self.m_panel3, wx.ID_ANY, u"Снять выбор со всех", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer43.Add( self.btn_deselect_all_tomes, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer30.Add( bSizer43, 0, wx.EXPAND, 5 )

        self.treelist_tomes = wx.dataview.TreeListCtrl( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_CHECKBOX|wx.dataview.TL_DEFAULT_STYLE|wx.dataview.TL_MULTIPLE )
        self.treelist_tomes.AppendColumn( u"Том", wx.COL_WIDTH_AUTOSIZE, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
        self.treelist_tomes.AppendColumn( u"Начало нумерации", wx.COL_WIDTH_AUTOSIZE, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
        self.treelist_tomes.AppendColumn( u"Путь", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
        self.treelist_tomes.AppendColumn( u"Полный шифр", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )

        bSizer30.Add( self.treelist_tomes, 1, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText24 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Опции формирования:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24.Wrap( -1 )

        self.m_staticText24.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer30.Add( self.m_staticText24, 0, wx.ALL, 5 )

        gSizer1 = wx.GridSizer( 2, 0, 0, 0 )

        self.cb_inner_enumeration = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Нумерация внутри элементов", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cb_inner_enumeration.SetValue(True)
        gSizer1.Add( self.cb_inner_enumeration, 0, wx.ALL, 5 )

        self.cb_add_codes = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Добавлять полные шифры элементов", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cb_add_codes.SetValue(True)
        gSizer1.Add( self.cb_add_codes, 0, wx.ALL, 5 )

        self.cb_enumerate = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Сквозная нумерация", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cb_enumerate.SetValue(True)
        gSizer1.Add( self.cb_enumerate, 0, wx.ALL, 5 )

        self.cb_with_bookmarks = wx.CheckBox( self.m_panel3, wx.ID_ANY, u"Формировать закладки на основе структуры", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.cb_with_bookmarks.SetValue(True)
        gSizer1.Add( self.cb_with_bookmarks, 0, wx.ALL, 5 )


        bSizer30.Add( gSizer1, 0, wx.EXPAND, 5 )


        self.m_panel3.SetSizer( bSizer30 )
        self.m_panel3.Layout()
        bSizer30.Fit( self.m_panel3 )
        bSizer44.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

        self.btn_process = wx.Button( self, wx.ID_ANY, u"Сформировать техотчеты", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.btn_process.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_TICK_MARK, wx.ART_BUTTON ) )
        self.btn_process.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

        bSizer31.Add( self.btn_process, 1, wx.ALL|wx.EXPAND, 5 )

        self.btn_open_folders = wx.Button( self, wx.ID_ANY, u"Открыть выходную папку (папки)", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.btn_open_folders.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FOLDER_OPEN, wx.ART_BUTTON ) )
        bSizer31.Add( self.btn_open_folders, 1, wx.ALL, 5 )


        bSizer44.Add( bSizer31, 0, wx.EXPAND, 5 )


        bSizer29.Add( bSizer44, 1, wx.EXPAND, 5 )

        bSizer45 = wx.BoxSizer( wx.VERTICAL )

        self.text_logger = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer45.Add( self.text_logger, 1, wx.ALL|wx.EXPAND, 5 )

        self.progress_bar = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.progress_bar.SetValue( 0 )
        bSizer45.Add( self.progress_bar, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer29.Add( bSizer45, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer29 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.btn_select_all_tomes.Bind( wx.EVT_BUTTON, self.on_select_all_tomes )
        self.btn_deselect_all_tomes.Bind( wx.EVT_BUTTON, self.on_deselect_all_tomes )
        self.cb_inner_enumeration.Bind( wx.EVT_CHECKBOX, self.toggle_inner_enumeration )
        self.cb_add_codes.Bind( wx.EVT_CHECKBOX, self.toggle_add_codes )
        self.cb_enumerate.Bind( wx.EVT_CHECKBOX, self.toggle_enumerate )
        self.cb_with_bookmarks.Bind( wx.EVT_CHECKBOX, self.toggle_bookmarks )
        self.btn_process.Bind( wx.EVT_BUTTON, self.process )
        self.btn_open_folders.Bind( wx.EVT_BUTTON, self.open_folders )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_select_all_tomes( self, event ):
        event.Skip()

    def on_deselect_all_tomes( self, event ):
        event.Skip()

    def toggle_inner_enumeration( self, event ):
        event.Skip()

    def toggle_add_codes( self, event ):
        event.Skip()

    def toggle_enumerate( self, event ):
        event.Skip()

    def toggle_bookmarks( self, event ):
        event.Skip()

    def process( self, event ):
        event.Skip()

    def open_folders( self, event ):
        event.Skip()


###########################################################################
## Class BasePagesCountDialog
###########################################################################

class BasePagesCountDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Сводные характеристики структуры", pos = wx.DefaultPosition, size = wx.Size( 998,509 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer50 = wx.BoxSizer( wx.VERTICAL )

        self.treelist = wx.dataview.TreeListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )
        self.treelist.AppendColumn( u"Количество листов", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )

        bSizer50.Add( self.treelist, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer51 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button12 = wx.Button( self, wx.ID_CLOSE, u"ОК", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer51.Add( self.m_button12, 0, wx.ALL, 5 )


        bSizer50.Add( bSizer51, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer50 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button12.Bind( wx.EVT_BUTTON, self.on_close )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_close( self, event ):
        event.Skip()


###########################################################################
## Class BaseBuildComputedDialog
###########################################################################

class BaseBuildComputedDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Сформировать PDF...", pos = wx.DefaultPosition, size = wx.Size( 532,586 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer46 = wx.BoxSizer( wx.VERTICAL )

        bSizer48 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Автособираемые элементы:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText41.Wrap( -1 )

        bSizer48.Add( self.m_staticText41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer48.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button18 = wx.Button( self, wx.ID_ANY, u"Выбрать все", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer48.Add( self.m_button18, 0, wx.ALL, 5 )

        self.m_button19 = wx.Button( self, wx.ID_ANY, u"Снять выбор", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer48.Add( self.m_button19, 0, wx.ALL, 5 )


        bSizer46.Add( bSizer48, 0, wx.EXPAND, 5 )

        cl_computedChoices = []
        self.cl_computed = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cl_computedChoices, 0 )
        bSizer46.Add( self.cl_computed, 1, wx.ALL|wx.EXPAND, 5 )

        self.text_logs = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer46.Add( self.text_logs, 2, wx.ALL|wx.EXPAND, 5 )

        self.m_gauge2 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.m_gauge2.SetValue( 0 )
        bSizer46.Add( self.m_gauge2, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer47 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer47.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.btn_process = wx.Button( self, wx.ID_ANY, u"Сформировать PDF для автособираемых элементов...", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer47.Add( self.btn_process, 0, wx.ALL, 5 )

        self.btn_close = wx.Button( self, wx.ID_ANY, u"Выход", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer47.Add( self.btn_close, 0, wx.ALL, 5 )


        bSizer46.Add( bSizer47, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer46 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button18.Bind( wx.EVT_BUTTON, self.on_select_all )
        self.m_button19.Bind( wx.EVT_BUTTON, self.on_deselect_all )
        self.btn_process.Bind( wx.EVT_BUTTON, self.on_process )
        self.btn_close.Bind( wx.EVT_BUTTON, self.on_close )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_select_all( self, event ):
        event.Skip()

    def on_deselect_all( self, event ):
        event.Skip()

    def on_process( self, event ):
        event.Skip()

    def on_close( self, event ):
        event.Skip()


###########################################################################
## Class BaseParseFileDialog
###########################################################################

class BaseParseFileDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 955,614 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer56 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer57 = wx.BoxSizer( wx.VERTICAL )

        lb_pagesChoices = []
        self.lb_pages = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lb_pagesChoices, wx.LB_EXTENDED|wx.LB_HSCROLL )
        bSizer57.Add( self.lb_pages, 3, wx.ALL|wx.EXPAND, 5 )

        bSizer58 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer58.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button20 = wx.Button( self, wx.ID_ANY, u"В новый элемент", wx.DefaultPosition, wx.DefaultSize, 0 )

        self.m_button20.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_PLUS, wx.ART_BUTTON ) )
        bSizer58.Add( self.m_button20, 0, wx.ALL, 5 )


        bSizer58.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer57.Add( bSizer58, 0, wx.EXPAND, 5 )

        bSizer60 = wx.BoxSizer( wx.HORIZONTAL )

        lb_elementsChoices = []
        self.lb_elements = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lb_elementsChoices, 0 )
        bSizer60.Add( self.lb_elements, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer61 = wx.BoxSizer( wx.VERTICAL )

        self.m_button23 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )

        self.m_button23.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_UP, wx.ART_BUTTON ) )
        bSizer61.Add( self.m_button23, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_button24 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )

        self.m_button24.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_DOWN, wx.ART_BUTTON ) )
        bSizer61.Add( self.m_button24, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_button25 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )

        self.m_button25.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_MINUS, wx.ART_BUTTON ) )
        bSizer61.Add( self.m_button25, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer60.Add( bSizer61, 0, wx.EXPAND, 5 )


        bSizer57.Add( bSizer60, 2, wx.EXPAND, 5 )

        bSizer59 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer59.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button21 = wx.Button( self, wx.ID_ANY, u"Добавить", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer59.Add( self.m_button21, 0, wx.ALL, 5 )

        self.m_button22 = wx.Button( self, wx.ID_ANY, u"Отмена", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer59.Add( self.m_button22, 0, wx.ALL, 5 )


        bSizer57.Add( bSizer59, 0, wx.EXPAND, 5 )


        bSizer56.Add( bSizer57, 1, wx.EXPAND, 5 )

        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer56.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer56 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class BaseIGDIMultipartDialog
###########################################################################

class BaseIGDIMultipartDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ИГДИ - несколько частей", pos = wx.DefaultPosition, size = wx.Size( 551,229 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.AddGrowableCol( 1 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, u"Где создать проект:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText43.Wrap( -1 )

        fgSizer1.Add( self.m_staticText43, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fp_save_location = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Место сохранения проекта", u"*.reportprj", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OVERWRITE_PROMPT|wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
        fgSizer1.Add( self.fp_save_location, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

        self.m_staticText431 = wx.StaticText( self, wx.ID_ANY, u"Общий шаблон\nдля содержания тома:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText431.Wrap( -1 )

        fgSizer1.Add( self.m_staticText431, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.fp_tome_contents_template = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Шаблон по умолчанию для содержания тома:", u"Word Documents (*.doc;*.docx)|*.doc;*.docx", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        fgSizer1.Add( self.fp_tome_contents_template, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

        self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Названия отводов\n(через запятую)", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText50.Wrap( -1 )

        fgSizer1.Add( self.m_staticText50, 0, wx.ALL, 5 )

        self.text_taps = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
        fgSizer1.Add( self.text_taps, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

        bSizer69 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Кол-во томов ГЧ:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText44.Wrap( -1 )

        bSizer69.Add( self.m_staticText44, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.spin_n_tomes = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 10, 1 )
        self.spin_n_tomes.SetMinSize( wx.Size( 50,-1 ) )

        bSizer69.Add( self.spin_n_tomes, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        fgSizer1.Add( bSizer69, 1, wx.EXPAND, 5 )

        bSizer70 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText441 = wx.StaticText( self, wx.ID_ANY, u"Макс. километраж\nдля шифра:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText441.Wrap( -1 )

        bSizer70.Add( self.m_staticText441, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.spin_max_km = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 5000, 0 )
        self.spin_max_km.SetMinSize( wx.Size( 80,-1 ) )

        bSizer70.Add( self.spin_max_km, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        fgSizer1.Add( bSizer70, 1, wx.EXPAND, 5 )


        fgSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        bSizer63 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer63.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_button26 = wx.Button( self, wx.ID_CANCEL, u"Отмена", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer63.Add( self.m_button26, 0, wx.ALL, 5 )

        self.m_button27 = wx.Button( self, wx.ID_OK, u"ОК", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer63.Add( self.m_button27, 0, wx.ALL, 5 )


        fgSizer1.Add( bSizer63, 0, wx.EXPAND, 5 )


        self.SetSizer( fgSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.fp_save_location.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_save_location_change )
        self.fp_tome_contents_template.Bind( wx.EVT_FILEPICKER_CHANGED, self.on_contents_template_change )
        self.text_taps.Bind( wx.EVT_TEXT, self.on_taps_enter )
        self.text_taps.Bind( wx.EVT_TEXT_ENTER, self.on_taps_enter )
        self.spin_n_tomes.Bind( wx.EVT_SPINCTRL, self.on_n_tomes_change )
        self.spin_n_tomes.Bind( wx.EVT_TEXT, self.on_n_tomes_change )
        self.spin_n_tomes.Bind( wx.EVT_TEXT_ENTER, self.on_n_tomes_change )
        self.spin_max_km.Bind( wx.EVT_SPINCTRL, self.on_max_km_change )
        self.spin_max_km.Bind( wx.EVT_TEXT, self.on_max_km_change )
        self.spin_max_km.Bind( wx.EVT_TEXT_ENTER, self.on_max_km_change )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def on_save_location_change( self, event ):
        event.Skip()

    def on_contents_template_change( self, event ):
        event.Skip()

    def on_taps_enter( self, event ):
        event.Skip()


    def on_n_tomes_change( self, event ):
        event.Skip()



    def on_max_km_change( self, event ):
        event.Skip()




