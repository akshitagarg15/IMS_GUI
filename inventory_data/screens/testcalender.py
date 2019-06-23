import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from utilities import *

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.dateEdit = QDateEdit()
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.calendarWidget().installEventFilter(self)
        layout.addWidget(self.dateEdit, 0, 0)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Calendar')
        layout.addWidget(self.dateEdit,1,2)
        self.setLayout(layout)

        self.show()




def main():

    app = QApplication(sys.argv)
    ex = Widget()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()