from PyQt5.Qt import *
from Handler_Class import Handler

class GetButtons(QWidget):
    def __init__(self, comboBoxFileNames):
        super(GetButtons, self).__init__()

        self.comboBoxFileNames = comboBoxFileNames
        self.initUi()

    def initUi(self):
        self.mainLayout = QVBoxLayout()

        for carottage in Handler(self.comboBoxFileNames.currentText()).keys:
            if carottage != 'DEPT':
                self.newButton = QPushButton()
                self.newButton.setObjectName(carottage)
                self.newButton.setText(carottage)
                self.newButton.setMaximumWidth(50)
                self.newButton.setMinimumWidth(50)
                self.newButton.setFont(QFont('Comic Sans MS', 10))

                self.mainLayout.addWidget(self.newButton)

        self.setLayout(self.mainLayout)