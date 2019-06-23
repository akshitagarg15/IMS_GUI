from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import datetime


class AddSupplierScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.setWindowTitle("Add Supplier details screen")
        grid=QGridLayout()
        grid.setSpacing(10)

        #Initialize the widgets
        lblsupname=QLabel("Enter Supplier Name")
        lblgstno=QLabel("Enter GSTNO")
        lblcontact = QLabel("Enter Contact")
        lblemailid = QLabel("Enter Email Id")
        lbladdress = QLabel("Enter Address")

        self.supnameEdit=QLineEdit()
        self.gstnoEdit = QLineEdit()
        self.contactEdit = QLineEdit()
        self.emailidEdit = QLineEdit()
        self.addressEdit = QLineEdit()
        self.btn=QPushButton("Add New Supplier")

        newfont=QFont("Bell MT",18,QFont.Bold)
        lblsupname.setFont(newfont)
        lblgstno.setFont(newfont)
        lblcontact.setFont(newfont)
        lblemailid.setFont(newfont)
        lbladdress.setFont(newfont)
        self.supnameEdit.setFont(newfont)
        self.gstnoEdit.setFont(newfont)
        self.contactEdit.setFont(newfont)
        self.emailidEdit.setFont(newfont)
        self.addressEdit.setFont(newfont)
        self.btn.setFont(newfont)
        self.btn.clicked.connect(self.AddSupplier)
        lbl=QLabel(self)
        pixmap=QPixmap("sup.gif")
        lbl.setPixmap(pixmap)

        #initialize the widgets
        grid.addWidget(lblsupname,1,0)
        grid.addWidget(self.supnameEdit, 1, 1,1,2)

        grid.addWidget(lblgstno, 2, 0)
        grid.addWidget(self.gstnoEdit, 2, 1, 1, 2)


        grid.addWidget(lblcontact, 3, 0)
        grid.addWidget(self.contactEdit, 3, 1, 1, 2)
        grid.addWidget(lbl, 3, 4, 1, 1)

        grid.addWidget(lblemailid, 4, 0)
        grid.addWidget(self.emailidEdit, 4, 1, 1, 2)

        grid.addWidget(lbladdress, 5, 0)
        grid.addWidget(self.addressEdit, 5, 1, 1, 2)
        grid.addWidget(self.btn,6,0,1,3)
        self.setLayout(grid)
        #self.show()

    def AddSupplier(self):
        supname = self.supnameEdit.text()
        gstno=self.gstnoEdit.text()
        contact = self.contactEdit.text()
        emailid = self.emailidEdit.text()
        address = self.addressEdit.text()

        message = ""
        AllValid = True
        if IsEmpty(supname):
            message = " Please Fill Supplier Name\n\n"
            AllValid = False
        if IsEmpty(gstno):
            message += " Please Fill Supplier GSTNO\n\n"
            AllValid = False
        elif not ValidGST(gstno):
            message+="Enter a Valid GST NO\n\n"
            AllValid=False
        if IsEmpty(contact):
            message += " Please Fill Supplier Contact\n\n"
            AllValid = False
        elif not ValidContact(contact):
            message += "Please Enter a Valid Contact Number\n\n"
            AllValid = False
        if IsEmpty(address):
            message += "Please Enter Supplier Address\n\n"
            AllValid = False
        if AllValid:
            table_name = "supplierinfo"
            column_values = dict()
            column_values["SupplierName"] = supname
            column_values["GSTno"] = gstno
            column_values["contact"] = contact
            column_values["EmailId"] = emailid
            column_values["Address"] = address


            con = Connections.Connection()

            query = con.CreateInsertQuery(table_name, column_values)
            print(query)
            if con.InsertQuery(query):
                message = "Supplier information saved in database"
            else:
                message = "Insertion Failure Due To:" + con.GetErrorMessage()
        ShowMessageDialog(self, message)
