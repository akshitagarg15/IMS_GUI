from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import datetime
import os
import sys

class AddEmployeeInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        try:
            self.setWindowTitle("Employee Details")
            grid=QGridLayout()
            self.setGeometry(100,100,300,350)

            #Initilize the Widgets

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
            self.rbadhaar=QCheckBox("Adhaar Card")
            lblproofid = QLabel("Proof ID")
            lblsalary=QLabel("Salary")
            lbldesignation=QLabel("Designation")
            self.LblJoiningDate = QLabel("Entry Date")

            NewFont=QFont("Bell MT",18,QFont.Bold)
            self.dob=QDateEdit()
            grid.setContentsMargins(0, 0, 0, 0)
            self.dob.setCalendarPopup(True)
            #self.dob.setGridVisible(True)
            self.dob.calendarWidget().installEventFilter(self)

            self.enameEdit = QLineEdit()
            self.fnameEdit = QLineEdit()
            self.contactEdit = QLineEdit()
            self.emailidEdit = QLineEdit()
            self.addressEdit = QLineEdit()
            self.pidEdit = QLineEdit()
            self.salaryEdit = QLineEdit()
            self.designationEdit = QLineEdit()
            self.btn = QPushButton("Add New Employee")

            self.enameEdit.setFont(NewFont)
            self.fnameEdit.setFont(NewFont)
            self.contactEdit.setFont(NewFont)
            self.emailidEdit.setFont(NewFont)
            self.addressEdit.setFont(NewFont)
            self.pidEdit.setFont(NewFont)
            self.salaryEdit.setFont(NewFont)
            self.designationEdit.setFont(NewFont)
            # self.EntryDateEdit.setFont(NewFont)
            self.btn.setFont(NewFont)
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

            self.rbadhaar.setFont(NewFont)
            lblgender.setFont(NewFont)
            lbldob.setFont(NewFont)

            self.lblpic=QLabel(self)
            #pixmap=QPixmap(os.path.realpath("screens/EmpMale.gif"))
            #print(os.path.realpath("screens/pic3.png"))
            #print(pixmap.isNull())
            #self.lblpic.setPixmap(pixmap)
            grid.addWidget(self.lblpic, 4, 5,8,8)

            self.rbmale.toggled.connect(self.male)
            self.rbfemale.toggled.connect(self.female)
            self.rbothers.toggled.connect(self.others)

            grid.addWidget(lblename,1,0,1,1)
            grid.addWidget(self.enameEdit,1,1,1,3)

            grid.addWidget(lblfname, 2, 0, 1, 1)
            grid.addWidget(self.fnameEdit, 2, 1, 1, 3)

            grid.addWidget(lbldob, 3, 0, 1, 1)
            grid.addWidget(self.dob, 3, 1, 1, 3)


            grid.addWidget(lblgender, 4, 0,1,1)
            grid.addWidget(self.rbmale, 4, 1,1,1)
            grid.addWidget(self.rbfemale, 4, 2,1,1)
            grid.addWidget(self.rbothers, 4, 3,1,1)

            grid.addWidget(lblcontact, 5, 0, 1, 1)
            grid.addWidget(self.contactEdit, 5, 1, 1, 3)

            grid.addWidget(lblemailid, 6, 0, 1, 1)
            grid.addWidget(self.emailidEdit, 6, 1, 1, 3)

            grid.addWidget(lbladdress, 7, 0, 1, 1)
            grid.addWidget(self.addressEdit, 7, 1, 1, 3)

            grid.addWidget(lblprooftype, 8, 0)
            grid.addWidget(self.rbadhaar, 8, 1)
            #grid.addWidget(self.rblicence, 8, 2)
           # grid.addWidget(self.rbavoter, 8, 3)
            grid.addWidget(lblproofid, 9, 0, 1, 1)
            grid.addWidget(self.pidEdit, 9, 1, 1, 3)

            grid.addWidget(lblsalary, 10, 0, 1, 1)
            grid.addWidget(self.salaryEdit, 10, 1, 1, 3)
            grid.addWidget(lbldesignation, 11, 0, 1, 1)
            grid.addWidget(self.designationEdit, 11, 1, 1, 3)
            grid.addWidget(self.btn, 12, 0, 1, 3)

            self.btn.clicked.connect(self.AddDetails)

            self.setLayout(grid)
            #self.show()
        except BaseException as ex:
            print(ex)
    def male(self,enabled):
        try:
            print(enabled)
            if enabled:

                #self.lblpic = QLabel(self)
                #pixmap = QPixmap(os.path.realpath("screens/EmpMale.gif"))
                pixmap=QPixmap("EmpMale.gif")

                self.lblpic.setPixmap(pixmap)
                #self.lblpic.move(100,200)
        except BaseException as ex:
            print(ex)
    def female(self, enabled):
        try:
            if enabled:
                #self.lblpic = QLabel(self)
                #pixmap = QPixmap(os.path.realpath("screens/EmpFemale.gif"))
                pixmap =QPixmap ("EmpFemale.gif")
                self.lblpic.setPixmap(pixmap)
                print(os.path.realpath(self.lblpic))
                #self.lblpic.move(100, 200)
        except BaseException as ex:
            print(ex)
    def others(self,enabled):
        try:
            print(enabled)
            if enabled:

                #self.lblpic = QLabel(self)
                #pixmap = QPixmap(os.path.realpath("screens/trans.png"))
                pixmap=QPixmap("trans.png")

                self.lblpic.setPixmap(pixmap)
                #self.lblpic.move(100,200)
        except BaseException as ex:
            print(ex)


    def AddDetails(self):
        allvalid=True
        message=""

        ename=self.enameEdit.text()
        fname=self.fnameEdit.text()

        dob=self.dob.text()
        #print(dob)

        gen=""

        contact=self.contactEdit.text()
        email=self.emailidEdit.text()
        add=self.addressEdit.text()
        ptype=""

        pid=self.pidEdit.text()
        sal=self.salaryEdit.text()
        desig=self.designationEdit.text()

        if self.rbmale.isChecked():
            gen=self.rbmale.text()
        elif self.rbfemale.isChecked():
            gen=self.rbfemale.text()
        elif self.rbothers.isChecked():
            gen=self.rbothers.text()


        if self.rbadhaar.isChecked():
            ptype=self.rbadhaar.text()
        else:
            message+="Select proof type\n\n"


        if IsEmpty(ename):
            message+="Enter Employee Name\n\n"
            allvalid=False
        elif IsNumber(ename):
            message += "Enter Employee Name in alphabets\n\n"
            allvalid = False
        if IsEmpty(fname):
            message+="Enter Employee's Father Name\n\n"
            allvalid=False
        elif IsNumber(fname):
            message += "Enter Valid Employee's Father Name in alphabets\n\n"
            allvalid = False
        if IsEmpty(gen):
            message += "Enter Valid Employee's Gender\n\n"
            allvalid = False



        if IsEmpty(dob):
            message += "Enter Employee's DOB\n\n"
            allvalid = False
        if IsEmpty(email):
            message += "Enter Employee's Email Id\n\n"
            allvalid = False
        if IsEmpty(contact):
            message += "Enter Employee's Contact NO\n\n"
            allvalid = False
        elif not ValidContact(contact):
            message += "Enter Valid Employee's Contact No\n\n"
            allvalid = False

        if IsEmpty(add):
            message += "Enter Employee's Address\n\n"
            allvalid = False
        if IsEmpty(pid):
            message += "Enter Valid Employee's Proof Id\n\n"
            allvalid = False
        elif not ValidAdhaar(pid):
            message += "Enter Valid Employee's Proof Id\n\n"
            allvalid = False

        if IsEmpty(sal):
            message += "Enter Employee's Salary\n\n"
            allvalid = False
        if IsEmpty(desig):
            message += "Enter Employee's Designation\n\n"
            allvalid = False



        try:

            # value=datetime.datetime.now()
            # print(value)
            # print(value.year)
            # print(value.month)
            #
            # print(value.date)

            # date=self.dob.selectedDate()
            # Date=str(value.year)+"-"+str(value.month)+"-"+str(value.date)
            # print(Date)

            date=QDate.currentDate().toPyDate()
            print(date)
            date=str(date)
            # date=date.split('-')
            dob=str(dob)
            dob=dob.split('-')
            DOB=str(dob[2]) +"-"+ str(dob[1]) +"-"+ str(dob[0])
            print(DOB)

        except BaseException as ex:
            print(ex)

        if allvalid==True:
            try:
                con=Connections.Connection()
                print(123)
                table_name="employeeinfo"
                column_values={"EmpName":ename,"FName":fname,"DOB":str(DOB),"Gender":gen,"contact":contact,"EmailId":email,"Address":add,"ProofId":pid,"ProofType":"adhaar","Salary":sal,"Designation":desig,"DateOfJoining":str(date)}
                query=con.CreateInsertQuery(table_name,column_values)
                print(query)
                if con.InsertQuery(query):
                    message="New Employee Details Inserted Successfully"
                else:
                    message="Insertion Failure Due To: "+con.GetErrorMessage()
            except BaseException as ex:
                message+="Insertion Failure"
                print(ex)

        ShowMessageDialog(self,message)


