from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class DeleteSupplierBrandInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        grid=QGridLayout()
        grid.setSpacing(10)
        newfont = QFont("Bell MT", 18, QFont.Bold)
        self.sup_records=list()
        self.brand_records=list()
        self.setWindowTitle("Delete SupplierBrandInfo Screen")
        self.sup_records=list()
        lblsupid=QLabel("Choose Supplier Id")
        self.supcombo=QComboBox()
        lblsupname=QLabel("Supplier Name")
        self.supnameEdit=QLineEdit()
        lblbname = QLabel("Brand Name")
        self.bnameEdit = QLineEdit()
        self.btndelete = QPushButton("Delete Info")
        lblsupid.setFont(newfont)
        lblbname.setFont(newfont)
        lblsupname.setFont(newfont)
        self.supcombo.setFont(newfont)
        self.bnameEdit.setFont(newfont)
        self.supnameEdit.setFont(newfont)
        self.btndelete.setFont(newfont)

        # Positoning of widgets
        grid.addWidget(lblsupid, 1, 0)
        grid.addWidget(self.supcombo, 1, 1, 1, 3)
        grid.addWidget(lblsupname, 2, 0)
        grid.addWidget(self.supnameEdit, 2, 1, 1, 3)
        grid.addWidget(lblbname, 3, 0)
        grid.addWidget(self.bnameEdit, 3, 1, 1, 3)
        grid.addWidget(self.btndelete, 4, 0, 1, 4)
        # grid.addWidget(self.btnupdate, 4, 2, 1, 2)
        self.supcombo.addItem("Choose Supplier")
        self.PrepareComboItems()
        self.supcombo.currentTextChanged.connect(self.ChangeCombo)
        self.btndelete.clicked.connect(self.DeleteInfo)
        self.supcombo.setToolTip("choose supplier whose brand detail to be deleted")
        self.bnameEdit.setToolTip("Automatically")
        self.setLayout(grid)

        #self.show()

    def PrepareComboItems(self):
        con=Connections.Connection()
        column_values = ("BrandId", "BrandName")
        table1 = "brandinfo"
        table2 = "supplierbrandinfo"
        query = con.CreateJoinQuery(column_values, table1, table2)

        self.brand_records = con.ExecuteQuery(query)
        print(self.brand_records)

        column_values = ("SupplierId", "SupplierName")
        table1 = "supplierinfo"
        table2 = "supplierbrandinfo"
        query = con.CreateJoinQuery(column_values, table1, table2)

        self.sup_records = con.ExecuteQuery(query)
        print(self.sup_records)

        if self.sup_records is not None:
            for record in self.sup_records:
                value = record[1] + "(" + str(record[0]) + ")"
                self.supcombo.addItem(value)

    def ChangeCombo(self):
        index = self.supcombo.currentIndex()
        if index > 0 and (index - 1) <= len(self.sup_records) and (index - 1) <= len(self.brand_records):
            record = self.brand_records[index - 1]
            suprecord = self.sup_records[index - 1]
            self.bnameEdit.setText(record[1])
            self.supnameEdit.setText(suprecord[1])
        else:
            self.bnameEdit.setText("")
            self.supnameEdit.setText("")

    def DeleteInfo(self):

        try:
            sid = self.supcombo.currentIndex()
            message = ""
            if sid > 0:
                con = Connections.Connection()
                index = sid
                record = self.sup_records[index - 1]
                sid = record[0]
                table_name = "supplierbrandinfo"
                primary_values = {"SupplierId": sid}
                query = con.CreateDeleteQuery(table_name, primary_values)
                print(query)
                res=ShowConfirmation(self)
                if res==QMessageBox.Yes:
                    if con.InsertQuery(query):
                        message = "Deletion happened successfully"
                        self.PrepareComboItems()
                    else:
                        message = "Deletion Failure Due To: " + con.GetErrorMessage()

                else:
                    message="Deletion not hsppened"
            ShowMessageDialog(self, message)
        except BaseException as ex:
            print(ex)
