#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Version 0.002

from pymysql import *
from Libs.ortakMethodlar import *

ayarFileAdres = "../ayar.txt"


class DbConnection:
    __hostName = ""
    __dbUsername = ""
    __dbPass = ""
    __dbName = ""
    __username = ""
    __userID = -1

    def __init__(self):
        try:
            with open(ayarFileAdres) as ayarFile:
                ayarLines = ayarFile.read()
        except Exception as err:
            errorMessage = "DbConnection __init__ : " + str(err)
            hataBas(errorMessage)
            exit(-1)

        self.__hostName = extract(ayarLines, "hostName")
        self.__dbUsername = extract(ayarLines, "dbUsername")
        self.__dbPass = extract(ayarLines, "dbPass")
        self.__dbName = extract(ayarLines, "dbName")
        self.__username = extract(ayarLines, "username")

        try:
            db = connect(host=self.__hostName, user=self.__dbUsername,
                     passwd=self.__dbPass, db=self.__dbName)
            sqlQuery = 'SELECT userID FROM USERS where username="' + self.__username + '";'

            cursor = db.cursor()
            cursor.execute(sqlQuery)
            result = cursor.fetchall()
            db.close()
        except Exception as err:
            errorMessage = "DbConnection __init__ : " + str(err)
            hataBas(errorMessage)
            exit(-1)

        if result == ():
            self.__userID = ""
        else:
            self.__userID = result[-1][-1]

    def getHostAdres(self):
        return self.__hostName

    def getDbUserName(self):
        return self.__dbUsername

    def getDbPass(self):
        return self.__dbPass

    def getDbName(self):
        return self.__dbName

    def getUserName(self):
        return self.__username

    def getUserID(self):
        return self.__userID

    def getData(self, id = ""):
        data = []
        if id == "":
            try:
                db = connect(host=self.__hostName, user=self.__dbUsername,
                                     passwd=self.__dbPass, db=self.__dbName)
                sqlQuery = 'SELECT * FROM ODALAR WHERE userID in (SELECT userID FROM USERS where username="'+ self.__username + '");'

                cursor = db.cursor()
                cursor.execute(sqlQuery)
                result = cursor.fetchall()
                db.close()
            except Exception as err:
                errorMessage = "DbConnection getData: " + str(err)
                hataBas(errorMessage)
                return -1

            for index, item in enumerate(result):
                data.append(item[1:3])
        else:
            try:
                db = connect(host=self.__hostName, user=self.__dbUsername,
                                     passwd=self.__dbPass, db=self.__dbName)
                sqlQuery = 'SELECT * FROM ODALAR WHERE userID in (SELECT userID FROM USERS where username="' + self.__username + '") AND isim like "' + str(id) + '";'

                cursor = db.cursor()
                cursor.execute(sqlQuery)
                result = cursor.fetchall()
                db.close()
            except Exception as err:
                errorMessage = "DbConnection getData: " + str(err)
                hataBas(errorMessage)
                return -1

            data.append(result[-1][1:3])

        return data

    def setData(self, item, value):
        try:
            db = connect(host=self.__hostName, user=self.__dbUsername,
                                 passwd=self.__dbPass, db=self.__dbName)
            sqlQuery = 'UPDATE ODALAR SET deger=\"' + value + '" WHERE isim LIKE "'+ item + '" and userID=' + str(self.__userID) + ';'
            cursor = db.cursor()
            cursor.execute(sqlQuery)
            db.close()
        except Exception as err:
            errorMessage = "DbConnection setData: " + str(err)
            hataBas(errorMessage)
            return -1
        return 0

    def addData(self, item, value):
        try:
            db = connect(host=self.__hostName, user=self.__dbUsername,
                                 passwd=self.__dbPass, db=self.__dbName)
            item = "\"" + item + "\""
            value = "\"" + str(value )+ "\""
            id = "\"" + str(self.__userID) + "\""

            sqlQuery = 'INSERT INTO ODALAR(isim, deger, userID) VALUES(' + item + ', ' + value + ', ' + id + ');'

            cursor = db.cursor()
            cursor.execute(sqlQuery)
            db.commit()
            db.close()
        except Exception as err:
            errorMessage = "DbConnection addData: " + str(err)
            hataBas(errorMessage)
            return -1
        return 0

    def delData(self, item):
        try:
            db = connect(host=self.__hostName, user=self.__dbUsername,
                         passwd=self.__dbPass, db=self.__dbName)

            sqlQuery = "DELETE FROM ODALAR WHERE isim='" + item + "' and userID='" + str(self.__userID) + "';"

            cursor = db.cursor()
            cursor.execute(sqlQuery)
            db.commit()
            db.close()
        except Exception as err:
            errorMessage = "DbConnection delData: " + str(err)
            hataBas(errorMessage)
            return -1
        return 0