from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import datetime

class ViewCustomerInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.layout=QVBoxLayout()
        self.setWindowTitle("View Customer Details")
        self.setGeometry(50,50,550,600)
        newfont=QFont("Bell MT",18,QFont.Bold)
        self.tablewidget=QTableWidget()
        self.tablewidget.setColumnCount(6)
        column_headers=("Customer Id","Customer Name","Contact","Email Id","Address","Entry Date")
        self.tablewidget.setHorizontalHeaderLabels(column_headers)
        self.tablewidget.setStyleSheet("background-color:#CCDADA;Font-Size:20px")
        self.layout.addWidget(self.tablewidget)
        self.setLayout(self.layout)
        self.PrepareTableData()
        #self.show()

    def PrepareTableData(self):
        con=Connections.Connection()
        table_name="customerinfo"
        column_values=("CustomerId","customerName","contact","EmailId","Address","EntryDate")
        query=con.CreateSelectQuery(column_values,table_name)
        print(query)
        self.cust_records=con.ExecuteQuery(query)
        print(self.cust_records[0][4])
        row=0
        if self.cust_records is not None:
            self.tablewidget.setRowCount(len(self.cust_records))
            for record in self.cust_records:
                self.tablewidget.setItem(row,0,QTableWidgetItem(str(record[0])))
                self.tablewidget.setItem(row, 1, QTableWidgetItem(record[1]))
                self.tablewidget.setItem(row, 2, QTableWidgetItem(str(record[2])))
                self.tablewidget.setItem(row, 3, QTableWidgetItem(record[3]))
                self.tablewidget.setItem(row, 4, QTableWidgetItem(record[4]))
                self.tablewidget.setItem(row, 5, QTableWidgetItem(str(record[5])))
                row+=1

        else:
            self.tablewidget.setRowCount(1)
            for record in self.cust_records:
                self.tablewidget.setItem(row, 0, QTableWidgetItem("No Record"))
                self.tablewidget.setItem(row, 1, QTableWidgetItem("No Record"))
                self.tablewidget.setItem(row, 2, QTableWidgetItem("No Record"))
                self.tablewidget.setItem(row, 3, QTableWidgetItem("No Record"))
                self.tablewidget.setItem(row, 4, QTableWidgetItem("No Record"))
                self.tablewidget.setItem(row, 4, QTableWidgetItem("No Record"))
                row += 1