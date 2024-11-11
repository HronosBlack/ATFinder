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
        self.treeGenres.Expand(self.treeGenres.GetRootItem())
        mainSizer.Add(self.treeGenres, 2, wx.ALL | wx.EXPAND, 5)
        
        detailSizer = wx.BoxSizer(wx.VERTICAL)
        
        accessSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        accessLabel = wx.StaticText(self, label="Доступ:")
        accessSizer.Add(accessLabel, 2, wx.EXPAND | wx.ALL, 5)
        
        self.accessList = wx.ComboBox(self)
        for access in self.at.AllAccesses:
            self.accessList.Append(str(access), access)
        self.accessList.Select(0)
        self.accessList.Bind(wx.EVT_COMBOBOX, self.OnCheckAccess)
        accessSizer.Add(self.accessList, 3, wx.ALL | wx.EXPAND, 5)
        
        formatSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        formatLabel = wx.StaticText(self, label="Формат:")
        formatSizer.Add(formatLabel, 2, wx.ALL | wx.EXPAND, 5)
        
        self.formatList = wx.ComboBox(self)
        for format in self.at.AllFormat:
            self.formatList.Append(str(format), format)
        self.formatList.Select(0)
        self.formatList.Bind(wx.EVT_COMBOBOX, self.OnCheckFormat)
        formatSizer.Add(self.formatList, 3, wx.ALL | wx.EXPAND, 5)
        
        workFormSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        workFormLabel = wx.StaticText(self, label="Форма произведения:")
        workFormSizer.Add(workFormLabel, 2, wx.ALL | wx.EXPAND, 5)
        
        self.workFormList = wx.ComboBox(self)
        for workForm in self.at.AllWorkForms:
            self.workFormList.Append(str(workForm), workForm)
        self.workFormList.Select(0)
        self.workFormList.Bind(wx.EVT_COMBOBOX, self.OnCheckWorkForm)
        workFormSizer.Add(self.workFormList, 3, wx.ALL | wx.EXPAND, 5)
        
        detailSizer.Add(workFormSizer, 0, wx.ALL | wx.EXPAND, 0)
        detailSizer.Add(accessSizer, 0, wx.ALL | wx.EXPAND, 0)
        detailSizer.Add(formatSizer, 0, wx.ALL | wx.EXPAND, 0)
        detailSizer.Add((0, 0), 10, 0, 0)
        
        mainSizer.Add(detailSizer, 3, wx.ALL | wx.EXPAND, 0)
        
        self.SetSizer(mainSizer)
        
        self.Layout()
        
    def OnCheckAccess(self, event) -> None:
        access = event.GetClientData()
        print(str(access) + f"\t{access.UrlPrefix}={access.UrlKey}")
        
    def OnCheckFormat(self, event) -> None:
        format = event.GetClientData()
        print(str(format) + f"\t{format.UrlPrefix}={format.UrlKey}")
        
    def OnCheckWorkForm(self, event) -> None:
        workForm = event.GetClientData()
        print(str(workForm) + f"\t{workForm.UrlPrefix}={workForm.UrlKey}")
        
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
