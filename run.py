# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
TODO: Beautify the look, using icons, etc
Create a right-click popup menu to easy access
Validates path before errors
Multiplatform, proving it on Linux
"""

import wx, views, sys, subprocess
import OnTray
import json, os


config_path=os.path.join(os.path.abspath(os.curdir),'config.json')
my_drive=os.path.splitdrive(os.path.abspath(os.curdir))[0]
class MainForm(views.LauncherFrame):
    def __init__(self):
        super(MainForm, self).__init__(None)
        self.Portable.SetLabel('Portable mode (launch from %s drive)'%my_drive)
        self.read()
        self.tbIcon = OnTray.CustomTaskBarIcon(self)

        self.Bind(wx.EVT_ICONIZE, self.onMinimize)
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.Bind(wx.EVT_MOVE, self.onChange)
        self.Bind(wx.EVT_SIZE, self.onChange)

        self.Show()

    def onClose(self, evt):
        "Destroy the taskbar icon and the frame"
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        self.Destroy()

    def onMinimize(self, event):
        "When minimizing, hide the frame so it 'minimizes to tray'"
        self.Hide()

    def onChange(self,event):
        "Write new geometry on move or resize"
        self.write()
        event.Skip()

    @property
    def frame_geom(self):
        "Serializes frame's geometry properties"
        p1=self.GetSize()
        p2=self.GetScreenPosition()
        return {'w': p1.width, 'h': p1.height, 'x': p2.x, 'y': p2.y}

    @frame_geom.setter
    def frame_geom(self, value):
        "Restoration of frame's geometry properties"
        p1=wx.Size(value['w'],value['h'])
        p2=wx.Point(value['x'],value['y'])
        if p1!=self.GetSize():
            self.SetSize(p1)
        if p2!=self.GetScreenPosition():
            self.SetPosition(p2)



    def default(self):
        "Set default values"
        return {'BasePath':os.path.abspath(os.curdir),
            'PythonPath':os.path.abspath(sys.executable),
            'Geometry':self.frame_geom,
            'Portable':True,
            'Apps':[]}

    def read(self):
        "read data from file and show it on display"
        data = self.default()
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                data.update(json.load(f))
        self.PythonPath.SetPath(data['PythonPath'])
        self.BasePath.SetPath(data['BasePath'])
        self.Portable.SetValue(data['Portable'])
        self.frame_geom = data['Geometry']
        self.AppEditList.Clear()
        for item in data['Apps']:
            self.AppEditList.Append(item)
        self.refreshApps(data)
        return data

    def refreshApps(self,data):
        "show the list of apps on main panel"
        self.AppsList.Clear()
        for item in data['Apps']:
            path = item
            if item.startswith('~'):
                item=item[1:]
                path = os.path.join(data['BasePath'], item)
            if data['Portable']:
                path2 = os.path.join(my_drive,os.path.splitdrive(path)[1])
                if os.path.exists(path2):
                   path=path2
            if not os.path.exists(path):
                self.missing_file(path)
            else:
                self.AppsList.Append(item, path)

    def missing_file(self,path):
        dlg = wx.MessageDialog(self,'Missing file','The file %s not exists'%path, wx.ICON_ERROR)
        dlg.ShowModal()
        dlg.Destroy()

    def write(self):
        "write the list of apps on file"
        data={'BasePath':self.BasePath.GetPath(),
            'PythonPath':self.PythonPath.GetPath(),
            'Geometry':self.frame_geom,
            'Portable':self.Portable.GetValue(),
            'Apps':[]}
        for idx in range(self.AppEditList.GetCount()):
            data['Apps'].append(self.AppEditList.GetString(idx))
        with open(config_path, 'w') as f:
            json.dump(data,f)
        self.refreshApps(data)

    def PortableOnCheckBox(self,event):
        self.write()

    def BasePathOnDirChanged( self, event ):
        self.write()

    def PythonPathOnFileChanged( self, event ):
        self.write()

    def AppEditListOnListBox(self, event):
        self.Apps.SetPath(self.AppEditList.GetStringSelection())

    def get_new_app(self):
        "reads the path of the new app and extract de BasePath from it"
        new_app=self.Apps.GetPath()
        if new_app.startswith(self.BasePath.GetPath()):
            new_app = '~'+new_app[len(self.BasePath.GetPath())+1:]
        return new_app

    def AppendOnButtonClick(self, event):
        "append a new app to the list"
        new_app=self.get_new_app()
        idx=self.AppEditList.FindString(new_app)
        if idx == wx.NOT_FOUND:
            self.AppEditList.Append(new_app)
            self.write()
            self.Apps.SetPath('')

    def DeleteOnButtonClick(self, event):
        "delete one app from the list"
        if not self.AppEditList.IsEmpty():
            idx=self.AppEditList.GetSelection()
            if idx != wx.NOT_FOUND:
                self.AppEditList.Delete(idx)
                self.write()
                self.Apps.SetPath('')

    def EditOnButtonClick(self, event):
        "change one app on the list"
        if not self.AppEditList.IsEmpty():
            idx=self.AppEditList.GetSelection()
            self.AppEditList.SetString(idx, self.get_new_app())
            self.write()

    def UpOnButtonClick(self, event):
        "move up the selected app one position"
        if self.AppEditList.GetCount() > 1:
            self.interchange(self.AppEditList.GetSelection(),-1)

    def DownOnButtonClick(self, event):
        "move down the selected app one position"
        if self.AppEditList.GetCount() > 1:
            self.interchange(self.AppEditList.GetSelection(),+1)

    def interchange(self,idx,diff):
        "interchange two string-items into de listbox"
        obj = self.AppEditList
        if obj.GetCount() > 1 and (idx+diff) >= 0 and (idx+diff) < obj.GetCount():
            text = obj.GetString(idx)
            obj.SetString(idx,obj.GetString(idx+diff))
            obj.SetString(idx+diff,text)
            obj.SetSelection(idx+diff)
            self.write()

    def AppsListOnListBoxDClick(self, event):
        "Iconize to system tray and run the app"
        item = event.Selection
        if item >= 0:
            self.Iconize(True)
            self.run(self.AppsList.GetClientData(item))

    def run(self,file_name):
        "run the selected app"
        if file_name.endswith('.py') or file_name.endswith('.pyw'):
            os.chdir(os.path.dirname(file_name))
            subprocess.Popen([self.PythonPath.GetPath(),file_name])
        elif file_name.endswith('.exe'):
            subprocess.Popen([file_name])
        else:
            try:
                os.system('"%s"'%file_name)
                #subprocess.Popen([file_name])
            except Exception as error:
                print 'Error %s ' % error.message


# make an image list using the images

class Aplic(object):
    """
    iloc = wx.IconLocation(exefile, 0)
    icon = wx.IconFromLocation(iloc)
    bmp = wx.BitmapFromIcon(icon)
    """
    def __init__(self):
        self.app = wx.App(0)
        self.main()

    def main (self):
        self.main=MainForm()
        self.app.SetTopWindow(self.main)
        self.main.Show()
        self.app.MainLoop()

if __name__=="__main__":
    Aplic()
