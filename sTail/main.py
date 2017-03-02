import sTailGöster
from PyQt5 import QtWidgets
from PyQt5.QtCore import  QThread, pyqtSignal, QCoreApplication, QRect
import paramiko
import logging
import select

class MyWin(sTailGöster.Ui_Form):
    def __init__(self):
        super().__init__()

        self.makineler = []
        self.ui = []
        self.threadClass = []
        self.takipKelime = ""

        textEdit_X = 10
        textEdit_Y = 120
        label_X = 10
        label_Y = 90
        label3_X = 80
        label3_Y = 90
        buf_X = 330

        _translate = QCoreApplication.translate

        with open("makineler.txt", encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            hostName, username, password, host, takipDosya = line.split(":")
            makine = {
                "hostName": hostName.strip(),
                "username": username.strip(),
                "password": password.strip(),
                "host": host.strip(),
                "takipDosya": takipDosya.strip()
            }
            ui = {
                "textedit": QtWidgets.QTextEdit(self),
                "label": QtWidgets.QLabel(self),
                "label3": QtWidgets.QLabel(self)
            }

            ui["label"].setText(_translate("Form", "Makine Adı  : "))
            ui["label3"].setText(makine["hostName"])

            ui["textedit"].setGeometry(QRect(textEdit_X, textEdit_Y, 320, 320))
            ui["textedit"].setObjectName("textEdit")
            ui["label"].setGeometry(QRect(label_X, label_Y, 65, 15))
            ui["label"].setObjectName("label")
            ui["label3"].setGeometry(QRect(label3_X, label3_Y, 65, 15))
            ui["label3"].setObjectName("label_3")

            textEdit_X += buf_X
            label_X += buf_X
            label3_X += buf_X

            self.makineler.append(makine)
            self.ui.append(ui)

        self.setGeometry(300, 300, label_X, 470)


        self.pushButton_4.clicked.connect(self.baslat)

    def goster(self, value, index):
        self.ui[index]["textedit"].append(value)

    def baslat(self):
        self.takipKelime = self.lineEdit.text()
        # if self.takipKelime == "":
        #     print("Aranacak kelime boş")
        #     return -1
        for index, item in enumerate(self.makineler):
            self.threadClass.append(MyThread(item["host"], item["username"],
                                             item["password"], self.takipKelime,
                                             item["takipDosya"], index))
            self.threadClass[index].tmp.connect(self.goster)
            self.threadClass[index].start()

class MyThread(QThread):
    tmp = pyqtSignal(['QString', int])
    def __init__(self, host, username, password, takipKelime, takipDosya, index, parent = None):
        super(MyThread, self).__init__(parent)
        self.host = host
        self.password = password
        self.username = username
        self.takipDosya = takipDosya
        self.takipKelime = takipKelime
        self.delta = 1
        self.index = index
        self.BUF_SIZE = 2048

    def mkssh_conn(self, host, username, password):
        """returns an sshconnection"""
        try:
            paramiko.util.logging.getLogger('paramiko').setLevel(logging.WARN)
            sshcon = paramiko.SSHClient()
            sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            sshcon.connect(hostname=host, username=username, password=password, timeout=5)
            return sshcon
        except Exception as err:
            print("error : " + err)
            return 0

    def run(self):
        client = self.mkssh_conn(self.host, self.username, self.password)  # returns a paramiko.SSHClient()
        transport = client.get_transport()
        transport.set_keepalive(1)
        channel = transport.open_session()
        channel.settimeout(self.delta)
        cmd = "tail -f " + self.takipDosya #+ "| grep  --line-buffered " + self.takipKelime
        channel.exec_command(cmd)
        LeftOver = ""
        while transport.is_active():
            rl, wl, xl = select.select([channel], [], [], 0.0)
            if len(rl) > 0:
                buf = channel.recv(self.BUF_SIZE).decode()
                if len(buf) > 0:
                    lines_to_process = LeftOver + buf
                    EOL = lines_to_process.rfind("\n")
                    if EOL != len(lines_to_process) - 1:
                        LeftOver = lines_to_process[EOL + 1:]
                        lines_to_process = lines_to_process[:EOL]
                    else:
                        LeftOver = ""
                    for line in lines_to_process.splitlines():
                        if "error" in line:
                            print("error : " + line)
                        self.tmp.emit(line, self.index)
        client.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWin()
    ui.show()
    sys.exit(app.exec_())


