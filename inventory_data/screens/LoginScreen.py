from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
from screens import AdminMainWindow, UserMainWindow, CashierMainWindow
import sys

class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 1500, 1000)
        self.setWindowTitle("Inventory Control System::LoginScreen")
        newfont = QFont("Bell MT", 13, QFont.Bold)
        label=QLabel(self)
        label.move(0,0)
        pixmap=QPixmap('IMS(3).png')
        label.setPixmap(pixmap)
        self.btnlogin=QPushButton("Login",self)
        self.unameEdit=QLineEdit(self)
        self.passEdit = QLineEdit(self)
        self.passEdit.setEchoMode(QLineEdit.Password)
        #self.btnbill=QPushButton("Billing",self)
        self.btncancel=QPushButton("Cancel",self)
        self.unameEdit.setStyleSheet(" font-size:40px")
        self.passEdit.setStyleSheet(" font-size:40px")
        self.btncancel.setStyleSheet("background-color:green; color:white; font-size:30px;height:50;width:120")
        #self.btncustomer.setStyleSheet("background-color:Brown;Background-image:url(info.svg);Background-repeat:no repeat; color:Cherry Red; font-size:30px;height:100%;width:220%")
        self.btnlogin.setStyleSheet("background-color:Light Green; color:Maroon; font-size:30px;height:50;width:120")
        self.unameEdit.move(705,290)
        self.passEdit.move(705, 400)
        self.btnlogin.move(705,530)
        self.btncancel.move(850, 530)
        self.btnlogin.clicked.connect(self.Login)
        self.btncancel.clicked.connect(self.Cancel)
        #self.btnlogin.setDefault(True)
        self.btncancel.setDefault(True)

        #self.btnlogout.move(146, 515)
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
                    if rolename=="Admin":
                        self.obj=AdminMainWindow.AdminMainWindow(uname)
                        self.obj.show()
                        if record[0][2] is None:
                            message="Welcome Admin First Time"
                        else:
                            message="Your Last Visit: "+ str(record[0][2])
                        query="update logins set lastlogin=sysdate() "
                        query+=" where username= '"+uname+"'"
                        con.InsertQuery(query)
                        self.close()
                    elif rolename=="User":
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
                    elif rolename=="Cashier":
                        print(6)
                        self.obj=CashierMainWindow.CashierMainWindow(uname)
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


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:

            self.Login()

    def Cancel(self):
        self.close()
