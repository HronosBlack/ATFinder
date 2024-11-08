import wx

from wx.lib.agw.customtreectrl import CustomTreeCtrl, GenericTreeItem
from ATLibrary.core import AT
from ATLibrary.objects import Genre


class SearchPanel(wx.Panel):
    
    def __init__(self, **kwargs) -> None:
        self.at: AT = kwargs.pop('at')
        wx.Panel.__init__(self, **kwargs)
        
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.treeGenres = CustomTreeCtrl(self)
        self.LoadGenres()
        mainSizer.Add(self.treeGenres, 1, wx.ALL | wx.EXPAND, 5)
        
        detailSizer = wx.BoxSizer(wx.VERTICAL)
        
        detailSizer.Add((0, 0), 0, 0, 0)
        detailSizer.Add((0, 0), 0, 0, 0)
        detailSizer.Add((0, 0), 0, 0, 0)
        detailSizer.Add((0, 0), 0, 0, 0)
        
        mainSizer.Add(detailSizer, 1, wx.ALL | wx.EXPAND, 5)
        
        self.SetSizer(mainSizer)
        
        self.Layout()
        
    def LoadGenres(self) -> None:
        rootItem: GenericTreeItem = self.treeGenres.AddRoot("Жанры:")
        allGenres = self.at.AllGenres
        self.__add_genres_to_tree__(allGenres, rootItem)
        
    def __add_genres_to_tree__(self, genres: list[Genre], parent: GenericTreeItem) -> None:
        for genre in genres:
            item = self.treeGenres.AppendItem(
                parentId=parent,
                text=str(genre),
                ct_type=1,
                data=genre
            )
            if len(genre.Childs) > 0:
                self.__add_genres_to_tree__(genre.Childs, item)
