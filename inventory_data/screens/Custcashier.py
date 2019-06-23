from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from screens import ViewCustomerById, ViewCustomerByContact, ViewCustomerByName
from utilities import *
import sys

class Custcashier(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(10, 20, 1500, 1000)
        self.setWindowTitle("Inventory Control System::Cashier")
        newfont = QFont("Bell MT", 13, QFont.Bold)
        label=QLabel(self)
        label.move(0,0)
        pixmap=QPixmap('customer.png')
        label.setPixmap(pixmap)
        self.btnid=QPushButton("",self)
        self.btnname=QPushButton("",self)
        self.btncontact=QPushButton("",self)
        self.btncontact.setStyleSheet("background-color:#2BB550; ;height:150;width:220")
        self.btnname.setStyleSheet("background-color:#2BB550; ;height:150;width:220")
        self.btnid.setStyleSheet("background-color:#2BB550; ;height:150;width:220")
        self.btncontact.setIcon(QIcon("contact.png"))
        self.btncontact.setIconSize(QSize(130, 130))

        self.btnid.setIcon(QIcon("id.png"))
        self.btnid.setIconSize(QSize(130, 130))

        self.btnname.setIcon(QIcon("name.png"))
        self.btnname.setIconSize(QSize(130, 130))

        self.movie = QMovie('Cust.gif', QByteArray(), self)
        size = self.movie.scaledSize()
        self.movie_screen = QLabel(self)
        self.movie_screen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.movie_screen.setMovie(self.movie)
        self.movie.start()

        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(40)
        self.movie_screen.setAlignment(Qt.AlignCenter)

        self.btncontact.setToolTip("To check customer record by contact")
        self.btnid.setToolTip("To check customer record by ID")
        self.btnname.setToolTip("To check customer record by name")

        self.btncontact.move(246,186)
        self.btnid.move(246, 350)
        self.movie_screen.move(500, 350)
        self.btnname.move(246, 515)

        self.btncontact.clicked.connect(self.Contact)
        self.btnid.clicked.connect(self.ID)
        self.btnname.clicked.connect(self.Name)
        #self.show()

    def ID(self):
        self.obj=ViewCustomerById.ViewCustomerById()
        self.obj.show()

    def Contact(self):
        self.obj=ViewCustomerByContact.ViewCustomerByContact()
        self.obj.show()

    def Name(self):
        try:
            self.obj=ViewCustomerByName.ViewCustomerByName()
            self.obj.show()
        except BaseException as ex:
            print(ex)