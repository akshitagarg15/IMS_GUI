from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class AddBrandSubcategoryScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.brand_records=list()
        self.subcategory_records = list()
        self.setWindowTitle("SubCategory Details")
        grid=QGridLayout()
        grid.setSpacing(10)
        #initialize the widgets
        lblbrandcombo = QLabel("Choose Brand")
        lblsubcategorycombo=QLabel("Choose Category")
        self.brandcombo=QComboBox()
        self.subcategorycombo = QComboBox()

        newfont = QFont("Bell MT", 18, QFont.Bold)
        lblsubcategorycombo.setFont(newfont)
        lblbrandcombo.setFont(newfont)
        self.subcategorycombo.addItem("Choose A SubCategory")
        self.subcategorycombo.setFont(newfont)
        self.brandcombo.addItem("Choose A Brand")
        self.brandcombo.setFont(newfont)
        self.btn=QPushButton("Add Details")
        self.btn.setFont(newfont)
        self.btn.clicked.connect(self.AddDetails)

        #setting the widgets
        grid.addWidget(lblbrandcombo,1,0)
        grid.addWidget(self.brandcombo, 1, 1,1,2)
        grid.addWidget(lblsubcategorycombo, 2, 0)
        grid.addWidget(self.subcategorycombo, 2, 1, 1, 2)
        grid.addWidget(self.btn, 3, 0,1,3)
        self.PrepareComboBox()
        self.brandcombo.setToolTip("Choose a brandId to be added")
        self.subcategorycombo.setToolTip("Choose Subcategory which belongs to that brand")
        self.setLayout(grid)





    def PrepareComboBox(self):
        con=Connections.Connection()
        query="select SubCategoryId,SubCategoryName from subcategoryinfo"
        self.subcategory_records=con.ExecuteQuery(query)
        if len(self.subcategory_records)>0:
            for record in self.subcategory_records:
                value=record[1]+"("+str(record[0])+")"
                self.subcategorycombo.addItem(value)
        query = "select BrandId,BrandName from brandinfo"
        self.brand_records = con.ExecuteQuery(query)
        if len(self.brand_records) > 0:
            for record in self.brand_records:
                value = record[1] + "(" + str(record[0]) + ")"
                self.brandcombo.addItem(value)

    def AddDetails(self):
        try:
            message=""
            if "Choose" not in self.subcategorycombo.currentText() and "Choose" not in self.brandcombo.currentText():
                subcatid = self.subcategorycombo.currentIndex()
                bid = self.brandcombo.currentIndex()

                sub_record = self.subcategory_records[subcatid - 1]
                subcategoryid = sub_record[0]

                brand_record = self.brand_records[bid - 1]
                brandid =brand_record[0]
                con=Connections.Connection()
                table_name="brandsubcategoryinfo"
                column_values={"BrandId":brandid,"SubCategoryId":subcategoryid}
                query=con.CreateInsertQuery(table_name,column_values)

                if con.InsertQuery(query):
                    message="Insertion happpenened successfully"
                else:
                    message="Insertion Failure due to: "+con.GetErrorMessage()
            else:
                message="Select All Required Choices"
            ShowMessageDialog(self,message)
        except BaseException as ex:
            print(ex)