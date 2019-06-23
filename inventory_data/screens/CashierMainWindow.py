from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from screens import Custcashier, BillScreen
from utilities import *
import sys

class CashierMainWindow(QWidget):
    def __init__(self,uname=None):
        super().__init__()
        self.username=uname

        self.setGeometry(0, 0, 1500, 1000)
        self.setWindowTitle("Inventory Control System::Cashier")
        newfont = QFont("Bell MT", 13, QFont.Bold)
        label=QLabel(self)
        label.move(0,0)
        pixmap=QPixmap('cashierblue.png')
        label.setPixmap(pixmap)
        self.btncustomer=QPushButton("",self)
        self.btnbill=QPushButton("",self)
        self.btnlogout=QPushButton("",self)
        self.btnabout=QPushButton("about",self)
        self.btnlogout.setStyleSheet("background-color:#2BB550; ;height:150;width:220")
        self.btnbill.setStyleSheet("background-color:#2BB550; ;height:150;width:220")
        self.btncustomer.setStyleSheet("background-color:#2BB550; ;height:150;width:220")
        #self.btncustomer.setStyleSheet("background-color:#2BB550;Background-image:url(info.svg);Background-repeat:no repeat; color:Cherry Red; font-size:30px;height:150;width:220%")
        #self.btnbill.setStyleSheet("background-color:#2BB550; color:Yellow;padding :15px 24px; box-shadow: -12px 12px 0 hsl(16,100%,30%);outline:none; font-size:1.4rem;height:130;width:220")
        self.btnlogout.setIcon(QIcon("logout1.png"))
        self.btnlogout.setIconSize(QSize(130, 130))

        self.btnbill.setIcon(QIcon("bill1.png"))
        self.btnbill.setIconSize(QSize(130, 130))

        self.btncustomer.setIcon(QIcon("customercashier.svg"))
        self.btncustomer.setIconSize(QSize(130, 130))

        self.btncustomer.move(246,186)
        self.btnbill.move(246, 350)
        self.btnlogout.move(246, 515)
        self.btnabout.move(1000,800)
        self.btncustomer.setToolTip("To search customer record")
        self.btnlogout.setToolTip("To make exit from software")
        self.btnbill.setToolTip("To generate invoice")
        self.btnlogout.clicked.connect(self.logout)
        self.btncustomer.clicked.connect(self.customer)
        self.btnbill.clicked.connect(self.Bill)
        self.show()

    def logout(self):
        res=ShowConfirmation(self)
        if res==QMessageBox.Yes:
            sys.exit(True)

    def customer(self):
        self.obj=Custcashier.Custcashier()
        self.obj.show()

    def Bill(self):
        self.obj=BillScreen.BillScreen(self.username)
        self.obj.show()


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=CashierMainWindow()
    sys.exit(app.exec_())
