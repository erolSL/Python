import serial
from datetime import datetime
import time

from xbee import XBee
import sqlite3
import _thread

# Open serial port
# ser = serial.Serial(PORT,BAUD_RATE)
serial_port = serial.Serial('COM4', 9600)

# Continuously read and print packets
zb = XBee(serial_port)




def readData():
    global zb
    baglanti = sqlite3.connect('veriler.db')
    dbcursor = baglanti.cursor()
    while True:
        try:
            data = zb.wait_read_frame().get('rf_data').decode()
            print(data)
            prosesNo, sonuc = data.split(";")
            prosesNo = prosesNo.strip()
            sonuc = sonuc[:4]
            now = datetime.now().strftime("%d %b %Y %H:%M:%S")
            sqlQuery = "UPDATE veriler " + \
                       "SET sonuc='" + sonuc + "'," +\
                       "durum='tamamlandı', " +\
                       "zaman='" + now + "' "\
                       "WHERE ID=" + prosesNo + ";"
            dbcursor.execute(sqlQuery)
            baglanti.commit()
        except Exception as exp:
            print(exp)

    baglanti.close()


def main():
    global zb
    _thread.start_new_thread(readData, ())
    baglanti = sqlite3.connect('veriler.db')
    dbcursor = baglanti.cursor()
    i = 0
    while True:
        try:
            islem = str((i % 2) + 1)
            print("Sending : " + islem)
            now = datetime.now().strftime("%d %b %Y %H:%M:%S")
            sqlQuery = "INSERT INTO " + \
                       "veriler(zaman, islem, sonuc, durum) " + \
                       "VALUES('" + now + "', '" + islem + "', NULL, 'devam ediyor');"
            dbcursor.execute(sqlQuery)
            sqlQuery = "SELECT ID FROM veriler ORDER BY ID DESC  LIMIT 1"
            queryId = dbcursor.execute(sqlQuery).fetchall()[0][0]
            baglanti.commit()
            data = str(queryId) + ";" + islem + ";0"
            print(data)
            payload = data.encode()
            zb.send("tx", dest_addr=b"\x00\x00", data=payload)
        except Exception as exp:
            print(exp)

        i += 1
        time.sleep(3)
    baglanti.close()


if __name__ == "__main__":
    main()

serial_port.close()
