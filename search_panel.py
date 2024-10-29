import wx


class SearchPanel(wx.Panel):
    
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        
        szrMain = wx.BoxSizer(self, wx.HORIZONTAL)
        
        self.treGenres = wx.TreeCtrl(self, wx.ID_ANY)
        szrMain.Add(self.treGenres, 1, wx.ALL | wx.EXPAND, 5)
        
        szrParams = wx.BoxSizer(wx.VERTICAL)
        szrMain.Add(szrParams, 1, wx.EXPAND, 0)
        
        szrParams.Add((0, 0), 0, 0, 0)
        szrParams.Add((0, 0), 0, 0, 0)
        szrParams.Add((0, 0), 0, 0, 0)
        szrParams.Add((0, 0), 0, 0, 0)
        
        self.SetSizer(szrMain)
