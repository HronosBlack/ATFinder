import wx

from wx.lib.pubsub import pub


class AuthDialog(wx.Dialog):
    
    def __init__(self, **kwargs) -> None:
        username: str = kwargs.pop('username')
        kwargs['name'] = "authorizationDialog"
        wx.Dialog.__init__(self, **kwargs)
        self.SetIcon(wx.Icon("assets/img/login.png", wx.BITMAP_TYPE_PNG))
        
        # Блок данных учётной записи пользователя
        dataSizer = wx.BoxSizer(wx.VERTICAL)
        
        userLabel = wx.StaticText(self, label="Логин:")
        dataSizer.Add(userLabel, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.SHAPED, 3)
        
        self.userName = wx.TextCtrl(self, value=username)
        dataSizer.Add(self.userName, 0, wx.ALL | wx.EXPAND, 5)
        
        passLabel = wx.StaticText(self, label="Пароль:")
        dataSizer.Add(passLabel, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.SHAPED, 3)
        
        self.userPass = wx.TextCtrl(self, style=wx.TE_PASSWORD | wx.TE_PROCESS_ENTER)
        dataSizer.Add(self.userPass, 0, wx.ALL | wx.EXPAND, 5)
        
        # Блок кнопок диалогового окна
        buttonSizer = wx.StdDialogButtonSizer()
        
        self.btnLogin = wx.Button(self, wx.ID_OK, "Войти")
        self.btnLogin.SetDefault()
        self.btnLogin.Bind(wx.EVT_BUTTON, self.OnLoginClick)
        buttonSizer.AddButton(self.btnLogin)
        
        self.btnCancel = wx.Button(self, wx.ID_CANCEL, "Отмена")
        self.btnCancel.Bind(wx.EVT_BUTTON, self.OnCancelClick)
        buttonSizer.AddButton(self.btnCancel)
        
        buttonSizer.Realize()
        
        # Блок описания диалогового окна
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(dataSizer, 1, wx.EXPAND, 0)
        mainSizer.Add(buttonSizer, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 4)
        
        self.SetSizer(mainSizer)
        mainSizer.Fit(self)
        
        self.SetAffirmativeId(self.btnLogin.GetId())
        self.SetEscapeId(self.btnCancel.GetId())
        
        self.Layout()
        self.Center()
        
    def OnLoginClick(self, event) -> None:
        userData = {
            'userName': self.userName.GetValue(),
            'userPass': self.userPass.GetValue()
            }
        pub.sendMessage("loginAT", userData=userData)
        self.Destroy()
    
    def OnCancelClick(self, event) -> None:
        self.Destroy()
