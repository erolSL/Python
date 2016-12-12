#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from Libs.ortakMethodlar import *

class SqlLite:
    __adress = "../DB/vt.sqlite"

    # def __init__(self):
    #     pass

    def getAdres(self):
        return self.__adress

    def getData(self, id = ''):
        try:
            conn = sqlite3.connect(self.__adress)
            im = conn.cursor()
            veri = []
            data = []

            if id == "":
                im.execute("SELECT * FROM ODALAR;")
                veri = im.fetchall()
                conn.close()

                for index, item in enumerate(veri):
                    data.append(item[1:4])
            else:
                im.execute("SELECT * FROM ODALAR where isim='" + id + "';")
                veri = im.fetchall()
                conn.close()
                data = veri[1:4]
        except Exception as inst:
            hataBas("SqlLite.getData(): " + str(inst))
            return ""

        return data

    def setData(self, item = "", value = "", adres = ""):

        db = sqlite3.connect(self.__adress)
        if adres == "":
            sqlQuery = "UPDATE ODALAR SET deger=\"" + value + "\" WHERE isim LIKE \"" + item
            cursor = db.cursor()
            cursor.execute(sqlQuery)
        else:
            sqlQuery = "UPDATE ODALAR SET adres=\"" + value + "\" WHERE isim LIKE \"" + item
            cursor = db.cursor()
            cursor.execute(sqlQuery)
        db.commit()
        db.close()

    def addData(self, item, value, adres):
        db = sqlite3.connect(self.__adress)

        value = str(value)

        sqlQuery = "INSERT INTO odalar(isim, deger, adres) VALUES('" + item + "', '" + value + "', '" + adres + "');"

        cursor = db.cursor()
        cursor.execute(sqlQuery)
        db.commit()
        db.close()

    def delData(self, item):
        db = sqlite3.connect(self.__adress)

        sqlQuery = "DELETE FROM odalar WHERE isim=\"" + item + "\""

        cursor = db.cursor()
        cursor.execute(sqlQuery)
        db.commit()
        db.close()


# conn = SqlLite()
# conn.setData("", adres="123123")
# conn.addData("oda1", "1", "12345")
# conn.delData("oda100")
# print(conn.getData())