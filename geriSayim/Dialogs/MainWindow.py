import sys
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect, Qt, QTimer
from v7.Dialogs.Uyari import Uyari
import re


pngAdres = "clock.png"
title = "Geri Sayım"
defaultTime = "__:__:__"

class MainWindow(QWidget):
    __pressBaslat = False
    __timeStr = ""
    __top_zaman = 0

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(300, 300, 415, 400)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(pngAdres))

        self.label = QLabel(self)
        self.label.setGeometry(QRect(155, 40, 30, 21))
        self.label.setObjectName("label")
        self.label.setText("Süre : ")

        self.plainTextEdit = LineEdit(self)
        self.plainTextEdit.deselect()

        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(100, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Başlat")

        self.pushButton2 = QPushButton(self)
        self.pushButton2.setGeometry(QRect(260, 120, 75, 23))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.setText("Sıfırla")

        self.pushButton.clicked.connect(self.baslat)
        self.pushButton2.clicked.connect(self.sifirla)

        font = QFont()
        font.setPointSize(44)

        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(80, 180, 71, 61))
        self.label_2.setObjectName("label_2")

        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QRect(180, 180, 71, 61))
        self.label_3.setObjectName("label_3")

        self.label_4 = QLabel(self)
        self.label_4.setGeometry(QRect(280, 180, 71, 61))
        self.label_4.setObjectName("label_4")

        self.label_2.setText("00")
        self.label_3.setText("00")
        self.label_4.setText("00")

        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.label_4.setFont(font)

        self.label_5 = QLabel(self)
        self.label_5.setGeometry(QRect(150, 180, 21, 61))
        self.label_5.setObjectName("label_5")

        self.label_6 = QLabel(self)
        self.label_6.setGeometry(QRect(250, 180, 21, 61))
        self.label_6.setObjectName("label_6")

        self.label_5.setText(":")
        self.label_6.setText(":")

        self.label_5.setFont(font)
        self.label_6.setFont(font)

        font2 = QFont()
        font2.setPointSize(11)

        self.label_7 = QLabel(self)
        self.label_7.setGeometry(QRect(95, 260, 41, 21))
        self.label_7.setFont(font2)
        self.label_7.setObjectName("label_7")

        self.label_8 = QLabel(self)
        self.label_8.setGeometry(QRect(187, 260, 61, 21))
        self.label_8.setFont(font2)
        self.label_8.setObjectName("label_8")

        self.label_9 = QLabel(self)
        self.label_9.setGeometry(QRect(287, 260, 61, 21))
        self.label_9.setFont(font2)
        self.label_9.setObjectName("label_9")

        self.label_7.setText("SAAT")
        self.label_8.setText("DAKİKA")
        self.label_9.setText("SANİYE")

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(QRect(33, 320, 350, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setRange(0, 100)
        self.progressBar.setValue(0)

        self.show()

    def getTime(self):
        return self.plainTextEdit.text()

    def baslat(self):
        if self.__pressBaslat:
            # Zaman duraklatıldı
            self.pushButton.setText("Başlat")
            self.__pressBaslat = False
            self.timer.stop()
        else:
            # Zaman başlatıldı
            self.pushButton.setText("Duraklat")
            self.__pressBaslat = True
            if self.__timeStr == "":
                self.__timeStr = self.getTime()
                self.timer = QTimer()
                self.timer.setInterval(1000)
                self.timer.timeout.connect(self.geriSayim)

                hour, min, sec = self.plainTextEdit.text().split(":")
                self.__top_zaman = int(hour) * 3600 + int(min) * 60 + int(sec)
            self.timer.start()

        self.geriSayim()

    def geriSayim(self):
        hour, min, sec = self.__timeStr.split(":")
        kalan_zaman = int(hour) * 3600 + int(min) * 60 + int(sec)
        if self.__timeStr == "00:00:00":
            self.timer.stop()
            self.label_2.setText(hour)
            self.label_3.setText(min)
            self.label_4.setText(sec)
            self.uyari = Uyari()
            self.pushButton.setText("Başlat")
            self.__pressBaslat = False
            self.timer.deleteLater()
        self.label_2.setText(hour)
        self.label_3.setText(min)
        self.label_4.setText(sec)

        bitenZaman = self.__top_zaman - kalan_zaman
        oran = int((bitenZaman / self.__top_zaman) * 100)
        self.progressBar.setValue(oran)

        sec = str(int(sec) - 1)
        if sec == "-1":
            min = str(int(min) - 1)
            sec = "59"
        if min == "-1":
            hour = str(int(hour) - 1)
            min = "59"
        if len(sec) == 1:
            sec = "0" + sec
        if len(min) == 1:
            min = "0" + min
        if len(hour) == 1:
            hour = "0" + hour
        self.__timeStr = hour + ":" + min + ":" + sec

    def sifirla(self):
        self.pushButton.setText("Başlat")
        self.__pressBaslat = False
        self.timer.stop()
        self.label_2.setText("00")
        self.label_3.setText("00")
        self.label_4.setText("00")
        self.progressBar.setValue(0)
        self.__timeStr = ""

class LineEdit(QLineEdit):
    __basildi = False
    def __init__(self, pencere):
        super().__init__(pencere)
        self.setGeometry(QRect(195, 38, 60, 24))
        self.setObjectName("plainTextEdit")
        self.setText(defaultTime)
        self.textChanged.connect(self.duzenle)
        self.setMaxLength(8)

    def mousePressEvent(self, event):
        if not self.__basildi:
            if event.button() == Qt.LeftButton:
                self.setText("")
                self.__basildi = True

    def duzenle(self):
        text = self.text()
        if "__:__:__" in text:
            self.setText(text.replace("__:__:__", ""))

        harf = re.search(r"[a-z]", text)
        if harf:
            QMessageBox.critical(self, "Uyarı", "Lütfen rakam giriniz.")
            text = text.replace(harf.group(), "")
            self.setText(text)
        if len(text) == 3:
            text = text[:2] + ":" + text[-1]
            self.setText(text)
        if len(text) == 6:
            text = text[:5] + ":" + text[-1]
            self.setText(text)
