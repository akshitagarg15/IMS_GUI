from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import datetime
import os
import sys

class ViewEmployeeInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        try:
            self.setWindowTitle("View Employee Details")
            grid=QGridLayout()
            #self.setGeometry(100,100,300,350)
            self.total=0
            self.records=list()
            self.currentindex=0
            self.photo_records=[]
            #Initilize the Widgets
            lbleid=QLabel("Employee Id:")
            self.eid=QLabel()

            lblename=QLabel("Employee Name")
            lblfname = QLabel("Father Name")
            lbldob=QLabel("Date Of Birth")
            lblgender=QLabel("Gender")
            self.rbmale=QRadioButton("Male")
            self.rbfemale = QRadioButton("FeMale")
            self.rbothers = QRadioButton("Others")
            lblcontact = QLabel("Contact No")
            lblemailid = QLabel("Email ID")
            lbladdress = QLabel("Address")
            lblprooftype=QLabel("Proof Type")
            self.ptypeEdit=QLineEdit()
            lblproofid = QLabel("Proof ID")
            lblsalary=QLabel("Salary")
            lbldesignation=QLabel("Designation")
            self.LblJoiningDate = QLabel("Entry Date")

            NewFont=QFont("Bell MT",18,QFont.Bold)
            self.eid.setFont(NewFont)
            lbleid.setFont(NewFont)
            self.dob=QLineEdit()
            grid.setContentsMargins(0, 0, 0, 0)


            self.enameEdit = QLineEdit()
            self.fnameEdit = QLineEdit()
            self.contactEdit = QLineEdit()
            self.emailidEdit = QLineEdit()
            self.addressEdit = QLineEdit()
            self.pidEdit = QLineEdit()
            self.salaryEdit = QLineEdit()
            self.designationEdit = QLineEdit()
            self.btnnext = QPushButton("Next Record")
            self.btnprev = QPushButton("Prev Record")
            self.btnupdate=QPushButton("Update")
            self.btndel=QPushButton('Delete')

            self.enameEdit.setFont(NewFont)
            self.fnameEdit.setFont(NewFont)
            self.contactEdit.setFont(NewFont)
            self.emailidEdit.setFont(NewFont)
            self.addressEdit.setFont(NewFont)
            self.pidEdit.setFont(NewFont)
            self.ptypeEdit.setFont(NewFont)
            self.salaryEdit.setFont(NewFont)
            self.designationEdit.setFont(NewFont)
            # self.EntryDateEdit.setFont(NewFont)
            self.btnnext.setFont(NewFont)
            self.btnprev.setFont(NewFont)
            self.btnupdate.setFont(NewFont)
            self.btndel.setFont(NewFont)
            lblename.setFont(NewFont)
            lblfname.setFont(NewFont)
            self.rbmale.setFont(NewFont)
            self.rbfemale.setFont(NewFont)
            self.rbothers.setFont(NewFont)
            self.dob.setFont(NewFont)
            lbladdress.setFont(NewFont)
            lblcontact.setFont(NewFont)
            lblemailid.setFont(NewFont)
            lblprooftype.setFont(NewFont)
            lblproofid.setFont(NewFont)
            lblsalary.setFont(NewFont)
            lbldesignation.setFont(NewFont)


            lblgender.setFont(NewFont)
            lbldob.setFont(NewFont)

            self.lblpic=QLabel(self)
            #pixmap=QPixmap(os.path.realpath("screens/EmpMale.gif"))
            #print(os.path.realpath("screens/pic3.png"))
            #print(pixmap.isNull())
            #self.lblpic.setPixmap(pixmap)
            grid.addWidget(self.lblpic, 3, 5,8,8)



            grid.addWidget(lbleid, 1, 0, 1, 1)
            grid.addWidget(self.eid, 1, 1, 1, 3)

            grid.addWidget(lblename,2,0,1,1)
            grid.addWidget(self.enameEdit,2,1,1,3)

            grid.addWidget(lblfname, 3, 0, 1, 1)
            grid.addWidget(self.fnameEdit, 3,1, 1, 3)

            grid.addWidget(lbldob, 4, 0, 1, 1)
            grid.addWidget(self.dob, 4, 1, 1, 3)


            grid.addWidget(lblgender, 5, 0,1,1)
            grid.addWidget(self.rbmale, 5, 1,1,1)
            grid.addWidget(self.rbfemale, 5, 2,1,1)
            grid.addWidget(self.rbothers, 5, 3,1,1)

            grid.addWidget(lblcontact, 6, 0, 1, 1)
            grid.addWidget(self.contactEdit, 6, 1, 1, 3)

            grid.addWidget(lblemailid, 7, 0, 1, 1)
            grid.addWidget(self.emailidEdit, 7, 1, 1, 3)

            grid.addWidget(lbladdress, 8, 0, 1, 1)
            grid.addWidget(self.addressEdit, 8, 1, 1, 3)

            grid.addWidget(lblprooftype, 9, 0,1,1)
            grid.addWidget(self.ptypeEdit, 9, 1,1,3)

            grid.addWidget(lblproofid, 10, 0, 1, 1)
            grid.addWidget(self.pidEdit, 10, 1, 1, 3)

            grid.addWidget(lblsalary, 11, 0, 1, 1)
            grid.addWidget(self.salaryEdit, 11, 1, 1, 3)
            grid.addWidget(lbldesignation, 12, 0, 1, 1)
            grid.addWidget(self.designationEdit, 12, 1, 1, 3)
            grid.addWidget(self.btnprev, 13, 1, 1, 1)
            grid.addWidget(self.btnupdate, 13, 2, 1, 1)
            #grid.addWidget(self.btndel, 13, 2, 1, 1)*
            grid.addWidget(self.btnnext, 13, 3, 1, 1)


            self.btnnext.clicked.connect(self.NextRecord)
            self.btnprev.clicked.connect(self.PrevRecord)

            self.CountRecords()
            self.ShowDetails()

            self.setLayout(grid)
            self.show()
        except BaseException as ex:
            print(ex)


    def NextRecord(self):
        if self.total>0 and self.currentindex+1 < self.total:
            self.currentindex+=1
            self.ShowDetails()
        else:
            ShowMessageDialog(self,"There is no next Record")

    def PrevRecord(self):
        if self.currentindex>0 and self.total>0:
            self.currentindex-=1
            self.ShowDetails()
        else:
            ShowMessageDialog(self,"There is no details")

    def ShowDetails(self):
        if self.total > 0 and self. currentindex < self.total:
            con=Connections.Connection()
            record=self.records[self.currentindex]
            query = "select PhotoId,extension from empphotos where EmpId = " + str(record[0])
            print(query)
            self.photo_records = con.ExecuteQuery(query)
            print(self.photo_records)
            if len(self.photo_records)>0:
                image_path="../Emp_Photos/"+ str(self.photo_records[0][0])+ self.photo_records[0][1]
            else:
                image_path = "../Emp_Photos/nopic.png"
            pixmap=QPixmap(image_path)
            self.lblpic.setPixmap(pixmap.scaledToWidth(400))
            self.eid.setText(str(record[0]))
            self.enameEdit.setText(record[1])
            self.fnameEdit.setText(record[2])
            self.dob.setText(str(record[3]))
            gender=record[4]
            if gender=="Male":
                self.rbmale.setChecked(True)
            if gender=="Female":
                self.rbfemale.setChecked(True)
            if gender=="Others":
                self.rbothers.setChecked(True)
            self.contactEdit.setText(str(record[5]))
            self.emailidEdit.setText(str(record[6]))
            self.addressEdit.setText(str(record[7]))
            self.pidEdit.setText(str(record[8]))
            self.ptypeEdit.setText("Adhaar Card")
            self.salaryEdit.setText(str(record[10]))
            self.designationEdit.setText(str(record[11]))

    def CountRecords(self):
        con=Connections.Connection()
        query="select EmpId,EmpName,FName,DOB,Gender,contact,EmailId,Address,ProofId,ProofType,Salary,Designation,DateOfJoining from employeeinfo"
        self.records=con.ExecuteQuery(query)
        self.total=len(self.records )



if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=ViewEmployeeInfo()
    sys.exit(app.exec_())



