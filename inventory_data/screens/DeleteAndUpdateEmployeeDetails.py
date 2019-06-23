from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import datetime

class DeleteAndUpdateEmployeeDetails(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        grid=QGridLayout()
        self.setWindowTitle("Delete/Update Employee Details")
        self.emp_records=list()
        newfont=QFont("Bell MT",18,QFont.Bold)

        lbleid = QLabel("Employee Id")
        self.eidcombo = QComboBox()
        lblename = QLabel("Employee Name")
        lblfname = QLabel("Father Name")
        lbldob=QLabel("Date of Birth")
        lblgender=QLabel("Gender")
        lblcontact = QLabel("Contact")
        lblemail = QLabel("Email Id")
        lbladd = QLabel("Address")
        lblprooftype=QLabel("Proof Type")
        lblproofid=QLabel("Proof ID")
        lblsalary=QLabel("Salary")
        lbldesig=QLabel("Designation")
        lblgen=QLabel("Gender")
        # lblentry = QLabel("Entry Date")

        self.enameEdit = QLineEdit()
        self.fnameEdit = QLineEdit()
        self.contactEdit = QLineEdit()
        self.emailEdit = QLineEdit()
        self.addEdit = QLineEdit()
        self.salaryEdit=QLineEdit()
        self.desigEdit=QLineEdit()
        self.dobEdit=QDateEdit()
        self.rbmale = QRadioButton("Male")
        self.rbfemale = QRadioButton("FeMale")
        self.rbothers = QRadioButton("Others")
        self.pidEdit=QLineEdit()
        self.desigEdit=QLineEdit()
        # self.entryedit = QLabel()
        self.btndelete = QPushButton("Delete Record")
        self.btnupdate = QPushButton("Update Record")
        self.rbadhaar=QCheckBox("adhaar")

        lbleid.setFont(newfont)
        self.eidcombo.setFont(newfont)
        lblename.setFont(newfont)
        lblfname.setFont(newfont)
        lbldob.setFont(newfont)
        lblsalary.setFont(newfont)
        lbldesig.setFont(newfont)
        lblproofid.setFont(newfont)
        lblprooftype.setFont(newfont)
        lblgen.setFont(newfont)
        lblcontact.setFont(newfont)
        lbladd.setFont(newfont)
        # lblentry.setFont(newfont)
        lblemail.setFont(newfont)
        self.enameEdit.setFont(newfont)
        self.fnameEdit.setFont(newfont)
        self.emailEdit.setFont(newfont)
        self.addEdit.setFont(newfont)
        self.contactEdit.setFont(newfont)
        self.salaryEdit.setFont(newfont)
        self.desigEdit.setFont(newfont)
        self.pidEdit.setFont(newfont)
        self.dobEdit.setFont(newfont)
        self.rbothers.setFont(newfont)
        self.rbfemale.setFont(newfont)
        self.rbmale.setFont(newfont)
        # self.entryedit.setFont(newfont)
        self.btndelete.setFont(newfont)
        self.btnupdate.setFont(newfont)
        self.rbadhaar.setFont(newfont)

        grid.addWidget(lblename, 1, 0, 1, 1)
        grid.addWidget(self.enameEdit, 1, 1, 1, 2)

        grid.addWidget(lblfname, 2, 0, 1, 1)
        grid.addWidget(self.fnameEdit, 2, 1, 1, 2)

        grid.addWidget(lbldob, 3, 0, 1, 1)
        grid.addWidget(self.dobEdit, 3, 1, 1, 2)

        grid.addWidget(lblgender, 4, 0, 1, 1)
        grid.addWidget(self.rbmale, 4, 1, 1, 1)
        grid.addWidget(self.rbfemale, 4, 2, 1, 1)
        grid.addWidget(self.rbothers, 4, 3, 1, 1)

        grid.addWidget(lblcontact, 5, 0, 1, 1)
        grid.addWidget(self.contactEdit, 5, 1, 1, 2)

        grid.addWidget(lblemail, 6, 0, 1, 1)
        grid.addWidget(self.emailEdit, 6, 1, 1, 2)

        grid.addWidget(lbladd, 7, 0, 1, 1)
        grid.addWidget(self.addEdit, 7, 1, 1, 2)

        grid.addWidget(lblprooftype, 8, 0)
        grid.addWidget(self.rbadhaar, 8, 1)
        # grid.addWidget(self.rblicence, 8, 2)
        # grid.addWidget(self.rbavoter, 8, 3)
        grid.addWidget(lblproofid, 9, 0, 1, 1)
        grid.addWidget(self.pidEdit, 9, 1, 1, 2)

        grid.addWidget(lblsalary, 10, 0, 1, 1)
        grid.addWidget(self.salaryEdit, 10, 1, 1, 2)
        grid.addWidget(lbldesig, 11, 0, 1, 1)
        grid.addWidget(self.desigEdit, 11, 1, 1, 2)
        grid.addWidget(self.btndelete, 12, 0, 1, 2)
        grid.addWidget(self.btnupdate, 12, 3, 1, 2)

        self.setLayout(grid)
        self.show
