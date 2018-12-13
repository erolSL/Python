import serial
from datetime import datetime
import time
from xbee import XBee
import sqlite3

# Open serial port
# ser = serial.Serial(PORT,BAUD_RATE)
serial_port = serial.Serial('COM4', 9600)

# Continuously read and print packets
zb = XBee(serial_port)
baglanti = sqlite3.connect('veriler.db')


def main():
    global baglanti, zb
    dbcursor = baglanti.cursor()

    for i in range(100):
        try:
            print("Sending : ")
            if i % 2 == 1:
                print("1")
                payload = str(1).encode()
                zb.send("tx", dest_addr=b"\x00\x00", data=payload)
                data = zb.wait_read_frame().get('rf_data').decode().strip()[:4]
                print(data)
                now = datetime.now().strftime("%d %b %Y %H:%M:%S")
                sqlQuery = "INSERT INTO veriler(zaman, islem, sonuc) VALUES('" + now + "', '1', '" + data + "');"
                dbcursor.execute(sqlQuery)
                baglanti.commit()
            if i % 2 == 0:
                print("2")
                payload = str(2).encode()
                zb.send("tx", dest_addr=b"\x00\x00", data=payload)
                data = zb.wait_read_frame().get('rf_data').decode()[:4]
                print(data)
                now = datetime.now().strftime("%d %b %Y %H:%M:%S")
                sqlQuery = "INSERT INTO veriler(zaman, islem, sonuc) VALUES('" + now + "', '2', '" + data + "');"
                dbcursor.execute(sqlQuery)
                baglanti.commit()

        except KeyboardInterrupt:
            break
        time.sleep(3)


    baglanti.close()


if __name__ == "__main__":
    main()

serial_port.close()
