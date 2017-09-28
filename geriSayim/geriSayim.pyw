import sys
from PyQt5.QtWidgets import *
from Dialogs.MainWindow import MainWindow

def main():
    app = QApplication(sys.argv)
    pen = MainWindow()
    app.exec_()

if __name__ == "__main__":
    main()