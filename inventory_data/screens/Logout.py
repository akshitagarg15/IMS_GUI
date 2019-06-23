from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from screens import LoginScreen, LoginReplica
from utilities import *
import sys

class Logout(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Management System::Logout Screen")
        self.setGeometry(100,300,550,550)
        newfont = QFont("Bell MT", 18, QFont.Bold)
        self.layout=QVBoxLayout()
        self.btnaccount=QPushButton("Login With Another Account")
        self.btnexit=QPushButton()
        self.btnaccount.setFont(newfont)
        self.btnexit.setFont(newfont)
        self.layout.addWidget(self.btnaccount)
        self.layout.addWidget(self.btnexit)
        self.btnaccount.setStyleSheet("background-color:LIGHT BLUE;color:RED;Background-image:url();Background-repeat:no repeat;background-position:10% 50px;width:20%;height:500%")
        #self.btnaccount.setStyleSheet("background-color:GREY; color: White")
        self.setLayout(self.layout)
        self.btnexit.clicked.connect(self.Exit)
        self.btnaccount.clicked.connect(self.Account)
        #self.show()
    def Exit(self):
        sys.exit(True)
    def Account(self):
        self.obj=LoginReplica.LoginReplica()
        self.obj.show()

        #self.close()