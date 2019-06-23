import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from screens import AdminMainWindow, UserMainWindow, CashierMainWindow
from utilities import *

class LoginReplica(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.setGeometry(500, 300, 450, 100)
        self.parent=None
        self.setWindowTitle("Inventory Control System::LoginScreen")
        newfont = QFont("Bell MT", 13, QFont.Bold)
        #grid = QGridLayout()

        #lbluname=QLabel("Username")
        #lblpass = QLabel("Password")
        self.unameEdit=QLineEdit()
        self.passEdit = QLineEdit()
        self.passEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.btnlogin=QPushButton("Login")
        self.btncancel=QPushButton("Cancel")
        self.btnlogin.setStyleSheet("Background-color:SKY BLUE;color:RED")
        self.btncancel.setStyleSheet("Background-color:RED;color:White")
        self.passEdit.setFont(newfont)
        self.btncancel.setFont(newfont)
        self.btnlogin.setFont(newfont)
        #lblpass.setFont(newfont)
        #lbluname.setFont(newfont)
        self.unameEdit.setFont(newfont)

        #grid.setSpacing(10)
        #grid.addWidget(lbluname,0,0,1,1)
        #grid.addWidget(self.unameEdit, 0, 1, 1,2)
        #grid.addWidget(lblpass, 1,0, 1, 1)
        #grid.addWidget(self.passEdit, 1,1, 1, 2)
        #grid.addWidget(self.btnlogin, 2, 1, 1,1)
        #grid.addWidget(self.btncancel, 2, 2, 1,1)
        #self.setLayout(grid)
        self.btnlogin.clicked.connect(self.Login)
        self.btncancel.clicked.connect(self.Cancel)

        self.btncancel.move(100,200)


        self.show()

    def Login(self):
        uname=self.unameEdit.text()
        upass=self.passEdit.text()
        message=""
        if IsEmpty(uname):
            message+="Enter Username\n\n"
        elif IsEmpty(upass):
            message+="Enter Password\n\n"
        else:
            query="select password,rolename,lastlogin from logins where username= '"+uname+"'"
            con=Connections.Connection()
            record=con.ExecuteQuery(query)
            if record is not None and len(record)>0:
                password=record[0][0]
                if upass==password:
                    rolename=record[0][1]
                    if rolename=="admin":
                        self.obj=AdminMainWindow.AdminMainWindow()
                        self.obj.show()
                        if record[0][2] is None:
                            message="Welcome Admin First Time"
                        else:
                            message="Your Last Visit: "+ str(record[0][2])
                        query="update logins set lastlogin=sysdate() "
                        query+=" where username= '"+uname+"'"
                        con.InsertQuery(query)
                        self.close()
                    elif rolename=="employee":
                        self.obj=UserMainWindow.UserMainWindow()
                        self.obj.show()
                        if record[0][2] is None:
                            message = "Welcome Employee First Time"
                        else:
                            message="Your Last Visit: "+ str(record[0][2])
                        query="update logins set lastlogin=sysdate() "
                        query+=" where username= '"+uname+"'"
                        con.InsertQuery(query)
                        self.close()
                    elif rolename=="cashier":
                        self.obj=CashierMainWindow.CashierMainWindow()
                        self.obj.show()
                        if record[0][2] is None:
                            message = "Welcome Cashier First Time"
                        else:
                            message="Your Last Visit: "+ str(record[0][2])
                        query="update logins set lastlogin=sysdate() "
                        query+=" where username= '"+uname+"'"
                        con.InsertQuery(query)
                        self.close()
                    else:
                        message="Invalid User Contact Administrator"

                else:
                    message="Invalid Password Given"
            else:
                message="Invalid Username Given"
        ShowMessageDialog(self,message)

    def Cancel(self):
        self.close()