from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import sys
class Combo(QWidget):
    def __init__(self):
        super().__init__()
        grid=QGridLayout()
        self.combo=QComboBox()

        lbl=QLabel("Enter Id")
        self.LineEdit=QLineEdit()
        self.btn=QPushButton("enter")

        grid.addWidget(lbl,1,0,1,2)
        grid.addWidget(self.LineEdit,2,0,1,2)
        grid.addWidget(self.btn,3,0,1,2)
        self.btn.clicked.connect(self.connect)
        self.setLayout(grid)
        self.show()
    def connect(self):
        id=self.LineEdit.text()
        if ValidLicence(id):
            print("valid")
        else:
            print("not valid")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Combo()
    sys.exit(app.exec_())
