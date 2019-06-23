from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import sys

class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        grid = QGridLayout()
        newfont = QFont("Bell MT", 18, QFont.Bold)
        self.rboldcust = QRadioButton("Old Customer")
        self.rbnewcust = QRadioButton("New Customer")
        lblcust = QLabel("New Customer Details")
        lblcustname = QLabel("Customer Name")
        lblcontact = QLabel("Contact No.")
        lblemail = QLabel("Email Id")
        lbladd = QLabel("Address")
        lblbid = QLabel("Choose BrandID")
        lblcid = QLabel("Choose CatID")
        lblid = QLabel("Choose ItemID")
        lblcustid = QLabel("Choose CustomerID")

        lblcust.setFont(newfont)
        lblcustname.setFont(newfont)
        lblcontact.setFont(newfont)
        lblemail.setFont(newfont)
        lbladd.setFont(newfont)
        lblcid.setFont(newfont)
        lblbid.setFont(newfont)
        lblid.setFont(newfont)
        lblcustid.setFont(newfont)
        self.rboldcust.setFont(newfont)
        self.rbnewcust.setFont(newfont)

        self.custnameEdit = QLineEdit()
        self.contactEdit = QLineEdit()
        self.emailEdit = QLineEdit()
        self.addEdit = QLineEdit()
        self.custidcombo = QComboBox()
        self.brandidcombo = QComboBox()
        self.catidcombo = QComboBox()
        self.itemidcombo = QComboBox()

        lblqty = QLabel("Qty")
        self.qtyEdit = QLineEdit()
        self.btn = QPushButton("ADD Product")
        lblpic = QLabel(self)
        pixmap = QPixmap("inventory-track.gif")
        lblpic.setPixmap(pixmap)

        lblqty.setFont(newfont)
        self.qtyEdit.setFont(newfont)
        self.addEdit.setFont(newfont)
        self.custnameEdit.setFont(newfont)
        self.contactEdit.setFont(newfont)
        self.emailEdit.setFont(newfont)
        self.custidcombo.setFont(newfont)
        self.brandidcombo.setFont(newfont)
        self.catidcombo.setFont(newfont)
        self.itemidcombo.setFont(newfont)
        self.btn.setFont(newfont)

        grid.addWidget(self.rboldcust, 1, 1)
        grid.addWidget(self.rbnewcust, 1, 3)
        grid.addWidget(lblcustid, 2, 0, 1, 1)
        grid.addWidget(self.custidcombo, 2, 1, 1, 1)
        grid.addWidget(lblcust, 2, 3, 1, 2)
        grid.addWidget(lblcustname, 3, 3, 1, 1)
        grid.addWidget(self.custnameEdit, 3, 4, 1, 1)
        grid.addWidget(lblcontact, 4, 3, 1, 1)
        grid.addWidget(self.contactEdit, 4, 4, 1, 1)
        grid.addWidget(lblemail, 5, 3, 1, 1)
        grid.addWidget(self.emailEdit, 5, 4, 1, 1)

        grid.addWidget(lbladd, 6, 3, 1, 1)
        grid.addWidget(self.addEdit, 6, 4, 1, 1)
        grid.addWidget(lblbid, 7, 0, 1, 1)
        grid.addWidget(self.brandidcombo, 7, 1)
        grid.addWidget(lblcid, 7, 2)
        grid.addWidget(self.catidcombo, 7, 3)
        grid.addWidget(lblid, 7, 4)
        grid.addWidget(self.itemidcombo, 7, 5)
        grid.addWidget(lblqty, 8, 0, 1, 1)
        grid.addWidget(self.qtyEdit, 8, 1, 1, 1)
        grid.addWidget(self.btn, 8, 3, 1, 1)
        grid.addWidget(lblpic, 9, 0, 55, 60)
        self.custidcombo.addItem("Choose CustomerID")
        self.brandidcombo.addItem("Choose BrandID")
        self.catidcombo.addItem("Choose CategoryID")
        self.itemidcombo.addItem("Choose ItemID")
        self.rboldcust.toggled.connect(self.radio1_clicked)
        self.rbnewcust.toggled.connect(self.radio2_clicked)

        self.setLayout(grid)
        self.show()
    def radio1_clicked(self, enabled):
        print(" Radio 1 Clicked ",enabled)
        self.custidcombo.setEnabled(enabled)

    def radio2_clicked(self, enabled):
        print(" Radio 2 Clicked ",enabled)
        if enabled:
            cname=self.custnameEdit.text()
            contact=self.contactEdit.text()
            email=self.emailEdit.text()
            add=self.addEdit.text()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    sys.exit(app.exec_())