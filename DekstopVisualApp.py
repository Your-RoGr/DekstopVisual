import sys
# import os
# import random
#
# import numpy
# import pandas
import win32gui
import win32con
import pywintypes # need for work pyinstaller with win32gui

from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *

from MplCanvas_Class import MplCanvas, MplCanvases

from MainForm import Ui_MainWindow

from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigatorToolbar

from Handler_Class import Handler
from GetCheckBox_Class import GetCheckBox

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.path = "data\\GIS_md"

        self.setWindowTitle("DesktopVisual")

        self.widgetCanvas.setMaximumHeight(900)
        self.widgetCanvas.setMinimumHeight(900)

        self.horizontalSlider.setRange(900, 6000)
        self.horizontalSlider.valueChanged.connect(self.changeSliderValue) # Сделать связь с lctrl

        self.actionOpen.triggered.connect(self.actionOpenToggled)

        self.comboBoxFileNames.addItems(Handler.GetFileNames(self.path))

        self.scrollAreaCarottageWidgetContents = QWidget()
        self.gridLayoutCarottageWidgetContents = QGridLayout()
        self.layoutH = QHBoxLayout(self.scrollAreaCarottageWidgetContents)
        self.layoutH.addLayout(self.gridLayoutCarottageWidgetContents)
        self.scrollAreaCarottage.setWidget(self.scrollAreaCarottageWidgetContents)

        self.checkBoxs = GetCheckBox(self.comboBoxFileNames)
        self.gridLayoutCarottageWidgetContents.addWidget(self.checkBoxs)

        self.plotButton.clicked.connect(self.onMyPlotButtonClick)

        self.allButton.clicked.connect(self.onMyAllButtonClick)

        for i in range(self.checkBoxs.mainLayout.count()):
            self.GiveOnMyCheckBoxClick(i)

        self.comboBoxFileNames.currentTextChanged.connect(self.changeComboBoxFileNamesEvent)

        self.exitButton.clicked.connect(self.onMyExitButtonClick)

    def actionOpenToggled(self):
        filter = '.las'
        customFilter = 'Other file types\0*.*0'

        try:
            fname, customFilter, flags = win32gui.GetOpenFileNameW(
                # InitialDir=os.environ['temp'],
                Flags=win32con.OFN_ALLOWMULTISELECT|win32con.OFN_EXPLORER,
                # File='somefilename',
                # DefExt='txt',
                Title='Выберите файл в папке назначения',
                Filter=filter,
                CustomFilter=customFilter,
                FilterIndex=0
            )

            try:
                a = repr(fname).split('\\')

                a.pop(-1)
                a.pop(0)

                path = "C:\\"

                for i in a:
                    path += i + '\\'

                self.path = path

            except:
                pass

        except:
            pass

        self.comboBoxFileNames.addItems(Handler.GetFileNames(self.path))

    def GiveOnMyCheckBoxClick(self, i):
        self.checkBoxs.mainLayout.itemAt(i).widget().clicked.connect(
            lambda x: self.onMyCheckBoxClick(self.checkBoxs.mainLayout.itemAt(i).widget()))

    def changeComboBoxFileNamesEvent(self):
        self.gridLayoutCarottageWidgetContents.removeWidget(self.checkBoxs)
        self.checkBoxs = GetCheckBox(self.comboBoxFileNames)
        self.gridLayoutCarottageWidgetContents.addWidget(self.checkBoxs)

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
        self.canvas = MplCanvases(fileName, self.GetColorsCheckBoxs())
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

    def onMyAllButtonClick(self, s):
        pass

    def onMyCheckBoxClick(self, this):
        dlg = QColorDialog(self)

        if dlg.exec_():
            this.setStyleSheet(f'color: {dlg.currentColor().name()};')

    def onMyExitButtonClick(self,s):
        self.close()

    def GetColorsCheckBoxs(self):
        dictColors = {'Name': [], 'Color': []}
        for i in range(self.checkBoxs.mainLayout.count()):
            dictColors['Name'].append(self.checkBoxs.mainLayout.itemAt(i).widget().objectName())
            dictColors['Color'].append(self.checkBoxs.mainLayout.itemAt(i).widget().styleSheet())

        return dictColors


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