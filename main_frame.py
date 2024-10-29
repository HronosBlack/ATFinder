import wx

from ..ATLibrary.core import AT
from search_panel import SearchPanel


class frmMain(wx.Frame):
    
    def __init__(self, *args, **kw):
        kw['style'] = kw.get('style', 0) | wx.DEFAULT_FRAME_STYLE
        super().__init__(*args, **kw)
        self.SetSize((660, 520))
        self.SetTitle("Поиск по Author.Today")
        
        self.fmnMain = wx.MenuBar()
        self.mnuFile = wx.Menu()
        self.fmnMain.mniAuth = self.mnuFile.Append(wx.ID_ANY, "Авторизация...", "Авторизация в онлайн библиотеке Author.Today")
        self.mnuFile.AppendSeparator()
        self.fmnMain.mniExit = self.mnuFile.Append(wx.ID_EXIT, "Выход", "Выход из программы")
        self.fmnMain.Append(self.mnuFile, "Файл")
        self.SetMenuBar(self.fmnMain)
        
        self.plnMain = SearchPanel(self, wx.ID_ANY)
        
        self.Layout()
