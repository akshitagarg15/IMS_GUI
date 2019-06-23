from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql
from PyQt5.QtCore import *
import sys
from dao import Connections
from utilities import *



class DelUser(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 220)
        self.setWindowTitle("Delete User")
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
        self.formGroupBox = QGroupBox("Delete User")
        fbox = QFormLayout()

        ######## Labels ##########
        self.lbl3 = QLabel("DELETE USER ")
        fbox.addRow(self.lbl3)
        self.lbl3.setAlignment(Qt.AlignCenter)



        self.uname = QLineEdit()
        fbox.addRow(QLabel("Username  : "), self.uname)
        self.uname.setToolTip("Enter username to be deleted")
        self.password= QLineEdit()
        fbox.addRow(QLabel("Password  : "), self.password)
        self.password.setToolTip("Enter password of username")
        self.password.setEchoMode(QLineEdit.Password)


        self.btn1 = QPushButton("DELETE")
        fbox.addRow(self.btn1)
        self.btn1.clicked.connect(self.Delete)

        self.setLayout(fbox)

    def Delete(self):
        res=ShowConfirmation(self)
        if res==QMessageBox.Yes:
            message=""
            uname=self.uname.text()
            password=self.password.text()

            con=Connections.Connection()
            query="select username, password from logins where password='"+password+"'"
            self.record=con.ExecuteQuery(query)

            if self.record is not None :
                query="delete from logins where username='"+uname+"'"


                if con.InsertQuery(query):
                    message="User Deleted successfully"
                else:
                    message= "User not deleted"

            else:
                message=" UserID Not Found"
        else:
            message="Deletion Aborted"
        ShowMessageDialog(self, message)
