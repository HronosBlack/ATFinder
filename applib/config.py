import configobj, os, sys


class Config():
    
    __APP_PATH = os.path.abspath(os.path.dirname(os.path.join(sys.argv[0])))
    __INI_FILE = os.path.join(__APP_PATH, "config.ini")
    
    def __init__(self) -> None:
        self.__CONFIG = None
        if not os.path.exists(self.__INI_FILE):
            self.__create_conf_file__()
        else:
            self.__CONFIG = configobj.ConfigObj(self.__INI_FILE)
        
    def __create_conf_file__(self) -> None:
        conf = configobj.ConfigObj()
        conf.filename = self.__INI_FILE
        conf['username'] = ""
        conf['window position'] = (0, 0)
        conf['window maximized'] = False
        conf['window size'] = (1000, 700)
        conf.write()
        
    @property
    def Username(self) -> str:
        if self.__CONFIG:
            return self.__CONFIG['username']
        else:
            return ""
    
    @Username.setter
    def Username(self, value: str) -> None:
        if not self.__CONFIG:
            self.__create_conf_file__()
        self.__CONFIG['username'] = value
        self.__CONFIG.write()
        
    @property
    def Pos(self) -> tuple[int, int]:
        if self.__CONFIG:
            return (int(self.__CONFIG['window position'][0]), int(self.__CONFIG['window position'][1]))
        else:
            return (0, 0)
        
    @Pos.setter
    def Pos(self, value: tuple[int, int]) -> None:
        if not self.__CONFIG:
            self.__create_conf_file__()
        self.__CONFIG['window position'] = value
        self.__CONFIG.write()
        
    @property
    def Maximized(self) -> bool:
        if self.__CONFIG:
            return self.__CONFIG.as_bool('window maximized')
        else:
            False
    
    @Maximized.setter
    def Maximized(self, value: bool) -> None:
        if not self.__CONFIG:
            self.__create_conf_file__()
        self.__CONFIG['window maximized'] = value
        self.__CONFIG.write()
        
    @property
    def Size(self) -> tuple[int, int]:
        if self.__CONFIG:
            return (int(self.__CONFIG['window size'][0]), int(self.__CONFIG['window size'][1]))
        return (1000, 700)
    
    @Size.setter
    def Size(self, value: tuple[int, int]) -> None:
        if not self.__CONFIG:
            self.__create_conf_file__()
        self.__CONFIG['window size'] = value
        self.__CONFIG.write()
