# import _mysql
#
# db=_mysql.connect(host="localhost",user="root",
#                   passwd="1",db="debe")

import MySQLdb

db = MySQLdb.connect(host="localhost",user="root",
                  passwd="1",db="debe")

cursor = db.cursor()
cursor.execute("SELECT * FROM users")

result = cursor.fetchall()

print(result)



