from pymysql import *

ayarFileAdres = "ayar.txt"

Attributes = [
    "hostName",
    "dbUsername",
    "dbPass",
    "dbName",
    "username"
]

class DbConnection:
    __hostName = ""
    __dbUsername = ""
    __dbPass = ""
    __dbName = ""
    __username = ""
    __userID = -1


    def __init__(self):
        with open(ayarFileAdres) as ayarFile:
            ayarLines = ayarFile.read()

        self.__hostName = self.extract(ayarLines, "hostName")
        self.__dbUsername = self.extract(ayarLines, "dbUsername")
        self.__dbPass = self.extract(ayarLines, "dbPass")
        self.__dbName = self.extract(ayarLines, "dbName")
        self.__username = self.extract(ayarLines, "username")

        try:
            db = connect(host=self.__hostName, user=self.__dbUsername,
                     passwd=self.__dbPass, db=self.__dbName)
            sqlQuery = "SELECT userID FROM USERS where username=\"" + self.__username + "\";"

            cursor = db.cursor()
            cursor.execute(sqlQuery)
            result = cursor.fetchall()
            db.close()
        except  Exception as err:
            print(err)

    def extract(self, text, marker):
        endSymbol = '\n'
        return [item.split(endSymbol)[0]
                for item in text.split(marker + ":")[1:]][0]



de = DbConnection()
de.getAtributes()


# import _mysql
#
# db=_mysql.connect(host="localhost",user="root",
#                   passwd="1",db="debe")

# import pymysql
# import sqlite3

# ayarDosya = "ayar.txt"
# hostName = ""
# dbuserName = ""
# password = ""
# dbName = ""
# username = "erol.uslu"
# userid = "1"
# id = "oda2"
#
# ayarFile = open(ayarDosya, "r")
# lines = ayarFile.readlines()
# ayarFile.close()
#
# for index, item in enumerate(lines):
#     item = item.strip()
#     if "dbAdres" in item:
#         hostName = item.split(":")[1]
#     elif "dbUsername" in item:
#         dbuserName = item.split(":")[1]
#     elif "dbPass" in item:
#         password = item.split(":")[1]
#     elif "dbName" in item:
#         dbName = item.split(":")[1]
#     elif "username" in item:
#         username = item.split(":")[1]
#
# print("Hostname : ", hostName)
# print("dbusername : ", dbuserName)
# print("password : ", password)
# print("dbname : ", dbName)
# print("username : ", username)
#
# db = pymysql.connect(host=hostName,
#                      user=dbuserName,
#                      passwd=password,
#                      db=dbName)
#
# sqlQuery = "SELECT * FROM odalar WHERE userID in (SELECT userID FROM USERS where username='" + username + "');"
# cursor = db.cursor()
# cursor.execute(sqlQuery)
# # db.commit()
# result = cursor.fetchall()
# db.close()
# #
# print(result)
#
#
# db = sqlite3.connect("DB/vt.sqlite")
# adres = "0000"
# cursor = db.cursor()
# sqlQuery = ""
#
# for i in result:
#     item = i[1]
#     value = i[2]
#     # sqlQuery = "INSERT INTO odalar(isim, deger, adres) VALUES('" + item + "', '" + value + "', '" + adres + "');"
#     cursor.execute(sqlQuery)
#
#
# db.commit()
# db.close()
#


# print(result[-1][-1])

# data = []
#
# for index, item in enumerate(result):
#     # print(item)
#     data.append(item[1:3])
#
# for index, item in enumerate(data):
#     print(item)