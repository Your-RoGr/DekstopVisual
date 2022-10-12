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

from Handler_Class import Handler

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle("DekstopVisual")

        self.widgetCanvas.setMaximumHeight(900)
        self.widgetCanvas.setMinimumHeight(900)

        self.horizontalSlider.setRange(900, 6000)
        self.horizontalSlider.valueChanged.connect(self.changeSliderValue) # Сделать связь с lctrl

        self.comboBoxFileNames.addItems(Handler.GetFileNames())

        self.plotButton.clicked.connect(self.onMyPlotButtonClick)

        self.exitButton.clicked.connect(self.onMyExitButtonClick)

        self.showCanvases(Handler.GetFileNames()[0])

    def changeSliderValue(self):
        self.widgetCanvas.setMaximumHeight(self.horizontalSlider.value())
        self.widgetCanvas.setMinimumHeight(self.horizontalSlider.value())

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

    def onMyPlotButtonClick(self,s):
        self.verticalLayout_2.removeWidget(self.widgetToolbar)

        self.widgetCanvas = QWidget()
        self.widgetToolbar = QWidget()

        self.scrollAreaCanvases.setWidget(self.widgetCanvas)
        self.verticalLayout_2.addWidget(self.widgetToolbar)

        self.showCanvases(self.comboBoxFileNames.currentText())


    def onMyExitButtonClick(self,s):
        self.close()

    # def wheelEvent(self, event):
    #     # если event.delta ()> 0: # Свернуть, PyQt4
    #     # This function has been deprecated, use pixelDelta() or angleDelta() instead.
    #     angle = event.angleDelta() / 8  # Возвращает объект QPoint, который является значением колеса прокрутки, единица измерения - 1/8 градуса
    #
    #     angleX = angle.x()  # Расстояние для поворота по горизонтали (здесь не используется)
    #     angleY = angle.y()  # Расстояние для поворота по вертикали
    #
    #     if angleY > 0:
    #         self.setText("Событие прокрутки колеса вверх: самоопределение")
    #         print("Колесо мыши в движении")  # ответ на тестовый запрос
    #     else:  # свернуть
    #         self.setText('Событие прокрутки колеса вниз: определите　себя')
    #         print("Прокрутка колеса мыши вниз")  # Ответ на тестовый запрос
    #
    # def key_lctrl(self):
    #     pass
    #     button_one = QPushButton()
    #     button_one.setShortcut('lctrl')
    #     button_one.clicked.connect(self.key_lctrl)

def Main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()

if __name__ == '__main__':
    Main()