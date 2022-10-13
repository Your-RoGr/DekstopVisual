from PyQt5.Qt import *
from Handler_Class import Handler

class GetDoubleSpinBoxs(QWidget):
    def __init__(self, comboBoxFileNames):
        super(GetDoubleSpinBoxs, self).__init__()

        self.comboBoxFileNames = comboBoxFileNames
        self.initUi()

    def initUi(self):
        self.mainLayout = QVBoxLayout()

        for carottage in Handler(self.comboBoxFileNames.currentText()).keys:
            if carottage != 'DEPT':
                self.newDoubleSpinBoxs = QDoubleSpinBox()
                self.newDoubleSpinBoxs.setObjectName(carottage)
                self.newDoubleSpinBoxs.setValue(1)
                self.newDoubleSpinBoxs.setMaximumWidth(62)
                self.newDoubleSpinBoxs.setMinimumWidth(62)
                self.newDoubleSpinBoxs.setMaximumHeight(30)
                self.newDoubleSpinBoxs.setMinimumHeight(30)
                self.newDoubleSpinBoxs.setFont(QFont('Comic Sans MS', 10))

                self.mainLayout.addWidget(self.newDoubleSpinBoxs)

        self.setLayout(self.mainLayout)