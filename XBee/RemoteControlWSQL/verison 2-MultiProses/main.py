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
    baglanti = sqlite3.connect('veriler.db')
    dbcursor = baglanti.cursor()
    while True:
        try:
            data = zb.wait_read_frame().get('rf_data').decode().strip()
            print(data)
            if data == "sccs":
                islem = "2"
            else:
                islem = "1"
            now = datetime.now().strftime("%d %b %Y %H:%M:%S")
            sqlQuery = "INSERT INTO " + \
                       "veriler(zaman, islem, sonuc) " + \
                       "VALUES('" + now + "', '" + islem + "', '" + data + "');"
            dbcursor.execute(sqlQuery)
            baglanti.commit()
        except Exception as exp:
            print(exp)


def main():
    global zb

    _thread.start_new_thread(readData, ())

    for i in range(100):
        try:
            print("Sending : ")
            if i % 2 == 1:
                print("1")
                payload = str(1).encode()
                zb.send("tx", dest_addr=b"\x00\x00", data=payload)
            if i % 2 == 0:
                print("2")
                payload = str(2).encode()
                zb.send("tx", dest_addr=b"\x00\x00", data=payload)

        except KeyboardInterrupt:
            break
        time.sleep(3)



if __name__ == "__main__":
    main()

serial_port.close()
