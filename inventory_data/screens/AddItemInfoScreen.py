from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class AddItemInfoScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.subcategory_records = list()
        self.setWindowTitle("Add Item Details Screen")
        self.setGeometry(300,100,500,400)
        grid = QGridLayout()
        grid.setSpacing(10)
        # initialize the widgets
        lblitemname = QLabel("Enter Item Name")
        lblsubcategorycombo = QLabel("Choose SubCategory")
        #lblavailable = QLabel("Enter Available Quantity")
        lblprice = QLabel("Enter Price")
        newfont = QFont("Bell MT", 18, QFont.Bold)
        lblitemname.setFont(newfont)
        lblsubcategorycombo.setFont(newfont)

        lblprice.setFont(newfont)
        self.itemnameEdit = QLineEdit()
        self.subcategorycombo = QComboBox()

        self.priceEdit = QLineEdit()
        self.btn=QPushButton()
        self.itemnameEdit.setFont(newfont)
        self.subcategorycombo.setFont(newfont)
        self.btn.setToolTip("Select to add new item info")
        self.subcategorycombo.setToolTip("Choose SubCategory of Item")
        self.priceEdit.setToolTip("Enter Price of Item")
        self.itemnameEdit.setToolTip("Enter new item name")
        self.priceEdit.setFont(newfont)
        self.btn.setFont(newfont)
        self.btn.setStyleSheet("background-image:url(bag.png);Background-repeat:no repeat;background-position:10% 50px;width:20%;height:150%")

        # setting the widgets
        grid.addWidget(lblitemname, 1, 0)
        grid.addWidget(self.itemnameEdit, 1, 1, 1, 2)
        grid.addWidget(lblsubcategorycombo, 2, 0)
        grid.addWidget(self.subcategorycombo, 2, 1, 1, 2)


        grid.addWidget(lblprice, 4, 0)
        grid.addWidget(self.priceEdit, 4, 1, 1, 2)
        #grid.addWidget(lbl, 5, 0, 1, 1)
        grid.addWidget(self.btn, 5, 1, 1, 4)
        self.subcategorycombo.addItem("Choose A SubCategory")
        self.btn.clicked.connect(self.AddItem)

        self.PrepareComboItems()
        self.setLayout(grid)
        #self.show()

    def PrepareComboItems(self):
        try:
            con=Connections.Connection()
            query="select SubCategoryId,SubCategoryName from subcategoryinfo"
            print(query)
            self.subcategory_records =con.ExecuteQuery(query)
            if len(self.subcategory_records )>0:
                for record in self.subcategory_records :
                    value=record[1]+"("+str(record[0])+")"
                    self.subcategorycombo.addItem(value)
        except BaseException as ex:
            print(ex)

    def AddItem(self):
        try:
            iname=self.itemnameEdit.text()
            sid=self.subcategorycombo.currentIndex()
            avail=0
            price=self.priceEdit.text()
            message=""

            AllValid=True
            if IsEmpty(iname):
                message+="Enter Item Name\n\n"
                AllValid=False

            if IsEmpty(price):
                message+="Enter item pice\n\n"
                AllValid = False
            elif IsNumber(price):
                if int(price) > 0:
                    iprice = price
                else:
                    message += "Enter Item Price\n\n"
                    AllValid = False


            if IsNumber(iname):
                message += "Enter a valid item name\n\n"
                AllValid = False



            if AllValid==True:
                if sid>0:
                    record=self.subcategory_records[sid-1]
                    subcatid=record[0]
                    con=Connections.Connection()
                    table_name="iteminfo"
                    column_values={"ItemName":iname,"SubCategoryId":subcatid,"AvailableQty":avail,"Price":iprice}
                    query=con.CreateInsertQuery(table_name,column_values)
                    print(query)
                    if con.InsertQuery(query):
                        message="Insertion is Successful"
                    else:
                        message="Insertion Failure Due To: "+con.GetErrorMessage()
            ShowMessageDialog(self,message)

        except BaseException as ex:
            print(ex)




