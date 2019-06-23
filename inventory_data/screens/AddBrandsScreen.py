from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class AddBrandsScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.setWindowTitle("Brand Details")
        self.setGeometry(100,100,300,150)

        #Initilize the Widgets
       # LblBrandId=QLabel("Brand ID")
        LblBrandName=QLabel("Brand Name")
        NewFont=QFont("Bell MT",18,QFont.Bold)

        self.BrandNameEdit=QLineEdit()
        self.btn=QPushButton("ADD")
        self.btn.clicked.connect(self.AddBrand)
        self.btn.setToolTip("Add new brand")
        self.BrandNameEdit.setToolTip("Enter Brand Name")
        self.BrandNameEdit.setFont(NewFont)
        LblBrandName.setFont(NewFont)
        self.btn.setFont(NewFont)
        lbl=QLabel(self)
        pixmap=QPixmap("pic26.gif")
        lbl.setPixmap(pixmap)
        #self.btn.setStyleSheet("color:Sky Blue;Background-color:SKY BLUE;font-color=Blue: font-size:30px")
        #Prepare the layout
        Grid=QGridLayout()
        Grid.setSpacing(10)

        #Grid.addWidget(LblBrandId,1,0)

        Grid.addWidget(LblBrandName, 2, 0)

        Grid.addWidget(self.BrandNameEdit, 2, 1,1,2)
        Grid.addWidget(lbl, 3, 0)
        Grid.addWidget(self.btn, 3, 1, 1, 3)
        self.setLayout(Grid)
        #self.show()

    def AddBrand(self):
        bname=self.BrandNameEdit.text()
        message=""
        if IsEmpty(bname):
            message="Fill the box"
        elif IsAlphabet(bname):
            Bname=bname
            table_name="brandinfo"
            column_values={"BrandName":Bname}
            con=Connections.Connection()
            query=con.CreateInsertQuery(table_name,column_values)
            print(query)
            if con.InsertQuery(query):
                message="Brand name added in the database"
            else:
                message="Insertion Failure due to:"+ con.GetErrorMessage()
        else:
            if IsNumber(bname):
                message="enter a valid brand name"
        ShowMessageDialog(self,message)



