CREATE TABLE veriler(
    ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    zaman DATETIME,
    islem VARCHAR(20),
    sonuc VARCHAR(20)
)

"INSERT INTO veriler(zaman, process, result) VALUES('', '2', 'sccs');"


INSERT INTO veriler(zaman, process, result) VALUES('07 Dec 2018 16:47:52', '2', 'sccs');