# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets

class Ui_Form(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setGeometry(300, 300, 397, 359)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 50, 64, 16))
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(QtCore.QRect(75, 50, 64, 16))
        self.label2.setObjectName("label2")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(10, 80, 101, 271))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(310, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 20, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 20, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Göster"))
        self.label.setText(_translate("Form", "Makine Adı  : "))
        self.label2.setText(_translate("Form", ""))
        self.pushButton.setText(_translate("Form", "Kaydet ve Çık"))
        self.pushButton_2.setText(_translate("Form", "Çık"))
        self.pushButton_3.setText(_translate("Form", "Kaydet"))
        self.pushButton_4.setText(_translate("Form", "Başlat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())
