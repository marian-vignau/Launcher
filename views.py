# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Apr 10 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class LauncherFrame
###########################################################################

class LauncherFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Applications launcher", pos = wx.DefaultPosition, size = wx.Size( 587,452 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.Notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_BOTTOM )
		self.m_panel1 = wx.Panel( self.Notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		AppsListChoices = []
		self.AppsList = wx.ListBox( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, AppsListChoices, 0 )
		self.AppsList.SetFont( wx.Font( 10, 74, 90, 92, False, "Tahoma" ) )
		
		bSizer2.Add( self.AppsList, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		self.Notebook.AddPage( self.m_panel1, u"Launch", False )
		self.m_panel2 = wx.Panel( self.Notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"PythonPath", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gbSizer1.Add( self.m_staticText2, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.PythonPath = wx.FilePickerCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.PythonPath.SetToolTipString( u"Path to pythonw.exe, used to run .py scripts" )
		
		gbSizer1.Add( self.PythonPath, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.xx = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Path Base", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.xx.Wrap( -1 )
		gbSizer1.Add( self.xx, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.BasePath = wx.DirPickerCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.BasePath.SetToolTipString( u"Base path for the list of applications" )
		
		gbSizer1.Add( self.BasePath, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.Portable = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"Portable mode (replace drive letters)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Portable.SetValue(True) 
		gbSizer1.Add( self.Portable, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Applications", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gbSizer1.Add( self.m_staticText3, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Apps = wx.FilePickerCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.Apps.SetToolTipString( u"Browse to find the app exe or main python script" )
		
		bSizer3.Add( self.Apps, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.Append = wx.Button( self.m_panel2, wx.ID_ANY, u"✚", wx.DefaultPosition, wx.Size( 25,25 ), 0 )
		self.Append.SetFont( wx.Font( 12, 74, 90, 90, False, "Tahoma" ) )
		self.Append.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Append.SetBackgroundColour( wx.Colour( 0, 128, 255 ) )
		self.Append.SetToolTipString( u"Append a new entry to the list" )
		
		bSizer3.Add( self.Append, 0, wx.LEFT|wx.TOP, 5 )
		
		self.Delete = wx.Button( self.m_panel2, wx.ID_ANY, u"✘", wx.DefaultPosition, wx.Size( 25,25 ), 0 )
		self.Delete.SetFont( wx.Font( 12, 74, 90, 90, False, "Tahoma" ) )
		self.Delete.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Delete.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
		self.Delete.SetToolTipString( u"Delete the selected app from the list" )
		
		bSizer3.Add( self.Delete, 0, wx.BOTTOM|wx.TOP, 5 )
		
		self.Edit = wx.Button( self.m_panel2, wx.ID_ANY, u"✔", wx.DefaultPosition, wx.Size( 25,25 ), 0 )
		self.Edit.SetFont( wx.Font( 12, 74, 90, 90, False, "Tahoma" ) )
		self.Edit.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Edit.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.Edit.SetToolTipString( u"Change the selected app." )
		
		bSizer3.Add( self.Edit, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 5 )
		
		self.Down = wx.Button( self.m_panel2, wx.ID_ANY, u"▼", wx.DefaultPosition, wx.Size( 25,25 ), 0 )
		self.Down.SetFont( wx.Font( 12, 74, 90, 90, False, "Tahoma" ) )
		self.Down.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Down.SetBackgroundColour( wx.Colour( 128, 0, 255 ) )
		self.Down.SetToolTipString( u"move up the selected app one position" )
		
		bSizer3.Add( self.Down, 0, wx.BOTTOM|wx.TOP, 5 )
		
		self.Up = wx.Button( self.m_panel2, wx.ID_ANY, u"▲", wx.DefaultPosition, wx.Size( 25,25 ), 0 )
		self.Up.SetFont( wx.Font( 12, 74, 90, 90, False, "Tahoma" ) )
		self.Up.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Up.SetBackgroundColour( wx.Colour( 128, 0, 255 ) )
		self.Up.SetToolTipString( u"Move down the selected app one position" )
		
		bSizer3.Add( self.Up, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 5 )
		
		
		gbSizer1.Add( bSizer3, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		AppEditListChoices = []
		self.AppEditList = wx.ListBox( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, AppEditListChoices, 0 )
		gbSizer1.Add( self.AppEditList, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		
		gbSizer1.AddGrowableCol( 1 )
		gbSizer1.AddGrowableRow( 4 )
		
		self.m_panel2.SetSizer( gbSizer1 )
		self.m_panel2.Layout()
		gbSizer1.Fit( self.m_panel2 )
		self.Notebook.AddPage( self.m_panel2, u"Configuration", True )
		
		bSizer1.Add( self.Notebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.LauncherFrameOnClose )
		self.Notebook.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.NotebookOnNotebookPageChanged )
		self.AppsList.Bind( wx.EVT_LISTBOX_DCLICK, self.AppsListOnListBoxDClick )
		self.PythonPath.Bind( wx.EVT_FILEPICKER_CHANGED, self.PythonPathOnFileChanged )
		self.BasePath.Bind( wx.EVT_DIRPICKER_CHANGED, self.BasePathOnDirChanged )
		self.Portable.Bind( wx.EVT_CHECKBOX, self.PortableOnCheckBox )
		self.Apps.Bind( wx.EVT_FILEPICKER_CHANGED, self.AppsOnFileChanged )
		self.Append.Bind( wx.EVT_BUTTON, self.AppendOnButtonClick )
		self.Delete.Bind( wx.EVT_BUTTON, self.DeleteOnButtonClick )
		self.Edit.Bind( wx.EVT_BUTTON, self.EditOnButtonClick )
		self.Down.Bind( wx.EVT_BUTTON, self.DownOnButtonClick )
		self.Up.Bind( wx.EVT_BUTTON, self.UpOnButtonClick )
		self.AppEditList.Bind( wx.EVT_LISTBOX, self.AppEditListOnListBox )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def LauncherFrameOnClose( self, event ):
		event.Skip()
	
	def NotebookOnNotebookPageChanged( self, event ):
		event.Skip()
	
	def AppsListOnListBoxDClick( self, event ):
		event.Skip()
	
	def PythonPathOnFileChanged( self, event ):
		event.Skip()
	
	def BasePathOnDirChanged( self, event ):
		event.Skip()
	
	def PortableOnCheckBox( self, event ):
		event.Skip()
	
	def AppsOnFileChanged( self, event ):
		event.Skip()
	
	def AppendOnButtonClick( self, event ):
		event.Skip()
	
	def DeleteOnButtonClick( self, event ):
		event.Skip()
	
	def EditOnButtonClick( self, event ):
		event.Skip()
	
	def DownOnButtonClick( self, event ):
		event.Skip()
	
	def UpOnButtonClick( self, event ):
		event.Skip()
	
	def AppEditListOnListBox( self, event ):
		event.Skip()
	

