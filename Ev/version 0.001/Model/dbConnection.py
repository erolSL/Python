# Version 0.002

import sys
sys.path.insert(0, "~/Masaüstü/Projeler/Ev/Libs/")
print(sys.path)

from ortakMethodlar import *

ayarFileAdres = "../ayar.txt"

class dbConnection:
    __adres = ""
    __username = None
    __passwd = None

    def __init__(self):
        dbFile = open(ayarFileAdres, "r")
        lines = dbFile.readlines()
        dbFile.close()
        for item in lines:
            item = item.strip()
            if "dbAdres" in item:
                self.__adres = item.split(":")[1]

    def getAdres(self):
        return self.__adres

    # def __del__(self):
    #     pass

    def getData(self, id = ""):
        data = ""
        nData = []
        if id == "":
            dbFile = open(self.__adres, "r")
            data = dbFile.readlines()
            dbFile.close()
            for item in data:
                nData.append(item.strip())
            data = nData
        else:
            dbFile = open(self.__adres, "r")
            lines = dbFile.readlines()
            dbFile.close()

            id = str(id)

            for index, item in enumerate(lines):
                item = item.strip()
                if ("id:" + id) in item:
                    data = item

        return data

    def setData(self, id, item, mode):
        if mode == "u":
            dbFile = open(self.__adres, "r")
            lines = dbFile.readlines()
            dbFile.close()

            for index, lItem in enumerate(lines):
                if ("id:" + id) in lItem:
                    lines[index] = item

            dbFile = open(self.__adres, "w")
            for items in lines:
                dbFile.write(items)
            dbFile.close()
        elif mode == "a":
            dbFile = open(self.__adres, "a")
            dbFile.write(item)
            dbFile.close()
        else:
            hataBas("dbConnection.setData : Hatalı mode. %s" %(mode))



# db = dataConnection()
# print(db.getData(1))
# print(db.getAdres())