import socket, socketserver
import threading

"""
sınıf socketserver için, handle fonk veri gönderme ve alma için fonksiyon(lar),
    veriyi almalı, çözmeli, işlemeli
(gerekirse) socket içinde bir sınıf, veri gönderme ve alma için fonksiyon(lar),
veri düzenleme için ayrı bir fonksiyon,
socket ve socketserver için threat açılacak
"""

host = "0.0.0.0"
port = 6666
alinanVeri = ""

def sifrele(veri):
    return veri

def coz(veri):
    return veri

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        global alinanVeri
        data = ""
        while True:
            tmp = coz(self.request.recv(1024).decode())
            if not tmp:
                break
            data += tmp
        alinanVeri += data

def dataGet():
    global alinanVeri
    data = alinanVeri
    alinanVeri = ""
    return data

def dataSend(veri):
    sended = True
    try:
        conn = socket.create_connection((host, port))
        conn.sendall(sifrele(veri).encode())
    except Exception as err:
        print(str(err))
        sended = False
    finally:
        conn.close()
        return sended

def main():
    try:
        server = socketserver.ThreadingTCPServer((host, port), ThreadedTCPRequestHandler)
        serverThread = threading.Thread(target = server.serve_forever)
        serverThread.daemon = True
        serverThread.start()
    except Exception as error:
        print(str(error))
        return


if __name__ == "__main__":
    main()