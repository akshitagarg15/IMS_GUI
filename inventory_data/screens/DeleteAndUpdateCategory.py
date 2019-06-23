from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class DeleteAndUpdateCategory(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.setWindowTitle("Delete and Update Category Details")
        self.records=list()
        #self.setGeometry(100,100,300,150)

        #Initilize the Widgets
        lblcategoryId=QLabel("Choose Category ID")
        lblcname=QLabel("Category Name")
        NewFont=QFont("Bell MT",18,QFont.Bold)

        self.categorycombo=QComboBox()
        self.btn1=QPushButton("Delete Category")
        self.btn2 = QPushButton("Update Category")

        self.btn1.clicked.connect(self.DeleteCategory)
        self.btn2.clicked.connect(self.UpdateCategory)
        self.cnameEdit=QLineEdit()
        self.cnameEdit.setFont(NewFont)
        self.categorycombo.setFont(NewFont)
        lblcname.setFont(NewFont)
        lblcategoryId.setFont(NewFont)
        self.btn1.setFont(NewFont)
        self.btn2.setFont(NewFont)

        self.categorycombo.setToolTip("Choose category to delete/update")
        self.cnameEdit.setToolTip("Rewrite category name to update it")
        #Prepare the layout
        grid=QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(lblcategoryId, 1, 0)
        grid.addWidget(self.categorycombo, 1, 1,1,2)
        grid.addWidget(lblcname, 2, 0)
        grid.addWidget(self.cnameEdit, 2, 1,1,2)
        grid.addWidget(self.btn1, 3, 1, 1, 1)
        grid.addWidget(self.btn2, 3, 2, 1, 1)
        self.categorycombo.addItem("Choose A Category")
        self.PrepareComboItems()
        self.categorycombo.currentTextChanged.connect (self.ChangeCombo)
        self.setLayout(grid)
        #self.show()

    def PrepareComboItems(self):
        con=Connections.Connection()
        query="select CategoryId,CategoryName from categoryinfo"
        self.records=con.ExecuteQuery(query)
        if len(self.records)>0:
            for record in self.records:
                value=record[1]+"("+str(record[0])+")"
                self.categorycombo.addItem(value)

    def ChangeCombo(self,value):
        index = self.categorycombo.currentIndex()
        if index > 0 and (index - 1) <= len(self.records):
            record = self.records[index - 1]
            self.cnameEdit.setText(record[1])
        else:
            self.cnameEdit.setText("")


    def DeleteCategory(self):
        try:
            cid=self.categorycombo.currentIndex()
            message=""
            if cid>0:
                con=Connections.Connection()
                index=cid
                record=self.records[index-1]
                catId=record[0]
                table_name="categoryinfo"
                primary_values={"CategoryId":catId}
                query=con.CreateDeleteQuery(table_name,primary_values)
                print(query)
                if con.InsertQuery(query):
                    message="Deletion happened successfully"
                    self.PrepareComboItems()
                else:
                    message="Deletion Failure Due To: "+con.GetErrorMessage()
            ShowMessageDialog(self,message)
        except BaseException as ex:
            print(ex)

    def UpdateCategory(self):
        ShowConfirmation(self)
        try:
            cid = self.categorycombo.currentIndex()

            message = ""
            cname = self.cnameEdit.text()
            if cid > 0:

                index = cid

                record = self.records[index - 1]

                catId = record[0]

                con = Connections.Connection()
                table_name = "categoryinfo"
                column_value = {"CategoryName": cname}
                primary_value = {"CategoryId": catId}

                query = con.CreateUpdateQuery(table_name, column_value, primary_value)

                if con.InsertQuery(query):
                    message = "Updation Happened In Database"
                    self.PrepareComboItems()
                else:
                    print("Insertion Failure due to: " + con.GetErrorMessage())
            ShowMessageDialog(self, message)
        except BaseException as ex:
            print(ex)

