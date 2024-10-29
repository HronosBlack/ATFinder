import wx

from main_frame import frmMain


class ATFinderApp(wx.App):
    
    def OnInit(self):
        self.frmMain = frmMain(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frmMain)
        self.frmMain.Show()
        return True


if __name__ == "__main__":
    app = ATFinderApp(0)
    app.MainLoop()
