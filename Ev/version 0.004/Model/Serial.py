import serial

seri = serial.Serial()
seri.baudrate = 9600
seri.port = 'COM2'

if seri.isOpen():
    print("buradayım")
else:
    print("hayır buradayım")
# seri.write("deneme")
seri.close()

#
# import serial
# ser = 0
#
# # Function to Initialize the Serial Port
# def init_serial():
#     global ser  # Must be declared in Each Function
#     ser = serial.Serial()
#     ser.baudrate = 9600
#     ser.port = "COM3"  # COM Port Name Start from 0
#
#     ser.timeout = 1
#     ser.open()  # Opens SerialPort
#
#     # print port open or closed
#     if ser.isOpen():
#         print('Open: ' + ser.portstr)
#     else:
#         print("Açılmadı")
#
#
# # Function Ends Here


# Call the Serial Initilization Function, Main Program Starts from here
# init_serial()

# temp = input('Type what you want to send, hit enter:\r\n')
# ser.write(temp)  # Writes to the SerialPort
#
# while 1:
#     bytes = ser.readline()  # Read from Serial Port
#     print
#     'You sent: ' + bytes  # Print What is Read from Port

# Ctrl+C to Close Python Window
