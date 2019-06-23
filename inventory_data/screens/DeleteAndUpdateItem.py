from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class DeleteAndUpdateItem(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.item_records=list()
        self.subcat_records=list()
        self.setWindowTitle("Delete/Update Item Details Screen")
        self.setGeometry(300, 100, 500, 400)
        grid = QGridLayout()
        grid.setSpacing(10)
        lblitemid=QLabel("Choose Item Id")
        lblname=QLabel("Item Name")
        lblsubcat = QLabel("SubCategory Name")
        #lblavail = QLabel("Available Quantity")
        lblprice = QLabel("Item Price")
        newfont = QFont("Bell MT", 18, QFont.Bold)
        lblitemid.setFont(newfont)
        lblname.setFont(newfont)
        lblsubcat.setFont(newfont)
        #lblavail.setFont(newfont)
        lblprice.setFont(newfont)

        self.itemidcombo=QComboBox()
        self.nameEdit=QLineEdit()
        self.subcatcombo=QComboBox()
        #self.availEdit=QLineEdit()
        self.priceEdit=QLineEdit()
        self.btndelete=QPushButton("Delete Item")
        self.btnupdate = QPushButton("Update Item")
        self.itemidcombo.setFont(newfont)
        self.nameEdit.setFont(newfont)
        self.subcatcombo.setFont(newfont)
        #self.availEdit.setFont(newfont)
        self.priceEdit.setFont(newfont)
        self.btnupdate.setFont(newfont)
        self.btndelete.setFont(newfont)

        grid.addWidget(lblitemid,1,0)
        grid.addWidget(self.itemidcombo, 1, 1,1,3)

        grid.addWidget(lblname, 2, 0)
        grid.addWidget(self.nameEdit, 2, 1, 1, 3)

        grid.addWidget(lblsubcat, 3, 0)
        grid.addWidget(self.subcatcombo, 3, 1, 1, 3)

        #grid.addWidget(lblavail, 4, 0)
        #grid.addWidget(self.availEdit, 4, 1, 1, 3)

        grid.addWidget(lblprice, 5, 0)
        grid.addWidget(self.priceEdit, 5, 1, 1, 3)

        grid.addWidget(self.btndelete, 6, 0, 1, 2)
        grid.addWidget(self.btnupdate, 6, 2, 1, 2)
        self.itemidcombo.addItem("Choose Item Id")
        self.subcatcombo.addItem("Choose Subcategory")
        self.PrepareComboItems()
        self.itemidcombo.currentTextChanged.connect(self.ChangeCombo)
        self.btndelete.clicked.connect(self.DeleteItem)
        self.btnupdate.clicked.connect(self.UpdateItem)
        self.setLayout(grid)
        #self.show()

    def PrepareComboItems(self):
        con=Connections.Connection()
        query="select ItemId,ItemName from iteminfo"
        self.item_records=con.ExecuteQuery(query)
        if len(self.item_records)>0:
            for record in self.item_records:
                value=record[1]+"("+str(record[0])+")"
                self.itemidcombo.addItem(value)

        query = "select SubCategoryId,SubCategoryName from subcategoryinfo"
        self.subcat_records = con.ExecuteQuery(query)
        if len(self.subcat_records) > 0:
            for record in self.subcat_records:
                value = record[1] + "(" + str(record[0]) + ")"
                self.subcatcombo.addItem(value)

    def ChangeCombo(self):
        index=self.itemidcombo.currentIndex()
        if index>0 and (index-1)<=len(self.item_records):
            record=self.item_records[index-1]
            self.nameEdit.setText(record[1])
        else:
            self.nameEdit.setText("")


    def DeleteItem(self):
        try:
            id=self.itemidcombo.currentIndex()
            message=""
            if id>0:
                record=self.item_records[id-1]
                itemid=record[0]
                con=Connections.Connection()
                table_name="iteminfo"
                primary_value={'ItemId':itemid}
                query=con.CreateDeleteQuery(table_name,primary_value)
                print(query)
                res=ShowConfirmation(self)
                if res == QMessageBox.Yes:
                    if con.InsertQuery(query):
                        message="Deletion Happened Successfully"
                        self.PrepareComboItems()
                    else:
                        message="Deletion Failure Due To: "+con.GetErrorMessage()
                elif res == QMessageBox.No:
                    message="Item Not Deleted"
                else:
                    message  ="Good  Job"
            else:
                message="Enter the Item To Be Deleted"
            ShowMessageDialog(self,message)
        except BaseException as ex:
            print(ex)

    def UpdateItem(self):
        try:
            id=self.itemidcombo.currentIndex()
            message=""
            if id>0:

                sid = self.subcatcombo.currentIndex()

                record=self.item_records[id-1]
                itemid=record[0]
                iname=self.nameEdit.text()
                #aval=self.availEdit.text()
                price=self.priceEdit.text()
                allvalid=True
                if sid>0:
                    subrecord=self.subcat_records[sid-1]
                    subid=subrecord[0]

                else:
                    message+="Choose SubCategory\n\n"
                    allvalid=False

                if IsEmpty(price):
                    message+="Enter Item Price"
                    allvalid=False
                elif  int(price)>0:
                    iprice=price
                else:
                    message+="Enter a valid value"
                    allvalid=False
            res=ShowConfirmation(self)
            if res==QMessageBox.Yes:
                if allvalid==True:
                    con=Connections.Connection()
                    table_name="iteminfo"
                    column_values={"ItemName":iname,"SubCategoryId":subid,"AvailableQty":avail,"Price":iprice}
                    primary_value={"ItemId":itemid}
                    query=con.CreateUpdateQuery(table_name,column_values,primary_value)
                    print(query)
                    if con.InsertQuery(query):
                        message="Item Info Updated Successfully"
                    else:
                        message="Updation Error Due To: "+con.GetErrorMessage()
            else:
                message="Item Is Not Updated"
            ShowMessageDialog(self,message)
        except BaseException as ex:
            print(ex)
