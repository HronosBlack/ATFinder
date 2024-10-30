import wx

from main_frame import frmMain


if __name__ == "__main__":
    app = wx.App(False)
    frame = frmMain()
    app.MainLoop()
