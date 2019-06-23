from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *


class ViewSupplierBrandInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.setWindowTitle("SupplierBrand Details")
        self.layout = QVBoxLayout()

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(2)
        column_headers=("Supplier Name","Brand Name")
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.layout.addWidget(self.tableWidget)
        self.tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        deleteAction = QAction("Delete Record", self.tableWidget)
        self.tableWidget.setStyleSheet("background-color:#CCDADA;")
        self.tableWidget.addAction(deleteAction)
        self.tableWidget.setToolTip("right click to delete record")
        self.setLayout(self.layout)
        self.PrepareTableData()

        #self.show()

    def PrepareTableData(self):
        con=Connections.Connection()
        column_value=("BrandId","BrandName")
        table_name1="brandinfo"
        table_name2 = "supplierbrandinfo"
        query=con.CreateJoinQuery(column_value,table_name1,table_name2)
        print(query)
        brand_record=con.ExecuteQuery(query)

        column_value = ("SupplierId", "SupplierName")
        table_name1 = "supplierinfo"
        table_name2 = "supplierbrandinfo"
        query = con.CreateJoinQuery(column_value, table_name1, table_name2)
        print(query)
        supplier_record = con.ExecuteQuery(query)

        row = 0
        if supplier_record is not None:
            self.tableWidget.setRowCount(len(supplier_record))
            for record in supplier_record:
                self.tableWidget.setItem(row, 0, QTableWidgetItem(record[1]))
                row += 1
        else:
            self.tableWidget.setRowCount(1)
            for record in supplier_record:
                self.tableWidget.setItem(row, 0, QTableWidgetItem("No Record"))

                row += 1

        row = 0

        if brand_record is not None:
            self.tableWidget.setRowCount(len(brand_record))
            for record in brand_record:
                self.tableWidget.setItem(row, 1, QTableWidgetItem(record[1]))
                row += 1
        else:
            self.tableWidget.setRowCount(1)
            for record in brand_record:
                self.tableWidget.setItem(row, 1, QTableWidgetItem("No Record"))
                row +=1


    def DeleteRecord(self):
        try:
            message = ""
            srow = self.tableWidget.currentRow()
            bid = self.tableWidget.item(srow, 0).text()
            res = ShowConfirmation(self)
            if res == QMessageBox.Yes:

                con = Connections.Connection()

                table_name = "supplierbrandinfo"
                primary_value = {"BrandId": bid}
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




