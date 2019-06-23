from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *


class ViewBrandBySubCat(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.records=list()
        self.brand_records=list()
        self.setWindowTitle("BrandList")
        self.layout = QGridLayout()
        newfont = QFont("Bell MT", 18, QFont.Bold)
        self.setGeometry(50,50,500,300)

        lblsid=QLabel("Enter SubCategory Id")
        self.sidEdit=QLineEdit()
        self.btn=QPushButton("Click To View")
        lblsid.setFont(newfont)
        self.sidEdit.setFont(newfont)
        self.btn.setFont(newfont)
        self.tableWidget=QTableWidget()

        self.layout.addWidget(lblsid,1,0,1,2)
        self.layout.addWidget(self.sidEdit,2,0,1,2)
        self.layout.addWidget(self.btn,3,0,1,2)
        self.layout.addWidget(self.tableWidget)
        self.btn.clicked.connect(self.View)
        #self.PrepareTableData()

        self.setLayout(self.layout)
        self.show()

    def View(self):
        try:
            message=""
            sid=self.sidEdit.text()
            if IsEmpty(sid):
                message="Enter SubCategoryId"
            elif not IsNumber(sid):
                message="Enter Id in Digits"
            if sid is not None:
                con=Connections.Connection()
                self.tableWidget.setColumnCount(1)
                column_headers = "BrandName"
                self.tableWidget.setHorizontalHeaderLabels(column_headers)
                table_name="brandsubcategoryinfo"
                column_value=("BrandId")
                query=con.CreateSelectQuery(column_value,table_name)
                query+="where SubCategoryId="+sid
                print(query)
                self.records=con.ExecuteQuery(query)
                print(self.records)
                if self.records is not None:
                    val=self.records[1]
                    #for record in self.records:
                else:
                    message="SubCategory Id do not Exist"
            ShowMessageDialog(self,message)
        except BaseException as ex:
            print(ex)