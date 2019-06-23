from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import datetime

class ViewBrandSubCategoryWithOption(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.SubCat_name=list()
        self.subcat_records=list()
        self.subcatID=list()
        self.brand_records=list()
        self.setWindowTitle("Brand/SubCategory List")
        grid= QGridLayout()
        self.setGeometry(50,50,500,500)
        self.rbbrand=QPushButton("Brand List")
        self.rbcat = QPushButton("SubCategory List")
        self.brandcombo=QComboBox()
        self.subcatcombo=QComboBox()
        newfont = QFont("Bell MT", 18, QFont.Bold)
        btnfont=QFont("consolas",18,QFont.Bold)
        self.rbbrand.setFont(btnfont)
        self.rbcat.setFont(btnfont)
        self.brandcombo.setFont(newfont)
        self.subcatcombo.setFont(newfont)
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(1)



        grid.addWidget(self.subcatcombo,1,1,1,2)
        grid.addWidget(self.tableWidget,1,5,5,10)
        grid.addWidget(self.rbbrand,2,1,1,2)

        grid.addWidget(self.brandcombo, 4,1 , 1, 2)
        grid.addWidget(self.rbcat,5, 1, 1, 2)
        self.brandcombo.addItem("Choose BrandID")
        self.subcatcombo.addItem("Choose SubCatID")
        self.setLayout(grid)
        self.rbcat.clicked.connect(self.SubCatList)
        self.rbbrand.clicked.connect(self.BrandList)
        self.PrepareCombo()
        self.brandcombo.setToolTip("Select brand for which you want subcategory list")
        self.subcatcombo.setToolTip("Select subcategory  for which you want brand list")
        self.rbcat.setToolTip("To generate list of subcategory of selected brand")
        self.rbbrand.setToolTip("To generate list of brand for selected subcategory")

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

        table_name = "subcategoryinfo"
        column_value = ("SubCategoryId", "SubCategoryName")
        query = con.CreateSelectQuery(column_value, table_name)
        self.subcat_records = con.ExecuteQuery(query)
        if self.subcat_records is not None:
            for record in self.subcat_records:
                value = record[1] + " (" + str(record[0]) + ")"
                self.subcatcombo.addItem(value)

    def SubCatList(self):
        try:
            bid = self.brandcombo.currentIndex()
            if bid > 0:
                self.tableWidget.setColumnCount(2)
                column_value = ("SubCategoryId", "SubCategoryName")
                self.tableWidget.setHorizontalHeaderLabels(column_value)

                record = self.brand_records[bid - 1]
                brandId = record[0]
                print(brandId)
                con = Connections.Connection()
                query = "select * from subcategoryinfo where SubCategoryId in (select SubCategoryId from brandsubcategoryinfo where BrandId= "
                query += str(brandId) + ")"
                print(query)
                self.records = con.ExecuteQuery(query)
                print(self.records)
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
            sid=self.subcatcombo.currentIndex()
            if sid >0:
                self.tableWidget.setColumnCount(2)
                column_value=("BrandId","BrandName")
                self.tableWidget.setHorizontalHeaderLabels(column_value)


                record= self.subcat_records[sid-1]
                subcatId=record[0]
                print(subcatId)
                con=Connections.Connection()
                query="select * from brandinfo where BrandId in (select BrandId from brandsubcategoryinfo where SubCategoryId= "
                query+= str(subcatId)+")"
                print(query)
                self.records=con.ExecuteQuery(query)
                print(self.records)
                row=0
                if self.records is not None:
                    self.tableWidget.setRowCount(len(self.records))
                    for ch in self.records:
                        self.tableWidget.setItem(row,0,QTableWidgetItem(str(ch[0])))
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(ch[1]))
        except BaseException as ex:
            print(ex)
