from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class AddSupplierBrandInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.brand_records=list()
        self.supplier_records = list()
        self.setWindowTitle("SupplierBrand details screen")
        grid = QGridLayout()
        grid.setSpacing(10)
        newfont=QFont("Bell MT", 18, QFont.Bold)

        lblbrandid=QLabel("Choose BrandId")
        lblsupid = QLabel("Choose SupplierId")
        self.brandcombo=QComboBox()
        self.suppliercombo = QComboBox()
        self.btn=QPushButton("Add SupplierBrand Info")
        lblbrandid.setFont(newfont)
        lblsupid.setFont(newfont)
        self.brandcombo.setFont(newfont)
        self.suppliercombo.setFont(newfont)
        self.btn.setFont(newfont)
        self.brandcombo.addItem("Choose BrandId")
        self.suppliercombo.addItem("Choose SupplierId")

        grid.addWidget(lblbrandid,1,0)
        grid.addWidget(self.brandcombo,1,1,1,2)

        grid.addWidget(lblsupid, 2, 0)
        grid.addWidget(self.suppliercombo, 2, 1,1, 2)
        grid.addWidget(self.btn, 3, 0, 1, 3)

        self.PrepareComboData()
        self.btn.clicked.connect(self.AddDetails)
        self.setLayout(grid)
        self.brandcombo.setToolTip("choose a brandId")
        self.suppliercombo.setToolTip("select supplier who supplies above selected brand")



        #self.show()

    def PrepareComboData(self):
        con=Connections.Connection()
        column_values=("BrandID","BrandName")
        table_name="brandinfo"
        query=con.CreateSelectQuery(column_values,table_name)
        self.brand_records=con.ExecuteQuery(query)
        if len(self.brand_records)>0:
            for record in self.brand_records:
                value=record[1]+"("+str(record[0])+")"
                self.brandcombo.addItem(value)

        column_values = ("SupplierID", "SupplierName")
        table_name = "supplierinfo"
        query = con.CreateSelectQuery(column_values, table_name)
        self.supplier_records = con.ExecuteQuery(query)
        if len(self.supplier_records) > 0:
            for record in self.supplier_records:
                value = record[1] + "(" + str(record[0]) + ")"
                self.suppliercombo.addItem(value)

    def AddDetails(self):
        message=""
        if "Choose" not in self.brandcombo.currentText() and "Choose" not in self.suppliercombo.currentText():
            supid = self.suppliercombo.currentIndex()
            bid = self.brandcombo.currentIndex()

            brand_record=self.brand_records[bid-1]
            brandid=str(brand_record[0])
            sup_record=self.supplier_records[supid-1]
            supplierid=str(sup_record[0])

            con = Connections.Connection()
            table_name = "supplierbrandinfo"
            column_values = {"BrandId": brandid, "SupplierId": supplierid}
            query = con.CreateInsertQuery(table_name, column_values)

            if con.InsertQuery(query):
                message = "Insertion happpenened successfully"
            else:
                message = "Insertion Failure due to: " + con.GetErrorMessage()
        else:
            message = "Select The Required Options"
        ShowMessageDialog(self, message)
