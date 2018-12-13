from xbee import XBee
import serial
import time

ser = serial.Serial('COM4', 9600)

ser.write("1".encode())
xbee = XBee(ser)
print("Başladık")
time.sleep(5)

while True:
    # print(xbee.wait_read_frame())
    data = xbee.wait_read_frame().get('rf_data')
    print(data)
    time.sleep(1)

xbee.halt()

ser.close()
