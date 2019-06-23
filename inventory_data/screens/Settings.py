from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from screens import AddUser
from utilities import *
import sys

class Settings(QWidget):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Inventory Control System::Settings")
        self.setGeometry(0, 0, 1500, 1000)
        newfont = QFont("Bell MT", 13, QFont.Bold)
        #grid=QGridLayout()
        lbl=QLabel(self)
        pixmap=QPixmap("IMS(3).png")
        lbl.setPixmap(pixmap)
        lbl.move(0,0)

        self.btnnewuser=QPushButton("Add New User",self)
        self.btnpass=QPushButton("Change Password",self)
        self.btndeluser=QPushButton("Delete User",self)
        self.btndeluser.setStyleSheet("background-color:SKY Blue; color:Red; font-size:30px;height:70;width:250")
        self.btnpass.setStyleSheet("background-color:White; color:Red; font-size:30px;height:70;width:250")
        self.btnnewuser.setStyleSheet("background-color:White; color:Red; font-size:30px;height:70;width:250")
        #grid.addWidget(self.btncustomer,2,1)
        #grid.addWidget(self.btnbill, 3, 1)
        #grid.addWidget(self.btnlogout, 4, 1, 1, 1)
        #self.setLayout(grid)
        self.btnnewuser.move(146,186)
        self.btnpass.move(146, 300)
        lbl.move(246, 300)
        self.btndeluser.move(146, 415)
        self.btnnewuser.clicked.connect(self.AddUser)
        #self.show()

    def AddUser(self):
        self.obj=AddUser.AddUser()

        self.obj.show()
        self.close()





