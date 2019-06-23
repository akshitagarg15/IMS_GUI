from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class ViewItemById(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.setWindowTitle("View Item BY ID Screen")
        self.setGeometry(300, 100, 500, 400)
        grid = QGridLayout()
        grid.setSpacing(10)
        lblitemid=QLabel("Enter Item Id")
        self.itemidEdit=QLineEdit()
        self.btn=QPushButton("View")
        self.tablewidget=QTableWidget()
        newfont = QFont("Bell MT", 18, QFont.Bold)
        lblitemid.setFont(newfont)
        self.itemidEdit.setFont(newfont)
        self.btn.setFont(newfont)

        grid.addWidget(lblitemid,1,0,1,2)
        grid.addWidget(self.itemidEdit, 2, 0, 1, 2)
        grid.addWidget(self.btn,3,0,1,2)
        grid.addWidget(self.tablewidget, 4, 0)
        self.btn.clicked.connect(self.ViewDetails)
        self.itemidEdit.setToolTip("Enter Id of item to view its details")
        self.btn.setToolTip("Click to view record of item")
        self.tablewidget.setStyleSheet("background-color:#CCDADA;")
        self.setLayout(grid)
        #self.show()

    def ViewDetails(self):
        try:
            message=""
            id=int(self.itemidEdit.text())

            print(4)
            if id >0:
                print(id)
                column_headers = ("ItemId", "ItemName", "SubCategoryId", "AvailableQty", "Price")
                self.tablewidget.setColumnCount(5)
                self.tablewidget.setHorizontalHeaderLabels(column_headers)
                con = Connections.Connection()
                print(1)
                query = "select * from iteminfo where ItemId="+str(id)
                print(query)
                row=0
                records = con.ExecuteQuery(query)
                print(records)
                if len(records)>0:
                    self.tablewidget.setRowCount(1)
                    for record in records:
                        self.tablewidget.setItem(row, 0, QTableWidgetItem(str(record[0])))
                        self.tablewidget.setItem(row, 1, QTableWidgetItem(record[1]))
                        self.tablewidget.setItem(row, 2, QTableWidgetItem(str(record[2])))
                        self.tablewidget.setItem(row, 3, QTableWidgetItem(str(record[3])))
                        self.tablewidget.setItem(row, 4, QTableWidgetItem(str(record[4])))
                        message="Record is Displayed"
                else:
                    self.tablewidget.setRowCount(1)
                    self.tablewidget.setItem(row, 0, QTableWidgetItem(str("No Record")))
                    self.tablewidget.setItem(row, 1, QTableWidgetItem(str("No Record")))
                    self.tablewidget.setItem(row, 2, QTableWidgetItem(str("No Record")))
                    self.tablewidget.setItem(row, 3, QTableWidgetItem(str("No Record")))
                    self.tablewidget.setItem(row, 4, QTableWidgetItem(str("No Record")))
                    message="Record does not exist"
            else:
                message="Enter a Valid Item Id"
            ShowMessageDialog(self,message)
        except BaseException as ex:
            print(ex)
