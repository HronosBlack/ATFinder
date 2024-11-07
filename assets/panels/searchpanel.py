import wx

from ATLibrary.core import AT


class SearchPanel(wx.Panel):
    
    def __init__(self, **kwargs) -> None:
        self.at: AT = kwargs.pop('at')
        wx.Panel.__init__(self, **kwargs)
        
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.treeGenres = wx.TreeCtrl(self)
        # TODO: Заполнение дерева
        mainSizer.Add(self.treeGenres, 1, wx.ALL | wx.EXPAND, 5)
        
        detailSizer = wx.BoxSizer(wx.VERTICAL)
        
        detailSizer.Add((0, 0), 0, 0, 0)
        detailSizer.Add((0, 0), 0, 0, 0)
        detailSizer.Add((0, 0), 0, 0, 0)
        detailSizer.Add((0, 0), 0, 0, 0)
        
        mainSizer.Add(detailSizer, 1, wx.ALL | wx.EXPAND, 5)
        
        self.SetSizer(mainSizer)
        
        self.Layout()
