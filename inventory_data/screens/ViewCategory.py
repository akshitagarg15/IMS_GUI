from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *


class ViewCategory(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.setWindowTitle("Brands")

        self.layout=QVBoxLayout()
        self.setGeometry(100,100,500,500)
        self.tableWidget=QTableWidget()
        self.tableWidget.setColumnCount(2)
        column_headers = ("CategoryID", "CategoryName")
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.layout.addWidget(self.tableWidget)
        self.tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        deleteAction = QAction("Delete Record", self.tableWidget)
        editAction = QAction("Edit Record", self.tableWidget)
        self.tableWidget.addAction(deleteAction)
        self.tableWidget.addAction(editAction)
        deleteAction.triggered.connect(self.DeleteRecord)
        editAction.triggered.connect(self.EditRecord)
        self.PrepareTableData()
        self.tableWidget.setStyleSheet("background-color:#CCDADA;")
        self.tableWidget.setToolTip("Right click to update/delete category name")
        self.setLayout(self.layout)
        #self.show()

    def PrepareTableData(self):
        Con=Connections.Connection()
        query="select CategoryId,CategoryName from categoryinfo"
        records=Con.ExecuteQuery(query)
        row=0

        if records is not None:
            self.tableWidget.setRowCount(len(records))
            for record in records:
                self.tableWidget.setItem(row,0,QTableWidgetItem(str(record[0])))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(record[1]))
                row+=1
        else:
            self.tableWidget.setRowCount(1)
            for record in records:
                self.tableWidget.setItem(row,0,QTableWidgetItem("No Record"))
                self.tableWidget.setItem(row, 1, QTableWidgetItem("No Record"))
                row+=1

    def DeleteRecord(self):
        try:
            message = ""
            srow = self.tableWidget.currentRow()
            cid = self.tableWidget.item(srow, 0).text()
            res = ShowConfirmation(self)
            if res == QMessageBox.Yes:
                if IsAlreadyPresent(cid):

                    message = "SubCategory Present of this Category"
                else:
                    con = Connections.Connection()

                    table_name = "categoryinfo"
                    primary_value = {"CategoryId": cid}
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

    def EditRecord(self):
        message = ""
        srow = self.tableWidget.currentRow()
        print(srow)
        scol = self.tableWidget.currentColumn()
        print(scol)
        cid = self.tableWidget.item(srow, 0).text()
        cname = self.tableWidget.item(srow, scol).text()

        con = Connections.Connection()
        query = "update categoryinfo set CategoryName='" + cname + "'"
        query += "where CategoryId=" + str(cid)
        print(query)
        if con.InsertQuery(query):
            message = " Updated Record Successfully"
        else:
            message = "Updation Error Due To: " + con.GetErrorMessage()
        ShowMessageDialog(self, message)

def IsAlreadyPresent(catid):
    try:

        result = False
        con = Connections.Connection()
        query = "select * from subcategoryinfo where CategoryId=" + catid

        record = con.ExecuteQuery(query)

        if len(record) > 0:
            return True

        else:
            return False
    except BaseException as ex:
        print(ex)

