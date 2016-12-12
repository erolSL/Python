#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 0.002

from Model.dbConnection import DbConnection
from Model.sqLiteConnection import SqlLite

ayarFileAdres = "../ayar.txt"

class EV:
    __odalar = {}
    __id = "-1"
    __username = ""

    def __init__(self):
        conn = DbConnection()
        self.__id = conn.getUserID()
        self.yukle()

    def yukle(self):
        conn = SqlLite()
        lines = conn.getData()

        if lines == "":
            conn = DbConnection()
            lines = conn.getData()

        for index, item  in enumerate(lines):
            self.__odalar[item[0]] = item[1]

    def kaydet(self):
        # belllekteki veriler veritabanına aktarılır.
        conndb = DbConnection()
        connsqlite = SqlLite()

        for key, value in self.__odalar.items():
            conndb.setData(key, value)
            connsqlite.setData(key, value)

    def yazOdalar(self):
        for key, value in self.__odalar.items():
            print(key, value)

    def guncelleOda(self, key = "", value = "", adres = ""):
        # belirli bir yeri güncelle
        conndb = DbConnection()
        connsqlite = SqlLite()

        if value != "":
            conndb.setData(key, value)
            connsqlite.setData(key, value)
            self.__odalar[key] = value
        if adres != "":
            connsqlite.setData(key, adres=adres)


    def ekleOda(self, key, value, adres):
        conndb = DbConnection()
        connsqlite = SqlLite()

        conndb.addData(key, value)
        connsqlite.addData(key, value, adres)
        self.__odalar[key] = value

    def silOda(self, key):
        conndb = DbConnection()
        connsqlite = SqlLite()

        conndb.delData(key)
        connsqlite.delData(key)
        self.__odalar.pop(key)

    def getSenkron(self):
        pass


ev = EV()
# ev.guncelleOda()
ev.yazOdalar()
# print("-------------------")
# ev.ekleOda("oda100", 100, "0000")
# ev.yazOdalar()
# print("-------------------")
# ev.silOda("oda100")
# ev.yazOdalar()

# ev.guncelle("oda1", "1")
# ev.guncelle("username", "erol.uslu@bil.omu.edu.tr")
# ev.guncelle("id", "2000")
# ev.kaydet()

# print("del ev")
# del ev