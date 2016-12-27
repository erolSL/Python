# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(414, 338)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(160, 38, 131, 24))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setPlainText("__:__:__")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 40, 31, 21))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 180, 71, 61))

        font = QtGui.QFont()
        font.setPointSize(44)

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(180, 180, 71, 61))

        font = QtGui.QFont()
        font.setPointSize(44)

        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(280, 180, 71, 61))

        font = QtGui.QFont()
        font.setPointSize(44)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(150, 180, 21, 61))

        font = QtGui.QFont()
        font.setPointSize(44)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(250, 180, 21, 61))

        font = QtGui.QFont()
        font.setPointSize(44)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(100, 260, 41, 21))

        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(190, 260, 61, 21))

        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(290, 260, 61, 21))

        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(30, 290, 351, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Geri Sayıcı"))
        self.label.setText(_translate("Form", "Süre : "))
        self.pushButton.setText(_translate("Form", "Başlat"))
        self.pushButton_2.setText(_translate("Form", "Sıfırla"))
        self.label_2.setText(_translate("Form", "00"))
        self.label_3.setText(_translate("Form", "00"))
        self.label_4.setText(_translate("Form", "00"))
        self.label_5.setText(_translate("Form", ":"))
        self.label_6.setText(_translate("Form", ":"))
        self.label_7.setText(_translate("Form", "SAAT"))
        self.label_8.setText(_translate("Form", "DAKİKA"))
        self.label_9.setText(_translate("Form", "SANİYE"))

    def changeText(self):
        self.plainTextEdit.setPlainText("")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

