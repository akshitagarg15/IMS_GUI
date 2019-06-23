from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql
from PyQt5.QtCore import *
import sys
from dao import Connections
from utilities import *



class ChangePass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 220)
        self.setWindowTitle("Change Password")
        font = QFont()
        font.setPointSize(18)
        self.setFont(font)
        self.font = QFont("Bell MT")


        layout = QVBoxLayout()
        layout.addWidget(self.create_form())
        # layout.addWidget(btn)
        self.setLayout(layout)
        self.show()

    def create_form(self):
        self.formGroupBox = QGroupBox("Change Password")
        fbox = QFormLayout()

        ######## Labels ##########
        self.lbl3 = QLabel("CHANGE PASSWORD ")
        fbox.addRow(self.lbl3)
        self.lbl3.setAlignment(Qt.AlignCenter)



        self.uname = QLineEdit()
        fbox.addRow(QLabel("Username  : "), self.uname)

        self.oldpass= QLineEdit()
        fbox.addRow(QLabel("Old Password  : "), self.oldpass)
        self.oldpass.setEchoMode(QLineEdit.Password)

        self.newpass= QLineEdit()
        fbox.addRow(QLabel("New Password: "), self.newpass)
        self.newpass.setEchoMode(QLineEdit.Password)

        self.conpass = QLineEdit()
        fbox.addRow(QLabel("Confirm Password: "), self.conpass)
        self.conpass.setEchoMode(QLineEdit.Password)

        self.btn1 = QPushButton("CHANGE")
        fbox.addRow(self.btn1)
        self.btn1.clicked.connect(self.Change)

        self.setLayout(fbox)

    def Change(self):
        message=""
        uname=self.uname.text()
        oldpass=self.oldpass.text()
        newpass=self.newpass.text()
        conpass=self.conpass.text()
        if newpass== conpass:
            con=Connections.Connection()
            query="select username, password from logins where password='"+oldpass+"'"
            self.record=con.ExecuteQuery(query)
            if self.record is not None:
                query="update logins set password = '"+newpass+"'"
                query+=" where username='"+uname+"' and password='"+oldpass+"'"
                print(query)
                if con.InsertQuery(query):
                    message="Password changed successfully"
                else:
                    message= "Password is not changed"

            else:
                message=" Passwords do not match"
        else:
            message="Invalid username or password"
        ShowMessageDialog(self, message)
