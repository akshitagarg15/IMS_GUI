from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from screens import AddUser, ChangePass, DelUser
from utilities import *

class About(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):

        #self.setGeometry(100,50,300,250)
        self.setWindowTitle("Settings")
        label = QLabel(self)
        label.move(0, 0)
        pixmap = QPixmap('settings5.png')
        label.setPixmap(pixmap)

        self.btnnew = QPushButton("", self)
        self.btnnew.setToolTip("To add a new user")
        self.btndel=QPushButton("",self)
        self.btndel.setToolTip("To delete a login userID")
        self.btnnew.move(210, 190)
        self.btndel.move(210, 570)
        self.btnpass = QPushButton("",self)
        self.btnpass.setToolTip("To change password")
        self.btnpass.move(210,390)



        self.btnpass.setStyleSheet("Background-color:Green;color:Green; ;height:90;width:100")
        self.btnpass.setIcon(QIcon("changepass.png"))
        self.btnpass.setIconSize(QSize(100,100))

        #self.btndel.setStyleSheet("Background-color:Green;color:Green; font-size:30px;height:90;width:100")
        self.btndel.setIcon(QIcon("deluser.png"))
        self.btndel.setIconSize(QSize(100, 100))

        #self.btnnew.setStyleSheet("Background-color:Green;color:Green; font-size:30px;height:90;width:100")
        self.btnnew.setIcon(QIcon("newuser.png"))
        self.btnnew.setIconSize(QSize(100, 100))
        self.btnnew.clicked.connect(self.AddUser)
        self.btndel.clicked.connect(self.DelUser)
        self.btnpass.clicked.connect(self.ChangePass)
        #self.showMaximized()
        #self.setWindowState(Qt.WindowMaximized)
        self.showFullScreen()
    def AddUser(self):
        self.obj = AddUser.AddUser()

        self.obj.show()
        #self.close()

    def ChangePass(self):
        self.obj=ChangePass.ChangePass()
        self.obj.show()

    def DelUser(self):
        self.obj=DelUser.DelUser()
        self.obj.show()

