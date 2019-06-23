from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *


class ViewBrandSubCategory(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.setWindowTitle("BrandSubCategory Details")
        self.setGeometry(50,50,400,540)
        self.layout = QVBoxLayout()

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        column_headers = ("BrandSubCatId", "BrandName", "SubCategoryName")
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.tableWidget.setToolTip("Right click to delete a record")
        self.layout.addWidget(self.tableWidget)
        self.PrepareTableData()
        # TO give options on a right click
        self.tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        deleteAction = QAction("Delete Record", self.tableWidget)

        self.tableWidget.addAction(deleteAction)

        deleteAction.triggered.connect(self.DeleteRecord)

        self.setLayout(self.layout)
        #self.show()

    def PrepareTableData(self):
        con=Connections.Connection()
        query="select * from brandinfo natural join brandsubcategoryinfo "
        brand_records=con.ExecuteQuery(query)

        query = "select * from subcategoryinfo natural join brandsubcategoryinfo "
        subcat_records = con.ExecuteQuery(query)

        row=0

        if brand_records is not None:
            self.tableWidget.setRowCount(len(brand_records))
            for record in brand_records:
                self.tableWidget.setItem(row,0,QTableWidgetItem(str(record[2])))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(record[1]))
                row+=1
        else:
            self.tableWidget.setRowCount(1)
            for record in brand_records:
                self.tableWidget.setItem(row,0,QTableWidgetItem("No Record"))
                self.tableWidget.setItem(row, 1, QTableWidgetItem("No Record"))
                row+=1
        row=0
        if subcat_records is not None:

            for record in subcat_records:
                self.tableWidget.setItem(row, 2, QTableWidgetItem((record[1])))

                row += 1
        else:
            for record in subcat_records:
                self.tableWidget.setItem(row,2,QTableWidgetItem("No Record"))
                row+=1

    def DeleteRecord(self):
        try:
            message = ""
            srow = self.tableWidget.currentRow()
            bid = self.tableWidget.item(srow, 0).text()
            res = ShowConfirmation(self)
            if res == QMessageBox.Yes:
                con=Connections.Connection()

                table_name = "brandsubcategoryinfo"
                primary_value = {"SrNo": bid}
                query = con.CreateDeleteQuery(table_name, primary_value)
                print(query)
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



