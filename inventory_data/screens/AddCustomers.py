from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import datetime

class AddCustomers(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.setWindowTitle("Customer Details")
        #self.setGeometry(100,100,300,150)

        #Initilize the Widgets
        LblCustomerId=QLabel("Customer ID")
        LblCustomerName=QLabel("Customer Name")
        LblContact = QLabel("Contact No")
        LblEmailId = QLabel("Email ID")
        LblAddress = QLabel("Address")
        #self.LblEntryDate = QLabel("Entry Date")

        NewFont=QFont("Bell MT",18,QFont.Bold)

        self.CustomerNameEdit=QLineEdit()
        self.ContactEdit = QLineEdit()
        self.EmailIdEdit = QLineEdit()
        self.AddressEdit = QLineEdit()




        self.btn=QPushButton("Add Customer")
        self.btn.clicked.connect(self.AddCustomer)
        self.CustomerNameEdit.setFont(NewFont)
        self.ContactEdit.setFont(NewFont)
        self.EmailIdEdit.setFont(NewFont)
        self.AddressEdit.setFont(NewFont)
        #self.EntryDateEdit.setFont(NewFont)
        self.btn.setFont(NewFont)
        LblCustomerId.setFont(NewFont)
        LblCustomerName.setFont(NewFont)
        LblAddress.setFont(NewFont)
        LblContact.setFont(NewFont)
        LblEmailId.setFont(NewFont)



        #Prepare the layout
        Grid=QGridLayout()
        Grid.setSpacing(10)



        Grid.addWidget(LblCustomerName, 2, 0)
        Grid.addWidget(self.CustomerNameEdit, 2, 1,1,2)

        Grid.addWidget(LblContact, 3,0)
        Grid.addWidget(self.ContactEdit, 3, 1,1,2)

        Grid.addWidget(LblEmailId, 4,0)
        Grid.addWidget(self.EmailIdEdit, 4,1,1,2)

        Grid.addWidget(LblAddress, 5, 0)
        Grid.addWidget(self.AddressEdit,5 ,1, 1,2)

        Grid.addWidget(self.btn, 7, 1, 1, 3)


        self.setLayout(Grid)
        #self.show()

    def AddCustomer(self):
        CustName=self.CustomerNameEdit.text()
        Contact=self.ContactEdit.text()
        EmailId=self.EmailIdEdit.text()
        Address=self.AddressEdit.text()

        Date = datetime.datetime.now()
        EntryDate=Date.date()
        print(EntryDate)
        message=""
        AllValid=True
        if IsEmpty(CustName) :
            message+=" Please Fill Customer Name\n\n"
            AllValid=False
        if IsEmpty(Contact) :
            message+=" Please Fill Customer Contact\n\n"
            AllValid=False
        elif not ValidContact(Contact):
            message+="Please Enter a Valid Contact Number\n\n"
            AllValid=False
        if IsEmpty(Address):
            message+="Please Enter Customer Address\n\n"
            AllValid=False
        if AllValid:
            table_name="customerinfo"
            column_values=dict()
            column_values["CustomerName"]= CustName
            column_values["contact"] = Contact
            column_values["EmailId"] = EmailId
            column_values["Address"] = Address
            column_values["EntryDate"] = str(EntryDate)

            con=Connections.Connection()

            query=con.CreateInsertQuery(table_name,column_values)
            print(query)
            if con.InsertQuery(query):
                message="Customer information saved in database"
            else:
                message="Insertion Failure Due To:"+ con.GetErrorMessage()
        ShowMessageDialog(self,message)

