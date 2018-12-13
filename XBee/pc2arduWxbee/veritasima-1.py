import serial
import time
from xbee import XBee

# Open serial port
# ser = serial.Serial(PORT,BAUD_RATE)
serial_port = serial.Serial('COM4', 9600)
payload = b"Hi There 123\n"

# Continuously read and print packets
zb = XBee(serial_port)

# while True:
#     try:
#         print("send data")
#         zb.send("tx", dest_addr=b"\x00\x00", data=payload)
#         #
#         # print(zb.wait_read_frame())
#
#         time.sleep(1)
#     except KeyboardInterrupt:
#         break

for i in range(100):
    try:
        payload = str(i).encode() + b"#\n"
        print("sending")
        zb.send("tx", dest_addr=b"\x00\x00", data=payload)
        time.sleep(0.1)
    except KeyboardInterrupt:
        break

serial_port.close()
