from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class ViewItemInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.setWindowTitle("View Item Details Screen")
        self.setGeometry(300, 100, 500, 400)
        self.layout=QVBoxLayout()
        self.tablewidget=QTableWidget()
        self.tablewidget.setStyleSheet("background-color:#CCDADA;")

        self.tablewidget.setColumnCount(5)
        column_headers=('ItemId','ItemName','SubCategoryName','AvailableQty','Price')
        self.tablewidget.setHorizontalHeaderLabels(column_headers)
        self.layout.addWidget(self.tablewidget)
        self.PrepareTableData()

        self.setLayout(self.layout)
        #self.show()

    def PrepareTableData(self):
        con=Connections.Connection()
        query="select ItemId,ItemName,SubCategoryId,AvailableQty,price from iteminfo"
        records=con.ExecuteQuery(query)
        query="select * from iteminfo natural join subcategoryinfo"
        cat_record= con.ExecuteQuery(query)
        print(cat_record)
        row=0

        if records is not None :
            self.tablewidget.setRowCount(len(records))
            for record in records:

                self.tablewidget.setItem(row,0,QTableWidgetItem(str(record[0])))
                self.tablewidget.setItem(row,1,QTableWidgetItem(record[1]))

                self.tablewidget.setItem(row, 3, QTableWidgetItem(str(record[3])))
                self.tablewidget.setItem(row, 4, QTableWidgetItem(str(record[4])))
                row+=1
        row=0
        if cat_record is not None:
            for record in cat_record:

                    self.tablewidget.setItem(row, 2, QTableWidgetItem(record[5]))
                    print(record[5])
                    row+=1


        else:
            self.tablewidget.setRowCount(1)
            self.tablewidget.setItem(row, 0, QTableWidgetItem("No Record"))
            self.tablewidget.setItem(row, 1, QTableWidgetItem("No Record"))
            self.tablewidget.setItem(row, 2, QTableWidgetItem("No Record"))
            self.tablewidget.setItem(row, 3, QTableWidgetItem("No Record"))
            self.tablewidget.setItem(row, 4, QTableWidgetItem("No Record"))

