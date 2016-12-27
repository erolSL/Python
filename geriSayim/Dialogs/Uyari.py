from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect, Qt, QCoreApplication

class Uyari(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 415, 300)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.uyari = QLabel(self)
        self.uyari.setObjectName("label")
        self.uyari.setGeometry(QRect(90, 60, 251, 51))
        self.uyari.setObjectName("uyariMesaji")
        self.uyari.setText("Süre Doldu.")

        font = QFont()
        font.setPointSize(30)
        self.uyari.setFont(font)

        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(160, 200, 101, 21))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Çıkış")
        # self.pushButton.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton.clicked.connect(self.done(0))

        self.show()
