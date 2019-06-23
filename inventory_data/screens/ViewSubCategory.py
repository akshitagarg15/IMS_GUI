from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class ViewSubCategory(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.setWindowTitle("SubCategory Details")

        self.layout = QVBoxLayout()
        self.setGeometry(100, 100, 500, 500)
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(3)
        column_headers = ("SubCategoryID", "SubCategoryName","CategoryId")
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.tableWidget.setStyleSheet("background-color:#CCDADA;")
        self.layout.addWidget(self.tableWidget)
        self.tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.PrepareTableData()
        deleteAction = QAction("Delete Record", self.tableWidget)
        editAction = QAction("Edit Record", self.tableWidget)
        self.tableWidget.addAction(deleteAction)
        self.tableWidget.addAction(editAction)
        deleteAction.triggered.connect(self.DeleteRecord)
        editAction.triggered.connect(self.EditRecord)
        self.setLayout(self.layout)

        #self.show()


    def PrepareTableData(self):
        Con = Connections.Connection()
        query = "select SubCategoryId,SubCategoryName,CategoryID from subcategoryinfo"
        records = Con.ExecuteQuery(query)
        row = 0
        if records is not None:
            self.tableWidget.setRowCount(len(records))
            for record in records:
                self.tableWidget.setItem(row,0,QTableWidgetItem(str(record[0])))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(record[1]))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(record[2])))
                row+=1
        else:
            self.tableWidget.setRowCount(1)
            for record in records:
                self.tableWidget.setItem(row,0,QTableWidgetItem("No Record"))
                self.tableWidget.setItem(row, 1, QTableWidgetItem("No Record"))
                self.tableWidget.setItem(row, 2, QTableWidgetItem("No Record"))
                row+=1

    def EditRecord(self):
        message = ""
        srow = self.tableWidget.currentRow()
        print(srow)
        scol = self.tableWidget.currentColumn()
        print(scol)
        sid = self.tableWidget.item(srow, 0).text()
        sname = self.tableWidget.item(srow, scol).text()

        con = Connections.Connection()
        query = "update subcategoryinfo set SubCategoryName='" + sname + "'"
        query += "where SubCategoryId=" + str(sid)
        print(query)
        if con.InsertQuery(query):
            message = " Updated Record Successfully"
        else:
            message = "Updation Error Due To: " + con.GetErrorMessage()
        ShowMessageDialog(self, message)

    def DeleteRecord(self):
        try:
            message = ""
            srow = self.tableWidget.currentRow()
            sid = self.tableWidget.item(srow, 0).text()
            res = ShowConfirmation(self)
            if res == QMessageBox.Yes:
                if IsAlreadyPresent(sid):

                    message = "SubCategory Present in items"
                else:
                    con = Connections.Connection()

                    table_name = "subcategoryinfo"
                    primary_value = {"SubCategoryId": sid}
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
        query = "select * from iteminfo where SubCategoryId=" + sid

        record = con.ExecuteQuery(query)

        if len(record) > 0:
            return True

        else:
            return False
    except BaseException as ex:
        print(ex)

