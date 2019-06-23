from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import datetime

class ViewSupplier(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        try:

            self.layout=QVBoxLayout()
            self.setWindowTitle("View Supplier Details")
            self.setGeometry(30, 50, 1500, 1550)
            newfont=QFont("Bell MT",18,QFont.Bold)
            self.tablewidget=QTableWidget()
            self.tablewidget.setColumnCount(6)
            column_headers=("Supplier Id","Supplier Name","GSTno","Contact","Email Id","Address")
            self.tablewidget.setHorizontalHeaderLabels(column_headers)
            self.tablewidget.setStyleSheet("background-color:#CCDADA;")
            self.tablewidget.setToolTip("Right click to delete/edit record")
            self.layout.addWidget(self.tablewidget)
            self.tablewidget.setContextMenuPolicy(Qt.ActionsContextMenu)
            deleteAction = QAction("Delete Record", self.tablewidget)
            editAction = QAction("Edit Record", self.tablewidget)
            self.tablewidget.addAction(deleteAction)
            self.tablewidget.addAction(editAction)
            self.setLayout(self.layout)
            deleteAction.triggered.connect(self.DeleteRecord)
            editAction.triggered.connect(self.EditRecord)

            self.PrepareTableData()
        except BaseException as ex:
            print(ex)
        #self.show()

    def PrepareTableData(self):
        con=Connections.Connection()
        table_name="supplierinfo"
        column_values=("SupplierId","SupplierName","GSTno","contact","EmailId","Address")
        query=con.CreateSelectQuery(column_values,table_name)
        #print(query)
        self.sup_records=con.ExecuteQuery(query)

        row=0
        if self.sup_records is not None:
            self.tablewidget.setRowCount(len(self.sup_records))
            for record in self.sup_records:
                self.tablewidget.setItem(row,0,QTableWidgetItem(str(record[0])))
                self.tablewidget.setItem(row, 1, QTableWidgetItem(record[1]))
                self.tablewidget.setItem(row, 2, QTableWidgetItem(str(record[2])))
                self.tablewidget.setItem(row, 3, QTableWidgetItem(record[3]))
                self.tablewidget.setItem(row, 4, QTableWidgetItem(record[4]))
                self.tablewidget.setItem(row, 5, QTableWidgetItem(str(record[5])))
                row+=1

        else:
            self.tablewidget.setRowCount(len(self.sup_records))
            for record in self.cust_records:
                self.tablewidget.setItem(row, 0, QTableWidgetItem("No Record"))
                self.tablewidget.setItem(row, 1, QTableWidgetItem("No Record"))
                self.tablewidget.setItem(row, 2, QTableWidgetItem("No Record"))
                self.tablewidget.setItem(row, 3, QTableWidgetItem("No Record"))
                self.tablewidget.setItem(row, 4, QTableWidgetItem("No Record"))
                self.tablewidget.setItem(row, 4, QTableWidgetItem("No Record"))
                row += 1

    def EditRecord(self):
        try:
            message = ""
            srow = self.tablewidget.currentRow()

            scol = self.tablewidget.currentColumn()

            supid = self.tablewidget.item(srow, 0).text()
            supname = self.tablewidget.item(srow, scol).text()

            con = Connections.Connection()
            query = "update supplierinfo set SupplierName='" + supname + "'"
            query += "where SupplierId=" + str(supid)

            if con.InsertQuery(query):
                message = " Updated Record Successfully"
            else:
                message = "Updation Error Due To: " + con.GetErrorMessage()
            ShowMessageDialog(self, message)
        except BaseException as ex:
            print(ex)
    def DeleteRecord(self):
        try:
            message = ""
            srow = self.tablewidget.currentRow()
            sid = self.tablewidget.item(srow, 0).text()
            res = ShowConfirmation(self)
            if res == QMessageBox.Yes:
                if IsAlreadyPresent(sid):

                    message = "Supplier  Present in Supplier-Brands"
                else:
                    con = Connections.Connection()

                    table_name = "supplierinfo"
                    primary_value = {"SupplierId": sid}
                    query = con.CreateDeleteQuery(table_name, primary_value)
                    if con.InsertQuery(query):
                        self.PrepareTableData()
                        message = "Deletion Happened Successfully"
                    else:
                        message = "Deletion failure Due To: " + con.GetErrorMessage()
            else:
                message = "Deletion Aborted"
            ShowMessageDialog(self, message)
        except BaseException as ex:
            print(ex)

def IsAlreadyPresent(sid):
    try:

        result = False
        con = Connections.Connection()
        query = "select * from supplierbrandinfo where SupplierId=" + sid

        record = con.ExecuteQuery(query)

        if len(record) > 0:
            return True

        else:
            return False
    except BaseException as ex:
        print(ex)
