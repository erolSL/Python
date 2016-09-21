#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Geri Sayım
'ayar.txt' dosyasından 'sure' yi alarak geri sayımı başlatır.
'ayar.txt' dosyasını bulamazsa 'log.txt' dosyasına kayıt atar.
Geri sayım bittiğinde yeni pencere oluşturur.
"""

import time
from datetime import datetime
from tkinter import *
from ctypes import *


class CalarSaat:
    __sure = 0
    __oncekiZaman = 0
    __simdiZaman = 0

    def __init__(self):
        try:
            file = open("ayar.txt", 'r')
            sure = file.readline()
            file.close()
            self.__sure = int(sure)
        except FileNotFoundError:
            try:
                errFile = open("log.txt", encoding='utf-8', mode='a')
                errMessage = "ayar.txt bulunamadı. Programdan çıkılıyor.\n"
                errFile.write("%s %s"%(datetime.now(), errMessage))
                errFile.close()
            except:
                pass
            exit()

    def calistir(self):
        self.__oncekiZaman = datetime.now()
        logFile = open("log.txt", encoding='utf-8', mode='a')
        logFile.write("%s %s saniye için çalışmaya başlanmıştır.\n" %(self.__oncekiZaman, self.__sure))
        logFile.close()
        time.sleep(self.__sure)
        self.__simdiZaman = datetime.now()
        logFile = open("log.txt", encoding='utf-8', mode='a')
        logFile.write("%s Çalışma bitmiştir.\n" %(self.__simdiZaman))
        logFile.close()

    def getSure(self):
        return self.__sure

    def getBaslangicZaman(self):
        return self.__oncekiZaman

    def getBitisZaman(self):
        return self.__simdiZaman


screen = windll.user32
windowW = 500
windowH = 300
screenW = int((screen.GetSystemMetrics(0) / 2) - (windowW / 2))
screenH = int((screen.GetSystemMetrics(1) / 2) - (windowH / 2))

str = str(windowW) + "x" + str(windowH) + "+" + str(screenW) + "+" + str(screenH)

app = Tk()
app.title("Büyük Çalışma")
app.geometry(str)
app.wm_attributes("-topmost", 1)

saat = CalarSaat()
saat.calistir()

label = Label(app, text="Süre Doldu", height=0, width=100)
button2 = Button(app, text="Quit", width=20, command=app.destroy)
label.pack()
button2.pack(side='bottom', padx=0, pady=0)

app.mainloop()

# Versiyon 4
# from tkinter import *
# import time
# from datetime import datetime
#
#
# app = Tk()
# app.title("SPIES")
# app.geometry("500x300+200+200")
#
# file = open("ayar.txt", 'r')
# sure = file.readline()
# file.close()
#
#
# oncekiZaman = datetime.now()
# print(oncekiZaman)
# print(sure)
# time.sleep(int(sure))
# simdiZaman = datetime.now()
# print(simdiZaman)
# farkZaman = simdiZaman - oncekiZaman
# print(farkZaman)
#
# label = Label(app, text="Süre Doldu", height=0, width=100)
# button2 = Button(app, text="Quit", width=20, command=app.destroy)
# label.pack()
# button2.pack(side='bottom',padx=0,pady=0)
#
# app.mainloop()


# # Versiyon 3
#
# import time
# import winsound
# from datetime import datetime
#
#
# file = open("ayar.txt", 'r')
# sure = file.readline()
# file.close()
#
# # Ses kontrol
# winsound.Beep(3000, 100)
# winsound.Beep(2500, 100)
# winsound.Beep(2000, 100)
# winsound.Beep(1000, 100)
# winsound.Beep(500, 100)
#
# oncekiZaman = datetime.now()
# print(oncekiZaman)
# print(sure)
# time.sleep(int(sure))
# simdiZaman = datetime.now()
# print(simdiZaman)
# farkZaman = simdiZaman - oncekiZaman
# print(farkZaman)
#
# # Ses kontrol
# winsound.Beep(3000, 100)
# winsound.Beep(2500, 100)
# winsound.Beep(2000, 100)
# winsound.Beep(1000, 100)
# winsound.Beep(500, 100)
#


# Versiyon 2

# import time
# import winsound
# from datetime import datetime

# Ses kontrol
# winsound.Beep(3000, 100)
# winsound.Beep(2500, 100)
# winsound.Beep(2000, 100)
# winsound.Beep(1000, 100)
# winsound.Beep(500, 100)
#
# oncekiZaman = datetime.now()
# print(oncekiZaman)
# time.sleep(60 * 60)
# simdiZaman = datetime.now()
# print(simdiZaman)
# farkZaman = simdiZaman - oncekiZaman
# print(farkZaman)
# Ses kontrol
# winsound.Beep(3000, 100)
# winsound.Beep(2500, 100)
# winsound.Beep(2000, 100)
# winsound.Beep(1000, 100)
# winsound.Beep(500, 100)


# Versiyon 1

# import time
# import winsound
# from datetime import datetime

# simdiZaman = datetime.now()
# print(simdiZaman)
#
# time.sleep(1)
#
# sonraZaman = datetime.today()
#
# print(sonraZaman)
#
# farkZaman = sonraZaman - simdiZaman
#
# print(farkZaman)
# print(farkZaman.days)
# print(farkZaman.total_seconds())
# print(farkZaman.seconds)
# print(farkZaman.microseconds)
#
# if farkZaman.total_seconds() > (1 * 60) :
#     print("Büyük")
# else:
#     print("Küçüktür")
#
# while farkZaman.total_seconds() < (1 * 60) :
#     time.sleep(1)
#     sonraZaman = datetime.today()
#     print(sonraZaman)
#     farkZaman = sonraZaman - simdiZaman
#     print(farkZaman)
