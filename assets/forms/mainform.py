import wx

from wx.lib.pubsub import pub
from assets.forms.authdialog import AuthDialog
from assets.panels.searchpanel import SearchPanel
from ATLibrary.core import AT
from applib.config import Config


class MainForm(wx.Frame):
    
    def __init__(self, **kwargs) -> None:
        kwargs['name'] = "mainForm"
        wx.Frame.__init__(self, **kwargs)
        self.SetIcon(wx.Icon("assets/img/icon.png", wx.BITMAP_TYPE_PNG))
        
        self.atauth = False
        
        # Блок главного меню приложения
        menubar = wx.MenuBar()
        
        self.fileMenu = wx.Menu()
        
        self.authMenuItem = wx.MenuItem(
            self.fileMenu,
            wx.ID_ANY,
            "Авторизация...",
            "Авторизация в онлайн-библиотеке Author.Today"
        )
        self.Bind(wx.EVT_MENU, self.OnAuthMenuClick, self.authMenuItem)
        self.fileMenu.Append(self.authMenuItem)
        
        self.fileMenu.AppendSeparator()
        
        self.exitMenuItem = wx.MenuItem(
            self.fileMenu,
            wx.ID_EXIT,
            "Выход",
            "Выход из приложения"
        )
        self.Bind(wx.EVT_MENU, self.OnCloseMenuClick, self.exitMenuItem)
        self.fileMenu.Append(self.exitMenuItem)
        
        self.searchMenu = wx.Menu()
        
        self.searchMenuItem = wx.MenuItem(
            None,
            wx.ID_ANY,
            "Поиск...",
            "Открыть панель поиска произведений"
        )
        self.Bind(wx.EVT_MENU, self.OnSearchMenuClick, self.searchMenuItem)
        self.searchMenu.Append(self.searchMenuItem)
        self.__set_enabled__()
        
        menubar.Append(self.fileMenu, "Файл")
        menubar.Append(self.searchMenu, "Поиск")
        self.SetMenuBar(menubar)
        
        self.mainPanel = wx.Panel(self, wx.ID_ANY)
        
        # Блок логики
        self.at = AT()
        self.conf = Config()
        pub.subscribe(self.OnLogin, "loginAT")
        
        self.Bind(wx.EVT_CLOSE, self.OnClose, self)
        
        self.SetPosition(wx.Point(self.conf.Pos[0], self.conf.Pos[1]))
        self.SetSize((self.conf.Size[0], self.conf.Size[1]))
        self.Maximize(self.conf.Maximized)
        
        self.Show()
    
    def OnClose(self, event) -> None:
        if not self.IsMaximized():
            self.conf.Pos = (self.Position[0], self.Position[1])
            self.conf.Size = (self.Size[0], self.Size[1])
        self.conf.Maximized = self.IsMaximized()
        self.Destroy()
    
    def OnCloseMenuClick(self, event) -> None:
        self.Close()
    
    def OnAuthMenuClick(self, event) -> None:
        authDlg = AuthDialog(parent=self, title="Авторизация в AT", username=self.conf.Username)
        authDlg.ShowModal()
        
    def OnSearchMenuClick(self, event) -> None:
        self.mainPanel.Destroy()
        self.mainPanel = SearchPanel(parent=self, at=self.at)
        self.Layout()
        self.Fit()
        
    def OnLogin(self, userData, arg2=None) -> None:
        answer = self.at.Login(userData['userName'], userData['userPass'])
        if 'token' in answer:
            self.conf.Username = userData['userName']
            self.atauth = True
            self.__set_enabled__()
        else:
            self.atauth = False
            self.__set_enabled__()
            errorData = ""
            if 'invalidFields' in answer:
                errorData += f"\n\tОшибки:"
                if 'login' in answer['invalidFields']:
                    errorData += f"\n{answer['invalidFields']['login'][0]}"
                if 'password' in answer['invalidFields']:
                    errorData += f"\n{answer['invalidFields']['password'][0]}"
            errorMessage = wx.MessageDialog(
                self,
                f"{answer['message']}{errorData}",
                "Ошибка авторизации Author.Today",
                style=wx.OK | wx.ICON_ERROR | wx.CENTER)
            errorMessage.ShowModal()
            self.OnAuthMenuClick()

    def __set_enabled__(self) -> None:
        self.searchMenuItem.Enable(self.atauth)
