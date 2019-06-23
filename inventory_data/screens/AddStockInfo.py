from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import datetime
import sys


class AddStockInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.item_records=list()
        self.setWindowTitle("Add Stock details screen")
        grid = QGridLayout()
        grid.setSpacing(10)
        newfont = QFont("Bell MT", 18, QFont.Bold)

        # Initialize the widgets
        lblitemid = QLabel("Choose Item ID")
        lblstocktype = QLabel("Select StockType")
        lblqty = QLabel("Enter Quantity")
        lblprice = QLabel("Price")
        lblexpirydate=QLabel("Select ExpiryDate")

        lbldiscount = QLabel("Enter Discount")

        self.itemcombo=QComboBox()
        self.rbstockin=QRadioButton("IN")
        self.rbstockout = QRadioButton("OUT")
        self.qtyEdit=QLineEdit()
        self.priceEdit=QLineEdit()
        self.discountEdit = QLineEdit()
        self.btn=QPushButton("Add StockInfo")
        #self.expirydate=QCalendarWidget()
        #self.expirydate.setGridVisible(True)
        self.expirydate=QDateEdit()
        grid.setContentsMargins(0, 0, 0, 0)
        self.expirydate.setCalendarPopup(True)
        self.expirydate.calendarWidget().installEventFilter(self)
        self.expirydate.setFont(newfont)

        lblprice.setFont(newfont)
        lbldiscount.setFont(newfont)
        lblqty.setFont(newfont)
        lblexpirydate.setFont(newfont)
        lblstocktype.setFont(newfont)
        lblqty.setFont(newfont)
        lblitemid.setFont(newfont)
        self.itemcombo.setFont(newfont)
        self.rbstockout.setFont(newfont)
        self.rbstockin.setFont(newfont)
        self.qtyEdit.setFont(newfont)
        self.discountEdit.setFont(newfont)
        self.priceEdit.setFont(newfont)
        self.btn.setFont(newfont)
        self.rbstockout.setToolTip("Select if stock is to remove from inventory")
        self.rbstockin.setToolTip("Select if stock is to be added in inventory")
        self.itemcombo.setToolTip("Choose item whose stock operation to be performed")
        self.qtyEdit.setToolTip("enter quantity of item")
        self.priceEdit.setToolTip("enter price of item")
        self.expirydate.setToolTip("select expiry date of item")
        #Adding Image
        try:

            #lblpic=QLabel(self)
            #pixmap=QPixmap("inventory-track.gif")
            #lblpic.setPixmap(pixmap)

            self.movie = QMovie('inventory-track.gif', QByteArray(), self)
            size = self.movie.scaledSize()
            self.movie_screen = QLabel()
            self.movie_screen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.movie.setCacheMode(QMovie.CacheAll)
            self.movie.setSpeed(75)
            self.movie_screen.setAlignment(Qt.AlignCenter)

            grid.addWidget(self.movie_screen, 3,10 , 5, 20)


            grid.addWidget(lblitemid,1,0)
            grid.addWidget(self.itemcombo,1,1,1,2)

            grid.addWidget(lblstocktype, 2, 0)
            grid.addWidget(self.rbstockin, 2, 1)
            grid.addWidget(self.rbstockout, 2, 2)

            grid.addWidget(lblqty, 3, 0)
            grid.addWidget(self.qtyEdit, 3, 1,1,2)

            grid.addWidget(lblqty, 4, 0)
            grid.addWidget(self.qtyEdit, 4, 1,1,2)

            grid.addWidget(lblprice, 5, 0)
            grid.addWidget(self.priceEdit, 5, 1,1,2)


            grid.addWidget(lbldiscount, 6, 0)
            grid.addWidget(self.discountEdit, 6, 1,1,2)
            grid.addWidget(lblexpirydate, 7, 0)
            grid.addWidget(self.expirydate, 7, 1,1,2)
            grid.addWidget(self.btn, 8, 0, 1, 3)
        except BaseException as ex:
            print(ex)
        self.itemcombo.addItem("Choose Item")
        self.PrepareComboItems()

        self.btn.clicked.connect(self.AddStockDetails)

        self.setLayout(grid)
        #self.show()

    def PrepareComboItems(self):
        con=Connections.Connection()
        table_name="iteminfo"
        column_values=("ItemId","ItemName","AvailableQty","Price")
        query=con.CreateSelectQuery(column_values,table_name)
        self.item_records=con.ExecuteQuery(query)
        if len(self.item_records)>0:
            for record in self.item_records:
                value=record[1]+"("+str(record[0])+")"+",Rs."+str(record[3])
                self.itemcombo.addItem(value)


    def AddStockDetails(self):
        try:
            itemid=self.itemcombo.currentIndex()
            message=""
            allvalid = True
            if itemid>0:
                record=self.item_records[itemid-1]
                itemId=record[0]
                availableqty=record[2]
                print(availableqty)
                print(type(availableqty))
                stocktype=""
                price=self.priceEdit.text()
                qty=self.qtyEdit.text()
                print(qty)
                print(type(qty))
                discount=self.discountEdit.text()
                expirydate=self.expirydate.text()
                #expdate=self.expirydate.selectedDate()
                #expirydate=str(expdate.year())+"-"+str(expdate.month())+"-"+str(expdate.day())

                if self.rbstockin.isChecked():
                    availableqty+=int(qty)
                    stocktype="IN"
                    print(2)
                elif self.rbstockout.isChecked():
                    if int(qty)<=availableqty:
                        message += "Available Stock is less than requested\n\n"
                    else:
                        availableqty-=int(qty)
                        stocktype="OUT"
                elif availableqty==0:
                    message+="Out of Stock\n\n"
                else:
                    message+="Available Stock is less than requested\n\n"
                if IsEmpty(expirydate):
                    message+="Enter Expiry Date Of Stock\n\n"


                if IsEmpty(qty):
                    message+="Enter the stock quantity\n\n"
                    allvalid=False

                elif not IsNumber(qty) and not IsFloat(qty):
                    message+="Enter valid stock quantity\n\n"
                    allvalid = False
                if IsEmpty(discount):
                    message += "Enter the item discount\n\n"
                    allvalid = False
                elif not IsNumber(discount) and not IsFloat(discount):
                    message += "Enter valid discount number\n\n"
                    allvalid = False
                if IsEmpty(price):
                    message+="Enter Current Item Price\n\n"
                    allvalid=False
                elif not IsFloat(price):
                    message+="Enter a valid price"
                    allvalid=False
                if IsEmpty(expirydate):
                    message+="Enter expiry date"

                expirydate = str(expirydate)
                expirydate = expirydate.split('-')
                ExpiryDate = str(expirydate[2]) + "-" + str(expirydate[1]) + "-" + str(expirydate[0])




                if allvalid==True:
                    con = Connections.Connection()
                    table_name = "iteminfo"
                    column_value = {"AvailableQty": availableqty,"Price":price}
                    primary_value = {"ItemId": itemId}
                    query = con.CreateUpdateQuery(table_name, column_value, primary_value)
                    print(query)
                    if con.InsertQuery(query):
                        table_name = "stockinfo"
                        column_value = {"ItemId": itemId, "StockType": stocktype, "Qty": qty, "Price": price,
                                        "ExpiryDate":str(ExpiryDate),"Discount": discount}
                        query = con.CreateInsertQuery(table_name, column_value)
                        print(query)
                        if con.InsertQuery(query):
                            message += "Stock Details Added Successfully"
                        else:
                            message += "Stock Details Insertion Failure Due To: " + con.GetErrorMessage()
                    else:
                        message+= "Item Stock Not Updated\n\n"


            else:
                message="Choose Item ID"
            ShowMessageDialog(self,message)
        except BaseException as ex:
            print(ex)

