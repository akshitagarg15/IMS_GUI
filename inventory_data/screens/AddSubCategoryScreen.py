from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class AddSubCategoryScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.records=list()
        self.setWindowTitle("SubCategory Details")
        grid=QGridLayout()
        grid.setSpacing(10)
        #initialize the widgets
        lblsubcategoryname = QLabel("SubCategory Name")
        lblcategorycombo=QLabel("Choose Category")
        self.categorycombo=QComboBox()
        self.subcategorynameEdit = QLineEdit()
        newfont = QFont("Bell MT", 18, QFont.Bold)
        lblsubcategoryname.setFont(newfont)
        lblcategorycombo.setFont(newfont)
        self.subcategorynameEdit.setFont(newfont)
        self.categorycombo.addItem("Choose A Category")
        self.categorycombo.setFont(newfont)
        self.btn=QPushButton("Add SubCategory Details")
        self.btn.setFont(newfont)
        self.btn.clicked.connect(self.AddDetails)

        #setting the widgets
        grid.addWidget(lblsubcategoryname,1,0)
        grid.addWidget(self.subcategorynameEdit, 1, 1,1,2)
        grid.addWidget(lblcategorycombo, 2, 0)
        grid.addWidget(self.categorycombo, 2, 1, 1, 2)
        grid.addWidget(self.btn, 3, 0,1,3)
        self.PrepareComboBox()
        self.categorycombo.setToolTip("Select a category for new Subcategory of item")
        self.subcategorynameEdit.setToolTip("Enter new subcategoryname")

        self.setLayout(grid)





    def PrepareComboBox(self):
        con=Connections.Connection()
        query="select CategoryId,CategoryName from categoryinfo"
        self.records=con.ExecuteQuery(query)
        if len(self.records)>0:
            for record in self.records:
                value=record[1]+"("+str(record[0])+")"
                self.categorycombo.addItem(value)

    def AddDetails(self):
        try:
            message=""
            subname=self.subcategorynameEdit.text()

            catText=self.categorycombo.currentText()




            if IsEmpty(subname):
                message="Enter subcategory in box"
            elif IsNumber(subname):
                message = "Enter a valid subcategory name "

            elif "Choose" not in catText:
                catid = self.categorycombo.currentIndex()
                record = self.records[catid - 1]
                categoryid = record[0]
                con=Connections.Connection()
                table_name="subcategoryinfo"
                column_values={"SubcategoryName":subname,"CategoryId":categoryid}
                query=con.CreateInsertQuery(table_name,column_values)
                print(query)
                if con.InsertQuery(query):
                    message="Insertion happpenened successfully"
                else:
                    message="Insertion Failure due to: "+con.GetErrorMessage()
            else:
                message="Select a category"
            ShowMessageDialog(self,message)
        except BaseException as ex:
            print(ex)