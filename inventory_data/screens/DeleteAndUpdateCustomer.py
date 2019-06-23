from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import datetime

class DeleteAndUpdateCustomer(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        grid=QGridLayout()
        self.setWindowTitle("Delete/Update Customer Details")
        self.cust_records=list()
        newfont=QFont("Bell MT",18,QFont.Bold)
        lblcid = QLabel("Customer Id")
        self.cidcombo=QComboBox()
        lblcname = QLabel("Customer Name")
        lblcontact = QLabel("Contact")
        lblemail = QLabel("Email Id")
        lbladd = QLabel("Address")
        #lblentry = QLabel("Entry Date")

        self.cnameEdit = QLineEdit()
        self.contactEdit = QLineEdit()
        self.emailEdit = QLineEdit()
        self.addEdit = QLineEdit()
        #self.entryedit = QLabel()
        self.btndelete = QPushButton("Delete Record")
        self.btnupdate = QPushButton("Update Record")

        lblcid.setFont(newfont)
        self.cidcombo.setFont(newfont)
        lblcname.setFont(newfont)
        lblcontact.setFont(newfont)
        lbladd.setFont(newfont)
        #lblentry.setFont(newfont)
        lblemail.setFont(newfont)
        self.cnameEdit.setFont(newfont)
        self.emailEdit.setFont(newfont)
        self.addEdit.setFont(newfont)
        self.contactEdit.setFont(newfont)
        #self.entryedit.setFont(newfont)
        self.btndelete.setFont(newfont)
        self.btnupdate.setFont(newfont)

        grid.addWidget(lblcid, 1, 0)
        grid.addWidget(self.cidcombo, 1, 1, 1, 3)
        grid.addWidget(lblcname, 2, 0)
        grid.addWidget(self.cnameEdit, 2, 1, 1, 3)

        grid.addWidget(lblcontact, 3, 0)
        grid.addWidget(self.contactEdit, 3, 1, 1, 3)

        grid.addWidget(lblemail, 4, 0)
        grid.addWidget(self.emailEdit, 4, 1, 1, 3)

        grid.addWidget(lbladd, 5, 0)
        grid.addWidget(self.addEdit, 5, 1, 1, 3)

        #grid.addWidget(lblentry, 6, 0)
        #grid.addWidget(self.entryedit, 6, 1, 1, 3)
        grid.addWidget(self.btnupdate, 7, 1)
        grid.addWidget(self.btndelete, 7, 2)
        self.cidcombo.addItem("Choose Customer Id")
        self.PrepareComboItems()
        self.cidcombo.currentTextChanged.connect(self.ChangeCombo)
        self.btndelete.clicked.connect(self.DeleteCust)
        self.btnupdate.clicked.connect(self.UpdateCust)

        self.setLayout(grid)

        #self.show()

    def PrepareComboItems(self):
        con=Connections.Connection()
        table_name="customerinfo"
        column_values=("CustomerId","CustomerName","contact","EmailId","Address")
        query=con.CreateSelectQuery(column_values,table_name)
        self.cust_records=con.ExecuteQuery(query)
        if len(self.cust_records)>0:
            for record in self.cust_records:
                value=record[1]+"("+str(record[0])+")"
                self.cidcombo.addItem(value)

    def ChangeCombo(self):
        index=self.cidcombo.currentIndex()
        if index > 0 and (index - 1) <= len(self.cust_records):
            record=self.cust_records[index-1]
            self.cnameEdit.setText(record[1])
            self.contactEdit.setTextstr((record[2]))
            self.emailEdit.setText(record[3])
            self.addEdit.setText(record[4])
        else:
            self.cnameEdit.setText("")
            self.contactEdit.setText("")
            self.emailEdit.setText('')
            self.addEdit.setText("")

    def DeleteCust(self):
        try:
            res=ShowConfirmation(self)
            message=""
            if res==QMessageBox.Yes:
                cid=self.cidcombo.currentIndex()
                if cid>0:
                    record=self.cust_records[cid-1]
                    custid=str(record[0])
                    con=Connections.Connection()
                    table_name="customerinfo"
                    primary_value={"CustomerId":custid}
                    query=con.CreateDeleteQuery(table_name,primary_value)
                    if con.InsertQuery(query):
                        message="Deletion happened Successfully"
                        self.PrepareComboItems()
                    else:
                        message="Deletion Failure Due To: "+con.GetErrorMessage()
            else:
                message="Deletion Cancelled"
            ShowMessageDialog(self,message)
        except BaseException as ex:
            print(ex)

    def UpdateCust(self):
        res=ShowConfirmation(self)
        cid=self.cidcombo.currentIndex()
        message=""
        if res==QMessageBox.Yes:
            if cid>0:
                record=self.cust_records[cid-1]
                custid=record[0]
                cname=self.cnameEdit.text()
                contact=self.contactEdit.text()
                email=self.emailEdit.text()
                add=self.addEdit.text()
                Date=datetime.datetime.now()
                entrydate=Date.date()
                entry=str(entrydate)
                if IsEmpty(cname) or IsEmpty(contact) or IsEmpty(add):
                    message+="Enter all the required Details\n\n"
                if  not ValidContact(contact):
                    message+="Enter a valid ContactNo\n\n"
                else:
                    con=Connections.Connection()
                    table_name="customerinfo"
                    primary_value={'CustomerId':custid}
                    column_values={"CustomerName":cname,"contact":contact,"EmailId":email,"Address":add}
                    query=con.CreateUpdateQuery(table_name,column_values,primary_value)
                    print(query)
                    if con.InsertQuery(query):
                        message="Updation happened Successfully"
                    else:
                        message="Updation Error Due To: "+con.GetErrorMessage()

        else:
            message="Updation Cancelled"
        ShowMessageDialog(self, message)
