import wx

from ATLibrary.objects import Genre


class SearchPanel(wx.Panel):
    
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        
        szrMain = wx.BoxSizer(wx.HORIZONTAL)
        
        self.treGenres = wx.TreeCtrl(self, wx.ID_ANY)
        szrMain.Add(self.treGenres, 1, wx.ALL | wx.EXPAND, 5)
        
        self.root_node = self.treGenres.AddRoot("Жанры:")
        
        szrParams = wx.BoxSizer(wx.VERTICAL)
        szrMain.Add(szrParams, 1, wx.EXPAND, 0)
        
        szrParams.Add((0, 0), 0, 0, 0)
        szrParams.Add((0, 0), 0, 0, 0)
        szrParams.Add((0, 0), 0, 0, 0)
        szrParams.Add((0, 0), 0, 0, 0)
        
        self.SetSizer(szrMain)
        
    def LoadTreeGenre(self, genres: list[Genre], root_node = None) -> None:
        
        if root_node == None:
            root_node = self.root_node
        
        for genre in genres:
            item = self.treGenres.AppendItem(root_node, str(genre))
            self.treGenres.SetItemData(item, genre)
            if len(genre.Childs) > 0:
                self.LoadTreeGenre(genre.Childs, item)
