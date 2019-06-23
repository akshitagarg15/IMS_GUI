from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class DeleteAndUpdateSubCategory(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.setWindowTitle("Delete And Update SubCategory Details")
        self.subcat_records=list()
        self.category_records=list()

        lblsubcategoryId = QLabel("Choose SubCategory ID")
        lblsubcatname = QLabel("SubCategory Name")
        lblcatidname = QLabel("Choose Category")
        newfont = QFont("Bell MT", 18, QFont.Bold)
        self.subcategorycombo = QComboBox()
        self.subcategoryEdit= QLineEdit()
        self.categorycombo = QComboBox()
        self.btn1 = QPushButton("Delete Category")
        self.btn2 = QPushButton("Update Category")
        self.subcategorycombo.setFont(newfont)
        self.subcategoryEdit.setFont(newfont)
        self.categorycombo.setFont(newfont)
        lblsubcategoryId.setFont(newfont)
        lblsubcatname.setFont(newfont)
        lblcatidname.setFont(newfont)
        self.btn1.setFont(newfont)
        self.btn2.setFont(newfont)
        self.subcategorycombo.setToolTip("choose a subcategory to perform operation")
        self.subcategoryEdit.setToolTip("Rewrite subcategory for update")
        self.categorycombo.setToolTip("Select the category to be updated")
        self.btn1.setToolTip("To delete subcategory permanently")
        self.btn2.setToolTip("To update subcategory")
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(lblsubcategoryId, 1, 0)
        grid.addWidget(self.subcategorycombo, 1, 1, 1, 3)
        grid.addWidget(lblsubcatname, 2, 0)
        grid.addWidget(self.subcategoryEdit, 2, 1, 1, 3)
        grid.addWidget(lblcatidname, 3, 0)
        grid.addWidget(self.categorycombo, 3, 1, 1, 3)
        grid.addWidget(self.btn1, 4, 1, 1, 1)
        grid.addWidget(self.btn2, 4, 2, 1, 1)
        self.subcategorycombo.addItem("Choose A SubCategory")
        self.categorycombo.addItem("Choose A Category")
        self.PrepareComboItems()
        self.subcategorycombo.currentTextChanged.connect(self.ChangeCombo)
        self.btn1.clicked.connect(self.DeleteSubCategory)
        self.btn2.clicked.connect(self.UpdateSubCategory)

        self.setLayout(grid)
        #self.show()

    def PrepareComboItems(self):
        con=Connections.Connection()
        query="select SubCategoryId,SubCategoryName from subcategoryinfo"
        self.subcat_records=con.ExecuteQuery(query)
        if len(self.subcat_records) >0:
            for record in self.subcat_records:
                value=record[1]+"("+str(record[0])+")"
                self.subcategorycombo.addItem(value)

        query = "select CategoryId,CategoryName from categoryinfo"
        self.category_records = con.ExecuteQuery(query)
        if len(self.category_records) > 0:
            for record in self.category_records:
                value = record[1] + "(" + str(record[0]) + ")"
                self.categorycombo.addItem(value)

    def ChangeCombo(self):
        index=self.subcategorycombo.currentIndex()
        if index > 0 and (index - 1) <= len(self.subcat_records):
            record = self.subcat_records[index - 1]
            self.subcategoryEdit.setText(record[1])
        else:
            self.subcategoryEdit.setText("")

    def DeleteSubCategory(self):
        subid=self.subcategorycombo.currentIndex()
        message=""
        if subid>0:
            con=Connections.Connection()
            record=self.subcat_records[subid-1]
            subcatid=record[0]
            table_name="subcategoryinfo"
            column_values={"SubCategoryId":subcatid}
            query=con.CreateDeleteQuery(table_name,column_values)
            print(query)
            if con.InsertQuery(query):
                message="Deletion Happened Successfully in Database"
            elif "foreign key constraint " in con.GetErrorMessage():
                message="Data is required cannot delete it"
            else:
                message="Deletion Failure Due To: "+con.GetErrorMessage()
        ShowMessageDialog(self,message)

    def UpdateSubCategory(self):
        subname=self.subcategoryEdit.text()
        message=""
        AllValid=True
        if IsEmpty(subname) or "Choose" in self.subcategorycombo.currentText() or "Choose" in self.categorycombo.currentText():
            message+="Fill the required feilds\n\n"
            AllValid=False
        if IsNumber(subname):
            message+="Enter a valid subcategory name\n\n"
            AllValid=False

        if AllValid==True:
            sid=self.subcategorycombo.currentIndex()
            cid=self.categorycombo.currentIndex()
            subname=self.subcategoryEdit.text()
            if cid>0 and sid>0:
                record=self.subcat_records[sid-1]
                subcatid=record[0]
                catrecord=self.category_records[cid-1]
                catid=catrecord[0]

                con=Connections.Connection()
                table_name="subcategoryinfo"
                column_values={"SubCategoryName":subname,"CategoryId":catid}
                primary_values={"SubCategoryID":subcatid}
                query=con.CreateUpdateQuery(table_name,column_values,primary_values)

                if con.InsertQuery(query):
                    message="Updation happened successfully in database"
                else:
                    message="Udation Failure due to: "+con.GetErrorMessage()

            ShowMessageDialog(self,message)
