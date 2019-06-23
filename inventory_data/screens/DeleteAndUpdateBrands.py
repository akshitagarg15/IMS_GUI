from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class DeleteAndUpdateBrands(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.records=()
        self.setWindowTitle("Delete and Update Brand Details")
        #self.setGeometry(100,100,300,150)

        #Initilize the Widgets
        lblbrandId=QLabel("Choose Brand")
        lblbname=QLabel("Brand Name")
        NewFont=QFont("Bell MT",18,QFont.Bold)

        self.bnameEdit=QLineEdit()
        self.btn1=QPushButton("Delete Brand")
        self.btn2 = QPushButton("Update Brand")

        self.btn1.clicked.connect(self.DeleteBrand)
        self.btn2.clicked.connect(self.UpdateBrand)
        self.brandIdCombo=QComboBox()
        self.brandIdCombo.setFont(NewFont)
        self.bnameEdit.setFont(NewFont)
        lblbname.setFont(NewFont)
        lblbrandId.setFont(NewFont)
        self.btn1.setFont(NewFont)
        self.btn2.setFont(NewFont)

        self.brandIdCombo.addItem("Choose Brand")

        #Prepare the layout
        grid=QGridLayout()
        grid.setSpacing(10)

        #Grid.addWidget(LblBrandId,1,0)
        grid.addWidget(lblbrandId, 1, 0)
        grid.addWidget(self.brandIdCombo, 1, 1,1,2)
        grid.addWidget(lblbname, 2, 0)
        grid.addWidget(self.bnameEdit, 2, 1,1,2)
        grid.addWidget(self.btn1, 3, 1, 1, 1)
        grid.addWidget(self.btn2, 3, 2, 1, 1)
        self.PrepareComboItems()
        self.brandIdCombo.currentTextChanged.connect (self.ChangeCombo)
        self.brandIdCombo.setToolTip("Choose BrandId")
        self.bnameEdit.setToolTip("To update brandname edit it")
        self.btn1.setToolTip("To delete brand")
        self.btn2.setToolTip("To update brandname")
        self.setLayout(grid)

        #self.show()

    def PrepareComboItems(self):
        con=Connections.Connection()
        query=" select BrandId,BrandName from brandinfo"
        self.records=con.ExecuteQuery(query)
        if len(self.records)>0:
            for record in self.records:
                value=record[1]+"("+str(record[0])+")"
                self.brandIdCombo.addItem(value)



    def ChangeCombo(self, value):
        index=self.brandIdCombo.currentIndex()

        if index>0 and (index-1)<= len(self.records):
            record=self.records[index-1]
            self.bnameEdit.setText(record[1])
        else:
            self.bnameEdit.setText("")



    def DeleteBrand(self):
        try:
            bid=self.brandIdCombo.currentIndex()
            message=""
            if bid>0:
                con=Connections.Connection()
                index=bid
                record=self.records[index-1]
                brandId=record[0]
                table_name="brandinfo"
                primary_values={"BrandId":brandId}
                query=con.CreateDeleteQuery(table_name,primary_values)
                print(query)
                if con.InsertQuery(query):
                    message="Deletion happened successfully"
                    self.PrepareComboItems()
                else:
                    message="Deletion Failure Due To: "+con.GetErrorMessage()
            ShowMessageDialog(self,message)
        except BaseException as ex:
            print(ex)


    def UpdateBrand(self):
       try:
           bid=self.brandIdCombo.currentIndex()

           message=""
           bname=self.bnameEdit.text()
           if bid >  0:

               index=bid

               record=self.records[index-1]

               brandId=record[0]

               con = Connections.Connection()
               table_name = "brandinfo"
               column_value = {"BrandName": bname}
               primary_value = {"BrandId": brandId}

               query = con.CreateUpdateQuery(table_name, column_value, primary_value)

               if con.InsertQuery(query):
                   message="Updation Happened In Database"
                   self.PrepareComboItems()
               else:
                   print("Insertion Failure due to: " + con.GetErrorMessage())
           ShowMessageDialog(self, message)
       except BaseException as ex:
           print(ex)

