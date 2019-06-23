from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class ViewSupplierById(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.setWindowTitle("View Supplier BY Id Screen")
        self.setGeometry(300, 100, 500, 400)
        grid = QGridLayout()
        grid.setSpacing(10)
        lblsupplierid=QLabel("Enter Supplier Id")
        self.supplieridEdit=QLineEdit()
        self.btn=QPushButton("View")
        self.tablewidget=QTableWidget()
        self.tablewidget.setStyleSheet("background-color:#CCDADA;")
        newfont = QFont("Bell MT", 18, QFont.Bold)
        lblsupplierid.setFont(newfont)
        self.supplieridEdit.setFont(newfont)
        self.btn.setFont(newfont)

        grid.addWidget(lblsupplierid,1,0,1,2)
        grid.addWidget(self.supplieridEdit, 2, 0, 1, 2)
        grid.addWidget(self.btn,3,0,1,2)
        grid.addWidget(self.tablewidget, 4, 0)
        self.btn.clicked.connect(self.ViewDetails)
        self.setLayout(grid)
        #self.show()

    def ViewDetails(self):
        try:
            message=""
            id=self.supplieridEdit.text()
            if IsEmpty(id):
                message="Enter Supplier Id"
            elif not IsNumber(id):
                message="Enter Id In Digits"

            else:
                if id is not None:

                    column_headers = ("SupplierId", "SupplierName", "GSTno", "Contact", "EmailId","Address")
                    self.tablewidget.setColumnCount(6)
                    self.tablewidget.setHorizontalHeaderLabels(column_headers)
                    con = Connections.Connection()

                    query = "select * from supplierinfo where SupplierId="+str(id)
                    print(query)
                    row=0
                    records = con.ExecuteQuery(query)
                    if len(records)>0:
                        self.tablewidget.setRowCount(1)
                        for record in records:
                            self.tablewidget.setItem(row, 0, QTableWidgetItem(str(record[0])))
                            self.tablewidget.setItem(row, 1, QTableWidgetItem(record[1]))
                            self.tablewidget.setItem(row, 2, QTableWidgetItem(str(record[2])))
                            self.tablewidget.setItem(row, 3, QTableWidgetItem(str(record[3])))
                            self.tablewidget.setItem(row, 4, QTableWidgetItem(str(record[4])))
                            self.tablewidget.setItem(row, 5, QTableWidgetItem(str(record[5])))
                            message="Record is Displayed"
                    else:
                        self.tablewidget.setRowCount(1)
                        self.tablewidget.setItem(row, 0, QTableWidgetItem(str("No Record")))
                        self.tablewidget.setItem(row, 1, QTableWidgetItem(str("No Record")))
                        self.tablewidget.setItem(row, 2, QTableWidgetItem(str("No Record")))
                        self.tablewidget.setItem(row, 3, QTableWidgetItem(str("No Record")))
                        self.tablewidget.setItem(row, 4, QTableWidgetItem(str("No Record")))
                        self.tablewidget.setItem(row, 5, QTableWidgetItem(str("No Record")))

                        message="Record does not exist"
                else:
                    message="Enter a Valid Supplier Id"
            ShowMessageDialog(self,message)
        except BaseException as ex:
            print(ex)
