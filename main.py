"""
Основной скрипт приложения
"""
import wx

from assets.forms.mainform import MainForm


if __name__ == '__main__':
    app = wx.App(False)
    mainForm = MainForm(parent=None, id=wx.ID_ANY, title="Поиск по онлайн-библиотеке Author.Today")
    app.MainLoop()
