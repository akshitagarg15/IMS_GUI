from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import datetime

class DeleteAndUpdateSupplier(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        grid=QGridLayout()
        self.setWindowTitle("Delete/Update Supplier Details")
        self.sup_records=list()
        newfont=QFont("Bell MT",18,QFont.Bold)
        lblsid = QLabel("Supplier Id")
        self.sidcombo=QComboBox()
        lblsname = QLabel("Supplier Name")
        lblgstno = QLabel("GstNo.")
        lblcontact = QLabel("Contact")
        lblemail = QLabel("Email Id")
        lbladd = QLabel("Address")
        #lblentry = QLabel("Entry Date")

        self.snameEdit = QLineEdit()
        self.gstnoEdit = QLineEdit()
        self.contactEdit = QLineEdit()
        self.emailEdit = QLineEdit()
        self.addEdit = QLineEdit()
        #self.entryedit = QLabel()
        self.btndelete = QPushButton("Delete Record")
        self.btnupdate = QPushButton("Update Record")

        lblsid.setFont(newfont)
        self.sidcombo.setFont(newfont)
        lblsname.setFont(newfont)
        lblgstno.setFont(newfont)
        lblcontact.setFont(newfont)
        lbladd.setFont(newfont)
        #lblentry.setFont(newfont)
        lblemail.setFont(newfont)
        self.snameEdit.setFont(newfont)
        self.emailEdit.setFont(newfont)
        self.addEdit.setFont(newfont)
        self.contactEdit.setFont(newfont)
        self.gstnoEdit.setFont(newfont)
        #self.entryedit.setFont(newfont)
        self.btndelete.setFont(newfont)
        self.btnupdate.setFont(newfont)
        self.sidcombo.setToolTip("select supplier whose records is to delete/update")
        self.emailEdit.setToolTip("Edit email if want to update")
        self.contactEdit.setToolTip("Edit contact if want to update.enter digits only")
        self.gstnoEdit.setToolTip("Edit gstno if want to update. Enter valid gstno as per criteria")
        self.snameEditEdit.setToolTip("Edit name if want to update")
        self.addEdit.setToolTip("Edit address if want to update")
        self.btnupdate.setToolTip("click to update supplier details")
        self.btndelete.setToolTip("click to delete suplier details permanently")

        grid.addWidget(lblsid, 1, 0)
        grid.addWidget(self.sidcombo, 1, 1, 1, 3)
        grid.addWidget(lblsname, 2, 0)
        grid.addWidget(self.snameEdit, 2, 1, 1, 3)

        grid.addWidget(lblgstno, 3, 0)
        grid.addWidget(self.gstnoEdit, 3, 1, 1, 3)

        grid.addWidget(lblcontact, 4, 0)
        grid.addWidget(self.contactEdit, 4, 1, 1, 3)

        grid.addWidget(lblemail, 5, 0)
        grid.addWidget(self.emailEdit, 5, 1, 1, 3)

        grid.addWidget(lbladd, 6, 0)
        grid.addWidget(self.addEdit, 6, 1, 1, 3)

        #grid.addWidget(lblentry, 6, 0)
        #grid.addWidget(self.entryedit, 6, 1, 1, 3)
        grid.addWidget(self.btnupdate, 7, 1)
        grid.addWidget(self.btndelete, 7, 2)
        self.sidcombo.addItem("Choose Supplier Id")
        self.PrepareComboItems()
        self.sidcombo.currentTextChanged.connect(self.ChangeCombo)
        self.btndelete.clicked.connect(self.DeleteSupplier)
        self.btnupdate.clicked.connect(self.UpdateSupplier)

        self.setLayout(grid)

        self.show()

    def PrepareComboItems(self):
        con=Connections.Connection()
        table_name="supplierinfo"
        column_values=("SupplierId","SupplierName","GSTno","contact","EmailId","Address")
        query=con.CreateSelectQuery(column_values,table_name)
        self.sup_records=con.ExecuteQuery(query)
        if len(self.sup_records)>0:
            for record in self.sup_records:
                value=record[1]+"("+str(record[0])+")"
                self.sidcombo.addItem(value)

    def ChangeCombo(self):
        try:
            index=self.sidcombo.currentIndex()
            if index > 0 and (index - 1) <= len(self.sup_records):
                record=self.sup_records[index-1]
                self.snameEdit.setText(record[1])
                self.gstnoEdit.setText(str(record[2]))
                self.contactEdit.setText(str(record[3]))
                self.emailEdit.setText(record[4])
                self.addEdit.setText(record[5])
            else:
                self.cnameEdit.setText("")
                self.gstnoEdit.setText("")
                self.contactEdit.setText("")
                self.emailEdit.setText('')
                self.addEdit.setText("")
        except BaseException as ex:
            print(ex)

    def DeleteSupplier(self):
        try:
            res=ShowConfirmation(self)
            message=""
            if res==QMessageBox.Yes:
                sid=self.sidcombo.currentIndex()
                if sid>0:
                    record=self.sup_records[sid-1]
                    supid=str(record[0])
                    con=Connections.Connection()
                    table_name="supplierinfo"
                    primary_value={"SupplierId":supid}
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

    def UpdateSupplier(self):
        res=ShowConfirmation(self)
        sid=self.sidcombo.currentIndex()
        message=""
        if res==QMessageBox.Yes:
            if sid>0:
                record=self.sup_records[sid-1]
                sid=record[0]
                sname=self.snameEdit.text()
                gstno = self.gstnoEdit.text()
                contact=self.contactEdit.text()
                email=self.emailEdit.text()
                add=self.addEdit.text()

                if IsEmpty(sname) or IsEmpty(gstno) or IsEmpty(contact) or IsEmpty(add):
                    message+="Enter all the required Details\n\n"
                if  not ValidContact(contact):
                    message+="Enter a valid ContactNo\n\n"
                else:
                    con=Connections.Connection()
                    table_name="supplierinfo"
                    primary_value={'SupplierId':sid}
                    column_values={"SupplierName":sname,"GSTno":gstno,"contact":contact,"EmailId":email,"Address":add}
                    query=con.CreateUpdateQuery(table_name,column_values,primary_value)
                    print(query)
                    if con.InsertQuery(query):
                        message="Updation happened Successfully"
                    else:
                        message="Updation Error Due To: "+con.GetErrorMessage()

        else:
            message="Updation Cancelled"
        ShowMessageDialog(self, message)
