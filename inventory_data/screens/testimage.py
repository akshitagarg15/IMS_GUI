from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import sys

class image(QWidget):
    def __init__(self):
        super().__init__()
        grid=QGridLayout()
        lblpic = QLabel()
        pixmap = QPixmap("bill.jpg")
        lblpic.setPixmap(pixmap)

        grid.addWidget(lblpic,3 ,1)
        self.setLayout(grid)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = image()
    sys.exit(app.exec_())