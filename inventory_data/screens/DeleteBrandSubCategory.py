from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class DeleteBrandSubCategory(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        grid=QGridLayout()
        grid.setSpacing(10)

        self.setWindowTitle("Delete BrandSubCategory Screen")
        self.brand_records=list()
        self.subcat_records=list()
        self.setGeometry(100,100,300,150)

        #Initilize the Widgets
        lblsubcatname=QLabel("Choose SubCategory")
        lblbid=QLabel("Choose Brand")
        lblbname=QLabel("Brand Name")
        newfont=QFont("Bell MT",18,QFont.Bold)
        lblbid.setFont(newfont)
        lblbname.setFont(newfont)
        lblsubcatname.setFont(newfont)

        self.brandcombo=QComboBox()
        self.bnameEdit=QLineEdit()
        self.subcatcombo=QComboBox()
        self.btndelete=QPushButton("Delete Info")
        #self.btnupdate = QPushButton("Update Info")

        self.brandcombo.setFont(newfont)
        self.bnameEdit.setFont(newfont)
        self.subcatcombo.setFont(newfont)
        self.btndelete.setFont(newfont)
        #self.btnupdate.setFont(newfont)

        #Positoning of widgets
        grid.addWidget(lblbid,1,0)
        grid.addWidget(self.brandcombo,1,1,1,3)
        grid.addWidget(lblbname, 2, 0)
        grid.addWidget(self.bnameEdit, 2, 1, 1, 3)
        grid.addWidget(lblsubcatname, 3, 0)
        grid.addWidget(self.subcatcombo, 3, 1, 1, 3)
        grid.addWidget(self.btndelete, 4, 0,1,4)

        self.brandcombo.addItem("Choose Brand")
        self.subcatcombo.addItem("Choose SubCategory")
        self.PrepareComboItems()
        self.brandcombo.currentTextChanged.connect(self.ChangeCombo)
        self.btndelete.clicked.connect(self.DeleteInfo)
        self.setLayout(grid)

        self.brandcombo.setToolTip("Choose Brand to be deleted")
        self.bnameEdit.setToolTip("Brand name will appear automatically")
        self.subcatcombo.setToolTip("Choose Subcategory of brand")

    def PrepareComboItems(self):
        try:
            con=Connections.Connection()

            column_values=("BrandId","BrandName")
            table1="brandinfo"
            table2="brandsubcategoryinfo"
            query=con.CreateJoinQuery(column_values,table1,table2)
            print(query)
            self.brand_records=con.ExecuteQuery(query)
            print(self.brand_records)



            if self.brand_records is not None:
                for record in self.brand_records:
                    value=record[1]+"("+str(record[0])+")"
                    self.brandcombo.addItem(value)


        except BaseException as ex:
            print(ex)


    def ChangeCombo(self):
        try:
            index=self.brandcombo.currentIndex()
            if index > 0 and (index - 1) <= len(self.brand_records):
                self.subcatcombo.clear()
                self.subcatcombo.addItem("Choose SubCategory")
                con=Connections.Connection()
                record = self.brand_records[index - 1]
                #subrecord=self.subcat_records[index-1]
                self.bnameEdit.setText(record[1])
                bid=record[0]
                #self.subcatEdit.setText(subrecord[1])
                column_values = ("BrandId", "SubCategoryName")
                table1 = "subcategoryinfo"
                table2 = "brandsubcategoryinfo"
                query = con.CreateJoinQuery(column_values, table1, table2)
                query+=" where BrandId="+str(bid)
                print(query)
                self.subcat_records = con.ExecuteQuery(query)
                print(self.subcat_records)
                if self.subcat_records is not None:
                    for record in self.subcat_records:
                        value = record[1] + "(" + str(record[0]) + ")"
                        self.subcatcombo.addItem(value)

            else:
                self.bnameEdit.setText("")
                #self.subcatEdit.setText("")
        except BaseException as ex:
            print(ex)
    def DeleteInfo(self):

        try:
            bid = self.brandcombo.currentIndex()
            sid=self.subcatcombo.currentIndex()
            message = ""
            if bid > 0 and sid>0:
                con = Connections.Connection()
                index = sid
                record = self.subcat_records[index - 1]
                sid = record[0]
                table_name = "brandsubcategoryinfo"
                primary_values = {"SrNo": sid}
                query = con.CreateDeleteQuery(table_name, primary_values)
                print(query)
                res=ShowConfirmation(self)
                if res==QMessageBox.Yes:
                    if con.InsertQuery(query):
                        message = "Deletion happened successfully"
                        self.PrepareComboItems()
                    else:
                        message = "Deletion Failure Due To: " + con.GetErrorMessage()
                else:
                    message="Deletion aborted"
            else:
                message="Select Required Fields"
            ShowMessageDialog(self, message)
        except BaseException as ex:
            print(ex)
