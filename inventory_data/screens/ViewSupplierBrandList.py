from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import datetime

class ViewSupplierBrandList(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        try:
            #self.Sup_name=list()
            self.supplier_records=list()
            #self.subcatID=list()
            self.brand_records=list()
            self.setWindowTitle("Supplier/Brand List")
            grid= QGridLayout()
            self.setGeometry(50,50,500,500)
            self.rbbrand=QPushButton("Brand List")
            self.rbsup = QPushButton("Supplier List")
            self.brandcombo=QComboBox()
            self.supcombo=QComboBox()
            newfont = QFont("Bell MT", 18, QFont.Bold)
            btnfont=QFont("consolas",18,QFont.Bold)
            self.rbbrand.setFont(btnfont)
            self.rbsup.setFont(btnfont)
            self.brandcombo.setFont(newfont)
            self.supcombo.setFont(newfont)
            self.tableWidget = QTableWidget()
            self.setStyleSheet("Font-Size:20px;background-color:#CCDADA;")
            self.tableWidget.setColumnCount(2)



            grid.addWidget(self.supcombo,1,1,1,2)
            grid.addWidget(self.tableWidget,1,5,5,10)
            grid.addWidget(self.rbbrand,2,1,1,2)

            grid.addWidget(self.brandcombo, 4,1 , 1, 2)
            grid.addWidget(self.rbsup,5, 1, 1, 2)
            self.tableWidget.setStyleSheet("background-color:#CCDADA;")
            self.brandcombo.addItem("Choose BrandID")
            self.supcombo.addItem("Choose SupplierID")
            self.PrepareCombo()
            self.setLayout(grid)
            self.rbsup.clicked.connect(self.SupplierList)
            self.rbbrand.clicked.connect(self.BrandList)
            self.brandcombo.setToolTip(" Choose a brand whose all supplier's list you want")
            self.supcombo.setToolTip(" Choose a supplier whose all brand's list you want")
            self.rbbrand.setToolTip("Click to generate list of all brands that selected supplier supplies")
            self.rbbrand.setToolTip("Click to generate list of all suppliers for selected brand ")
            #self.show()
        except BaseException as ex:
            print(ex)
    def PrepareCombo(self):
        con=Connections.Connection()
        table_name="brandinfo"
        column_value=("BrandId","BrandName")
        query=con.CreateSelectQuery(column_value,table_name)
        self.brand_records=con.ExecuteQuery(query)
        if self.brand_records is not None:
            for record in self.brand_records:
                value=record[1]+" ("+str(record[0])+")"
                self.brandcombo.addItem(value)

        table_name = "supplierinfo"
        column_value = ("SupplierId", "SupplierName")
        query = con.CreateSelectQuery(column_value, table_name)
        self.supplier_records = con.ExecuteQuery(query)
        if self.supplier_records is not None:
            for record in self.supplier_records:
                value = record[1] + " (" + str(record[0]) + ")"
                self.supcombo.addItem(value)

    def SupplierList(self):
        try:
            bid = self.brandcombo.currentIndex()
            if bid > 0:
                self.tableWidget.setColumnCount(2)
                column_value = ("SupplierId", "SupplierName")
                self.tableWidget.setHorizontalHeaderLabels(column_value)

                record = self.brand_records[bid - 1]
                brandId = record[0]
                print(brandId)
                con = Connections.Connection()
                query = "select * from supplierinfo where SupplierId in (select SupplierId from supplierbrandinfo where BrandId= "
                query += str(brandId) + ")"
                #print(query)
                self.records = con.ExecuteQuery(query)
                #print(self.records)
                row = 0
                if self.records is not None:
                    self.tableWidget.setRowCount(len(self.records))
                    for ch in self.records:
                        self.tableWidget.setItem(row, 0, QTableWidgetItem(str(ch[0])))
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(ch[1]))
        except BaseException as ex:
            print(ex)


    def BrandList(self):
        try:
            sid=self.supcombo.currentIndex()
            if sid >0:
                self.tableWidget.setColumnCount(2)
                column_value=("BrandId","BrandName")
                self.tableWidget.setHorizontalHeaderLabels(column_value)


                record= self.supplier_records[sid-1]
                supId=record[0]
                #print(subcatId)
                con=Connections.Connection()
                query="select * from brandinfo where BrandId in (select BrandId from supplierbrandinfo where SupplierId= "
                query+= str(supId)+")"
                print(query)
                self.records=con.ExecuteQuery(query)
                print(self.records)
                row=0
                if self.records is not None:
                    self.tableWidget.setRowCount(len(self.records))
                    for ch in self.records:
                        self.tableWidget.setItem(row,0,QTableWidgetItem(str(ch[0])))
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(ch[1]))
                        row+=1
        except BaseException as ex:
            print(ex)
