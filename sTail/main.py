# -*- coding: utf-8 -*-

import stail
import sTailGöster
from PyQt5 import QtWidgets
import paramiko
import logging
import select
import time

class MyWin(sTailGöster.Ui_Form):
    def __init__(self):
        super().__init__()
        self.machineName = "db"
        self.username = "oracle"
        self.password = "1"
        self.host = "192.168.10.21"
        self.takipDosya = "deneme"
        self.takipKelime = "1"
        self.delta = 1
        self.BUF_SIZE = 1024

        self.label2.setText(self.machineName)
        self.pushButton_4.clicked.connect(self.goster)

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

    def goster(self):
        client = self.mkssh_conn(self.host, self.username, self.password)  # returns a paramiko.SSHClient()
        if not client:
            return 0
        transport = client.get_transport()
        transport.set_keepalive(1)
        channel = transport.open_session()
        channel.settimeout(self.delta)
        cmd = "tail -f " + self.takipDosya + "| grep  --line-buffered " + self.takipKelime
        channel.exec_command(cmd)
        LeftOver = ""
        while transport.is_active():
            # print("transport is active")
            self.textEdit.append("deneme")
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
                        print(line)
                        self.textEdit.append(line)
            time.sleep(1)
        client.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWin()
    ui.show()
    # ui.goster()
    sys.exit(app.exec_())