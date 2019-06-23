from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class AddCategoryScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.setWindowTitle("Category Details")
        #self.setGeometry(100,100,300,150)

        #Initilize the Widgets
        #LblCategoryId=QLabel("Category ID")
        LblCategoryName=QLabel("Category Name")
        NewFont=QFont("Bell MT",18,QFont.Bold)

        self.CategoryNameEdit=QLineEdit()
        self.btn=QPushButton("Add Category")
        self.btn.clicked.connect(self.AddCategory)
        LblCategoryName.setFont(NewFont)
        self.CategoryNameEdit.setFont(NewFont)
        self.btn.setFont(NewFont )
        self.CategoryNameEdit.setToolTip("Enter new category name")
        self.btn.setToolTip("click to add category name")
        #Prepare the layout
        Grid=QGridLayout()
        Grid.setSpacing(10)



        Grid.addWidget(LblCategoryName, 2, 0)
        Grid.addWidget(self.CategoryNameEdit, 2, 1,1,2)
        Grid.addWidget(self.btn, 3, 0, 1, 3)

        self.setLayout(Grid)
        #self.show()

    def AddCategory(self):
        cname=self.CategoryNameEdit.text()
        message=""
        if IsEmpty(cname):
            message="Fill the box"

        elif IsNumber(cname):
            message="enter a valid category name"
        else:
            CatName=str(cname)
            table_name="categoryinfo"
            column_values=dict()
            column_values["CategoryName"]=CatName
            con=Connections.Connection()
            query=con.CreateInsertQuery(table_name,column_values)
            if con.InsertQuery(query):
                message="Category information saved in database"
            else:
                message="Insertion Failure Due To:"+ con.GetErrorMessage()
        ShowMessageDialog(self,message)

            


