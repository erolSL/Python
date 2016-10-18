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
            if "id:" in i:
                self.__id = i.split(":")[1]
            elif "username" in i:
                self.__username = i.split(":")[1]
        if self.__id == "-1":
            self.olustur()
        else:
            self.yukle()

    def __del__(self):
        # belllekteki veriler veritabanına aktarılır.
        conn = dbConnection()

        satir = "id:" + self.__id + ";" + "username:" + self.__username
        for key, value in self.__odalar.items():
            satir += ";" + key + ":" + str(value)
        satir += "\n"

        conn.setData(self.__id, satir, "u")

    def yukle(self):
        # Veri tabanından veriler yüklenir.
        conn = dbConnection()
        lines = conn.getData()

        for i in lines:
            i = i.strip()
            if ("id:" + self.__id) in i:
                for j in i.split(";"):
                    key, value = j.split(":")
                    if key == "id":
                        pass
                    elif key == "username":
                        self.__username = value
                    else:
                        self.__odalar[key] = value

    def olustur(self):
        conn = dbConnection()
        lines = conn.getData()

        self.__id = str(len(lines) + 1)
        self.__username = "erol.uslu@bil.omu.edu.tr"
        self.__odalar = {}

        satir = "id:" + self.__id + ";" + "username:" + self.__username

        for key, value in self.__odalar.items():
            satir += ";" + key + ":" + str(value)

        satir += "\n"

        conn.setData(self.__id, satir, "a")


    def kaydet(self):
        # belllekteki veriler veritabanına aktarılır.
        conn = dbConnection()

        satir = "id:" + self.__id + ";" + "username:" + self.__username
        for key, value in self.__odalar.items():
            satir += ";" + key + ":" + str(value)
        satir += "\n"

        conn.setData(self.__id, satir, "u")


    def yazOdalar(self):
        for key, value in self.__odalar.items():
            print(key, value)

    def guncelle(self, key, value):
        # belirli bir yeri güncelle
        conn = dbConnection()
        line = conn.getData(self.__id)

        nLine = ""
        degistiAyar = False

        if key == "id":
            hataBas("\"id\" değiştirilemez")
            return
        elif key == "username":
            self.__username = value
            degistiAyar = True
        else:
            self.__odalar[key] = value

        for item in line.split(";"):
            if (key + ":" ) in item:
                data = key + ":" + value
                nLine += data + ";"
            else:
                nLine += item + ";"
        nLine += "\n"
        conn.setData(self.__id, nLine, "u")

        if degistiAyar:
            ayarDosya = open(ayarFileAdres, "r")
            okuSatirlar = ayarDosya.readlines()
            ayarDosya.close()

            for index, item in enumerate(okuSatirlar):
                if (key + ":") in item:
                    okuSatirlar[index] = (key + ":" + value + "\n")

            ayarDosya = open(ayarFileAdres, "w")
            for index, item in enumerate(okuSatirlar):
                ayarDosya.write(okuSatirlar[index])
            ayarDosya.close()



ev = EV()
# ev.yazOdalar()
# ev.kaydet()

# ev.guncelle("username", "erol.uslu@bil.omu.edu.tr")
# ev.guncelle("id", "2000")

# print("del ev")
del ev