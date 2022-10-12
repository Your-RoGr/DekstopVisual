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

        # for i in range(self.mainLayout.count()):
        #     self.mainLayout.itemAt(i).widget().clicked.connect(lambda x: self.onMyCheckBoxClick(self.mainLayout.itemAt(i).widget()))

            # self.checkBoxs.clicked.connect(lambda x: self.onMyCheckBoxClick(self.checkBox))

        self.setLayout(self.mainLayout)

    # def onMyNewCheckBoxClick(self, this):
    #     dlg = QColorDialog(self)
    #
    #     if dlg.exec_():
    #         this.setStyleSheet(f'color: {dlg.currentColor().name()};')