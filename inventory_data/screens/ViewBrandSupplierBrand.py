from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class ViewBrandSupplierBrand(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.setWindowTitle("View Suppliers Supplying A Brand")
        self.setGeometry(300, 100, 500, 400)
        grid = QGridLayout()
        grid.setSpacing(10)
        lblbname=QLabel("Enter Brand Name")
        self.bnameEdit=QLineEdit()
        self.btn=QPushButton("View")
        self.tablewidget=QTableWidget()
        newfont = QFont("Bell MT", 18, QFont.Bold)
        lblbname.setFont(newfont)
        self.bnameEdit.setFont(newfont)
        self.btn.setFont(newfont)

        grid.addWidget(lblbname,1,0,1,2)
        grid.addWidget(self.bnameEdit, 2, 0, 1, 2)
        grid.addWidget(self.btn,3,0,1,2)
        grid.addWidget(self.tablewidget, 4, 0)
        self.btn.clicked.connect(self.ViewDetails)
        self.setLayout(grid)
        #self.show()

    def ViewDetails(self):
        try:
            message=""
            bname=self.bnameEdit.text()
            if IsEmpty(bname):
                message="Enter Brand Name"
            elif IsNumber(bname):
                message="Enter Name In Alphabets"

            else:
                if bname is not None:

                    column_headers = ("SupplierName","BrandName" )
                    self.tablewidget.setColumnCount(2)
                    self.tablewidget.setHorizontalHeaderLabels(column_headers)
                    con = Connections.Connection()

                    query = "select * from supplierinfo where SupplierName='"+bname+"'"
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
                    message="Enter a Valid Supplier Name"
            ShowMessageDialog(self,message)
        except BaseException as ex:
            print(ex)
