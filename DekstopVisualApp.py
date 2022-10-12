import sys
import os
import random
import win32gui
import win32con
import pywintypes # need for work pyinstaller with win32gui

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from MplCanvas_Class import MplCanvas, MplCanvases

from MainForm import Ui_MainWindow

from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigatorToolbar

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        k = 1
        self.exitButton.clicked.connect(self.onMyExitButtonClick)
        self.widgetCanvas.setMaximumHeight(k*1000)
        self.widgetCanvas.setMinimumHeight(k*1000)
        self.showCanvases('1.las')

        self.show()

    def onMyExitButtonClick(self,s):
        self.close()

    def showCanvas(self, fileName, carottage):
        # добавление шаблона резмещения на виджет
        self.layout_for_canvas = QVBoxLayout(self.widgetCanvas)
        self.layout_for_toolbar = QVBoxLayout(self.widgetToolbar)
        # Получение объекта класса холста с нашим рисунком
        self.canvas = MplCanvas(fileName, carottage)
        # Размещение экземпляра класса холста в шаблоне размещения
        self.layout_for_canvas.addWidget(self.canvas)
        # Получение объекта класса панели управления холста
        self.toolbar = NavigatorToolbar(self.canvas, self)
        # Размещение экземпляра класса панели управления в шаблоне размещения
        self.layout_for_toolbar.addWidget(self.toolbar)

    def showCanvases(self, fileName):
        # добавление шаблона резмещения на виджет
        self.layout_for_canvas = QVBoxLayout(self.widgetCanvas)
        self.layout_for_toolbar = QVBoxLayout(self.widgetToolbar)
        # Получение объекта класса холста с нашим рисунком
        self.canvas = MplCanvases(fileName)
        # Размещение экземпляра класса холста в шаблоне размещения
        self.layout_for_canvas.addWidget(self.canvas)
        # Получение объекта класса панели управления холста
        self.toolbar = NavigatorToolbar(self.canvas, self)
        # Размещение экземпляра класса панели управления в шаблоне размещения
        self.layout_for_toolbar.addWidget(self.toolbar)

def Main():
    app = QApplication(sys.argv)

    window = MainWindow()

    app.exec_()

if __name__ == '__main__':
    Main()