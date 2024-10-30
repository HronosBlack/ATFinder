import wx

from ATLibrary.core import AT
from search_panel import SearchPanel


class frmMain(wx.Frame):
    
    def __init__(self):
        # wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, None, title="Поиск по Author.Today")
        
        self.atconn = AT()
        self.atconn.Login("Hronos.Black@gmail.com", "Rtu87qw1")
        
        self.fmnMain = wx.MenuBar()
        self.mnuFile = wx.Menu()
        self.fmnMain.mniAuth = self.mnuFile.Append(wx.ID_ANY, "Авторизация...", "Авторизация в онлайн библиотеке Author.Today")
        self.mnuFile.AppendSeparator()
        self.fmnMain.mniExit = self.mnuFile.Append(wx.ID_EXIT, "Выход", "Выход из программы")
        self.fmnMain.Append(self.mnuFile, "Файл")
        
        self.SetMenuBar(self.fmnMain)
        
        self.plnMain = SearchPanel(self, wx.ID_ANY)
        
        self.Layout()
        
        self.GetGenres()
        
    def GetGenres(self) -> None:
        genres = self.atconn.AllGenres
        self.plnMain.LoadTreeGenre(genres)
