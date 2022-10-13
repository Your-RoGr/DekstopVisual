from PyQt5.Qt import *
from Handler_Class import Handler

class GetCheckBox(QWidget):
    def __init__(self, comboBoxFileNames):
        super(GetCheckBox, self).__init__()

        self.comboBoxFileNames = comboBoxFileNames
        self.initUi()

    def initUi(self):
        self.mainLayout = QVBoxLayout()

        for carottage in Handler(self.comboBoxFileNames.currentText()).keys:
            if carottage != 'DEPT':
                self.newCheckBox = QCheckBox()
                self.newCheckBox.setObjectName(carottage)
                self.newCheckBox.setText(carottage)
                self.newCheckBox.setMaximumWidth(62)
                self.newCheckBox.setMinimumWidth(62)
                self.newCheckBox.setMaximumHeight(30)
                self.newCheckBox.setMinimumHeight(30)
                self.newCheckBox.setFont(QFont('Comic Sans MS', 10))

                self.mainLayout.addWidget(self.newCheckBox)

        self.setLayout(self.mainLayout)