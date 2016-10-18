# import _mysql
#
# db=_mysql.connect(host="localhost",user="root",
#                   passwd="1",db="debe")

import MySQLdb

ayarDosya = "ayar.txt"
hostName = ""
dbuserName = ""
password = ""
dbName = ""
username = "erol.uslu"
userid = "1"
id = "oda1"

ayarFile = open(ayarDosya, "r")
lines = ayarFile.readlines()
ayarFile.close()

for index, item in enumerate(lines):
    item = item.strip()
    if "dbAdres" in item:
        hostName = item.split(":")[1]
    elif "dbUsername" in item:
        dbuserName = item.split(":")[1]
    elif "dbPass" in item:
        password = item.split(":")[1]
    elif "dbName" in item:
        dbName = item.split(":")[1]
    elif "username" in item:
        username = item.split(":")[1]

print("Hostname : ", hostName)
print("username : ", dbuserName)
print("password : ", password)
print("dbname : ", dbName)
print("dbname : ", username)

db = MySQLdb.connect(host=hostName,user=dbuserName,
                  passwd=password,db=dbName)

# sqlQuery = "SELECT * FROM ODALAR WHERE userID in (SELECT userID FROM USERS where username=\"" + username + "\") AND isim like \"" + id + "\";"
sqlQuery = "UPDATE ODALAR SET deger=\"uslu\" WHERE isim LIKE \"" + id + "\" and userID=" + userid + ";"

cursor = db.cursor()
cursor.execute(sqlQuery)
db.commit()

result = cursor.fetchall()

db.close()

print(result)

# print(result[-1][-1])

# data = []
#
# for index, item in enumerate(result):
#     # print(item)
#     data.append(item[1:3])
#
# for index, item in enumerate(data):
#     print(item)
