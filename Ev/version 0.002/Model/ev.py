# Version 0.002

from Libs.ortakMethodlar import *
from Model.dbConnection import dbConnection

ayarFileAdres = "../ayar.txt"

class EV:
    __odalar = {}
    __id = "-1"
    __username = ""

    def __init__(self):
        configFile = open(ayarFileAdres, "r")
        lines = configFile.readlines()
        configFile.close()

        for i in lines:
            i = i.strip()
            if "username" in i:
                self.__username = i.split(":")[1]
        conn = dbConnection()

        self.__id = conn.getUserID()

        self.yukle()

    def __del__(self):
        # belllekteki veriler veritabanına aktarılır.
        self.kaydet()

    def yukle(self):
        # Veri tabanından veriler yüklenir.
        conn = dbConnection()
        lines = conn.getData()

        for index, item  in enumerate(lines):
            self.__odalar[item[0]] = item[1]

    def kaydet(self):
        # belllekteki veriler veritabanına aktarılır.
        conn = dbConnection()

        for key, value in self.__odalar.items():
            conn.setData(key, value)

    def yazOdalar(self):
        for key, value in self.__odalar.items():
            print(key, value)

    def guncelle(self, key, value):
        # belirli bir yeri güncelle
        conn = dbConnection()
        conn.setData(key, value)

        self.__odalar[key] = value


ev = EV()
ev.yazOdalar()

# ev.guncelle("oda1", "1")
# ev.guncelle("username", "erol.uslu@bil.omu.edu.tr")
# ev.guncelle("id", "2000")
ev.kaydet()

# print("del ev")
# del ev