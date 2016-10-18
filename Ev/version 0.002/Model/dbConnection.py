# Version 0.002
from Libs.ortakMethodlar import *
import MySQLdb

ayarFileAdres = "../ayar.txt"

class dbConnection:
    __hostName = ""
    __dbUsername = ""
    __password = ""
    __dbName = ""
    __userName = ""
    __userID = -1

    def __init__(self):
        ayarFile = open(ayarFileAdres, "r")
        lines = ayarFile.readlines()
        ayarFile.close()

        for index, item in enumerate(lines):
            item = item.strip()
            if "dbAdres" in item:
                self.__hostName = item.split(":")[1]
            elif "dbUsername" in item:
                self.__dbUsername = item.split(":")[1]
            elif "dbPass" in item:
                self.__password = item.split(":")[1]
            elif "dbName" in item:
                self.__dbName = item.split(":")[1]
            elif "username" in item:
                self.__userName = item.split(":")[1]

        db = MySQLdb.connect(host=self.__hostName, user=self.__dbUsername,
                             passwd=self.__password, db=self.__dbName)

        sqlQuery = "SELECT userID FROM USERS where username=\"" + self.__userName + "\";"

        cursor = db.cursor()
        cursor.execute(sqlQuery)

        result = cursor.fetchall()
        db.close()
        self.__userID = result[-1][-1]



    def getUserName(self):
        return self.__userName

    def getDbUserName(self):
        return self.__dbUsername

    def getHostAdres(self):
        return self.__hostName

    def getPasswd(self):
        return self.__password

    def getDbName(self):
        return self.__dbName

    def getUserID(self):
        return self.__userID

    # def __del__(self):
    #     pass

    def getData(self, id = ""):
        data = []
        if id == "":
            db = MySQLdb.connect(host=self.__hostName, user=self.__dbUsername,
                                 passwd=self.__password, db=self.__dbName)

            sqlQuery = "SELECT * FROM ODALAR WHERE userID in (SELECT userID FROM USERS where username=\"" + self.__userName + "\");"

            cursor = db.cursor()
            cursor.execute(sqlQuery)
            result = cursor.fetchall()
            db.close()

            for index, item in enumerate(result):
                data.append(item[1:3])

        else:
            db = MySQLdb.connect(host=self.__hostName, user=self.__dbUsername,
                                 passwd=self.__password, db=self.__dbName)

            sqlQuery = "SELECT * FROM ODALAR WHERE userID in (SELECT userID FROM USERS where username=\"" + self.__userName + "\") AND isim like \"" + id + "\";"

            cursor = db.cursor()
            cursor.execute(sqlQuery)
            result = cursor.fetchall()
            db.close()

            data.append(result[-1][1:3])

        return data

    def setData(self, item, value):
        db = MySQLdb.connect(host=self.__hostName, user=self.__dbUsername,
                             passwd=self.__password, db=self.__dbName)

        sqlQuery = "UPDATE ODALAR SET deger=\"" + value + "\" WHERE isim LIKE \"" + item + "\" and userID=" + str(self.__userID) + ";"

        cursor = db.cursor()
        cursor.execute(sqlQuery)
        db.commit()

        result = cursor.fetchall()

        db.close()


    def addData(self, item, value):
        db = MySQLdb.connect(host=self.__hostName, user=self.__dbUsername,
                             passwd=self.__password, db=self.__dbName)

        item = "\"" + item + "\""
        value = "\"" + str(value )+ "\""
        id = "\"" + str(self.__userID) + "\""

        sqlQuery = "INSERT INTO ODALAR(isim, deger, userID) VALUES(" + item + ", " + value + ", " + id + ");"

        cursor = db.cursor()
        cursor.execute(sqlQuery)
        db.commit()

        result = cursor.fetchall()

        db.close()



db = dbConnection()

print("Hostname : ", db.getHostAdres())
print("dbname : ", db.getDbName())
print("dbusername : ", db.getDbUserName())
print("dbpassword : ", db.getPasswd())
print("username : ", db.getUserName())
print("UserID : ", db.getUserID())

# db.setData("oda1", "erol")
# db.addData("oda8", 8)

# for item in db.getData("oda6"):
#     print(item)
