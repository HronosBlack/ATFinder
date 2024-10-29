import wx


class dlgAuth(wx.Dialog):
    
    def __init__(self, *args, **kw):
        kw["style"] = kw.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        super().__init__(*args, **kw)
        
        self.SetTitle("Авторизация Author.Today")
        
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("assets/img/login.png", wx.BITMAP_TYPE_PNG))
        self.SetIcon(_icon)
        
        szrMain = wx.BoxSizer(wx.VERTICAL)
        
        szrData = wx.BoxSizer(wx.VERTICAL)
        szrMain.Add(szrData, 1, wx.EXPAND, 0)
        
        lblUsername = wx.StaticText(self, wx.ID_INFO, "Логин:")
        szrData.Add(lblUsername, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.SHAPED, 3)
        
        self.edtUsername = wx.TextCtrl(self, wx.ID_ANY, "")
        szrData.Add(self.edtUsername, 0, wx.ALL | wx.EXPAND, 5)
        
        lblPassword = wx.StaticText(self, wx.ID_INFO, "Пароль:")
        szrData.Add(lblPassword, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL | wx.SHAPED, 3)
        
        self.edtPassword = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PASSWORD)
        szrData.Add(self.edtPassword, 0, wx.ALL | wx.EXPAND, 5)
        
        szrButtons = wx.StdDialogButtonSizer()
        szrMain.Add(szrButtons, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 4)
        
        self.btnOK = wx.Button(self, wx.ID_OK, "Вход")
        self.btnOK.SetDefault()
        szrButtons.AddButton(self.btnOK)
        
        self.btnCANCEL = wx.Button(self, wx.ID_CANCEL, "Отмена")
        szrButtons.AddButton(self.btnCANCEL)
        
        szrButtons.Realize()
        
        self.SetSizer(szrMain)
        szrMain.Fit(self)
        
        self.SetAffirmativeId(self.btnOK.GetId())
        self.SetEscapeId(self.btnCANCEL.GetId())
        
        self.Layout()
