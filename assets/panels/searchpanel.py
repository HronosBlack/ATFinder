import wx
import wx.lib.agw.customtreectrl as wxc

from ATLibrary.core import AT
from ATLibrary.objects import Genre, Access


class SearchPanel(wx.Panel):
    
    def __init__(self, **kwargs) -> None:
        self.at: AT = kwargs.pop('at')
        wx.Panel.__init__(self, **kwargs)
        
        self.checkGenres: list[Genre] = []
        
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.treeGenres = wxc.CustomTreeCtrl(self)
        self.LoadGenres()
        self.treeGenres.ExpandAll()
        mainSizer.Add(self.treeGenres, 2, wx.ALL | wx.EXPAND, 5)
        
        detailSizer = wx.BoxSizer(wx.VERTICAL)
        
        accessSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        accessLabel = wx.StaticText(self, label="Доступ:")
        accessSizer.Add(accessLabel, 2, wx.EXPAND | wx.ALL, 5)
        
        self.accessList = wx.ComboBox(self)
        for access in self.at.AllAccesses:
            accessItem = self.accessList.Append(str(access), access)
        self.accessList.Bind(wx.EVT_COMBOBOX, self.OnCheckAccess)
        self.accessList.Select(0)
        accessSizer.Add(self.accessList, 3, wx.ALL | wx.EXPAND, 5)
        
        detailSizer.Add(accessSizer, 0, wx.ALL | wx.EXPAND, 0)
        detailSizer.Add((0, 0), 10, 0, 0)
        
        mainSizer.Add(detailSizer, 3, wx.ALL | wx.EXPAND, 0)
        
        self.SetSizer(mainSizer)
        
        self.Layout()
        
    def OnCheckAccess(self, event) -> None:
        access = event.GetClientData()
        print(str(access))
        
    def LoadGenres(self) -> None:
        rootItem: wxc.GenericTreeItem = self.treeGenres.AddRoot("Жанры:")
        allGenres = self.at.AllGenres
        self.__add_genres_to_tree__(allGenres, rootItem)
        mti = self.at.sample()
        print(mti)
        
    def __add_genres_to_tree__(self, genres: list[Genre], parent: wxc.GenericTreeItem) -> None:
        for genre in genres:
            item = self.treeGenres.AppendItem(
                parentId=parent,
                text=str(genre),
                ct_type=1,
                data=genre
            )
            self.Bind(wxc.EVT_TREE_ITEM_CHECKED, self.__check__genre__)
            if len(genre.Childs) > 0:
                self.__add_genres_to_tree__(genre.Childs, item)
                
    def __check__genre__(self, event) -> None:
        item: wxc.GenericTreeItem = event.GetItem()
        genre: Genre = item.GetData()
        if item.IsChecked():
            self.checkGenres.append(genre)
        else:
            self.checkGenres.pop(self.checkGenres.index(genre))
