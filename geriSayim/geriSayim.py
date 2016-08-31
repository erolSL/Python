#!/usr/bin/python
# -*- coding: utf-8 -*-

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
                errFile.write(errMessage)
                errFile.close()
            except:
                pass
            exit()

    def calistir(self):
        self.__oncekiZaman = datetime.now()
        time.sleep(self.__sure)
        self.__simdiZaman = datetime.now()

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
app.title("SPIES")
app.geometry(str)
app.wm_attributes("-topmost", 1)

saat = CalarSaat()
print("Çalışmaya başlanmıştır.")
saat.calistir()
print("Çalışma bitmiştir.")

label = Label(app, text="Süre Doldu", height=0, width=100)
button2 = Button(app, text="Quit", width=20, command=app.destroy)
label.pack()
button2.pack(side='bottom', padx=0, pady=0)

app.mainloop()
