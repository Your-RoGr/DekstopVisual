import win32con
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
import os
import win32gui

from MainForm import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.show()

        self.createButton.clicked.connect(self.onMyCreateButtonClick)
        self.exitButton.clicked.connect(self.onMyExitButtonClick)

    def onMyExitButtonClick(self,s):
        self.close()

    def onMyCreateButtonClick(self, s):
        pass

def Main():
    app = QApplication(sys.argv)

    window = MainWindow()

    app.exec_()

if __name__ == '__main__':
    Main()