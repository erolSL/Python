import serial
import time
from xbee import XBee

# Open serial port
# ser = serial.Serial(PORT,BAUD_RATE)
serial_port = serial.Serial('COM4', 9600)

# Continuously read and print packets
zb = XBee(serial_port)

for i in range(100):
    try:
        time.sleep(5)
        print("Sending : ")
        if i % 2 == 1:
            print("1")
            payload = str(1).encode()
            zb.send("tx", dest_addr=b"\x00\x00", data=payload)
            data = zb.wait_read_frame().get('rf_data')
            print(data.decode())
        if i % 2 == 0:
            print("2")
            payload = str(2).encode()
            zb.send("tx", dest_addr=b"\x00\x00", data=payload)
            data = zb.wait_read_frame().get('rf_data')
            print(data.decode())
    except KeyboardInterrupt:
        break


serial_port.close()
