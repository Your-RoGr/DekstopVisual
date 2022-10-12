import sys
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *

class QColorButton(QPushButton):
    ''' Пользовательский виджет Qt, чтобы отобразить выбранный цвет.
    Щелчок левой кнопкой мыши на кнопке показывает выбор цвета, в то время как
    щелчок правой кнопкой мыши сбрасывает цвет до None (без цвета).         '''

    colorChanged = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(QColorButton, self).__init__(*args, **kwargs)

        dlg = QColorDialog(self)

        if dlg.exec_():
            self.setColor(dlg.currentColor().name())

    def setColor(self, color):
        if color != self.color:
            self.color = color
            self.colorChanged.emit()

        if self.color:
            self.setStyleSheet("background-color: %s;" % self.color)
        else:
            self.setStyleSheet("")

    def color(self):
        return self.color

    def onColorPicker(self):
        '''  Диалоговое окно выбора цвета .
        По умолчанию Qt будет использовать собственный диалог.  '''

        dlg = QColorDialog(self)

        dlg.setCurrentColor(QColor(self.color))

        if dlg.exec_():
            self.setColor(dlg.currentColor().name())

def Main():
    app = QApplication(sys.argv)

    window = QColorButton()
    window.show()

    app.exec_()

if __name__ == '__main__':
    Main()