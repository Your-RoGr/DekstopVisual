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
            self.newCheckBox = QCheckBox()
            self.newCheckBox.setObjectName(carottage)
            self.newCheckBox.setText(carottage)

            self.mainLayout.addWidget(self.newCheckBox)

        self.setLayout(self.mainLayout)
