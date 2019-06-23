from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class AddUser(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.setWindowTitle("Add New User")
        #self.setGeometry(100,100,300,150)

        #Initilize the Widgets
        LblUname=QLabel("Enter User Name")
        LblPass=QLabel("Enter Password")
        LblRole = QLabel("Enter Role Name")
        NewFont=QFont("Bell MT",18,QFont.Bold)

        self.UnameEdit=QLineEdit()

        self.PassEdit = QLineEdit()
        # to hide password
        self.PassEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.RbAdmin=QRadioButton("Admin")
        self.RbUser = QRadioButton("User")
        self.RbCashier = QRadioButton("Cashier")
        self.btn=QPushButton("Add New User")
        self.btn.clicked.connect(self.AddNewUser)
        LblUname.setFont(NewFont)
        LblPass.setFont(NewFont)
        LblRole.setFont(NewFont)
        self.RbCashier.setFont(NewFont)
        self.UnameEdit.setFont(NewFont)
        self.PassEdit.setFont(NewFont)
        self.RbAdmin.setFont(NewFont)
        self.RbUser.setFont(NewFont)

        self.btn.setFont(NewFont )

        #Prepare the layout
        Grid=QGridLayout()
        Grid.setSpacing(10)

        #Grid.addWidget(LblCategoryId,1,0)

        Grid.addWidget(LblUname, 1, 0)
        Grid.addWidget(self.UnameEdit, 1, 1,1,3)

        Grid.addWidget(LblPass, 2, 0)
        Grid.addWidget(self.PassEdit, 2, 1, 1, 3)

        Grid.addWidget(LblRole, 3, 0)
        Grid.addWidget(self.RbAdmin, 3, 1)
        Grid.addWidget(self.RbUser, 3, 2)
        Grid.addWidget(self.RbCashier, 3, 3)
        Grid.addWidget(self.btn, 4, 0, 1, 4)

        self.setLayout(Grid)


        self.show()


    def AddNewUser(self):

        UName= self.UnameEdit.text()

        UPass = self.PassEdit.text()

        RoleName=""
        message=""
        if self.RbAdmin.isChecked():
            RoleName=self.RbAdmin.text()
        elif self.RbUser.isChecked():
            RoleName=self.RbUser.text()
        elif self.RbCashier.isChecked():
            RoleName=self.RbCashier.text()




        if IsEmpty(UName) or IsEmpty(UPass) or IsEmpty(RoleName):
            message="Please Fill All The Boxes"
        else:
            table_name =" logins "
            column_values = {"username":UName,"password":UPass,"rolename":RoleName}
            con = Connections.Connection()
            print(1)
            query = con.CreateInsertQuery(table_name,column_values)
            if con.InsertQuery(query):
                message="New User Is Added"
            else:
                message="Insertion Failure Due To: "+ con.GetErrorMessage()
        ShowMessageDialog(self,message)
