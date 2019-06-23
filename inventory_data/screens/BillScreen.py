from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import datetime
from screens import LoginScreen
import sys

class BillScreen(QWidget):
    def __init__(self,uname=None):
        super().__init__()
        self.username = uname
        print(self.username)

        self.PrepareScreen()

    def PrepareScreen(self):
        self.ptotal = 0
        self.itemnum = 0
        self.ProductList=list()
        self.brand_records=list()
        self.cat_records = list()
        self.subcat_records = list()
        self.item_records = list()
        self.cust_records=list()
        grid=QGridLayout()
        self.setGeometry(50,50,1500,1000)
        self.setWindowTitle("Bill Screen")
        newfont = QFont("Bell MT", 18, QFont.Bold)
        self.rboldcust=QRadioButton("Old Customer")
        self.rbnewcust = QRadioButton("New Customer")

        lblcust=QLabel("New Customer Details")
        lblcustname=QLabel("Customer Name")
        lblcontact=QLabel("Contact No.")
        lblemail=QLabel("Email Id")
        lbladd=QLabel("Address")
        lblbid=QLabel("Choose BrandID")
        lblcid = QLabel("Choose CatID")
        lblid = QLabel("Choose ItemID")
        lblcustid=QLabel("Choose CustomerID")
        lblsubid=QLabel("Choose SubCat ID")
        lblitemno=QLabel("Items")
        lbltotal=QLabel("Pay")
        lbloldcontact=QLabel("Contact")
        lblpaid=QLabel("Amount Paid")


        lblcust.setFont(newfont)
        lblcustname.setFont(newfont)
        lblcontact.setFont(newfont)
        lbloldcontact.setFont(newfont)
        lblemail.setFont(newfont)
        lbladd.setFont(newfont)
        lblcid.setFont(newfont)
        lblbid.setFont(newfont)
        lblid.setFont(newfont)
        lblpaid.setFont(newfont)
        lblcustid.setFont(newfont)
        lblsubid.setFont(newfont)
        lblitemno.setFont(newfont)
        lbltotal.setFont(newfont)
        self.rboldcust.setFont(newfont)
        self.rbnewcust.setFont(newfont)

        lblamount=QLabel("Amount")
        self.amount=QLineEdit()
        self.paidEdit=QLineEdit()
        self.itemno=QLabel()
        self.total=QLabel()
        self.oldcontactEdit=QLineEdit()
        self.total.setStyleSheet("color:red")
        self.itemno.setStyleSheet("color:BLUE")
        lblamount.setFont(newfont)
        self.amount.setFont(newfont)

        self.custnameEdit=QLineEdit()
        self.contactEdit=QLineEdit()
        self.paidEdit.setFont(newfont)
        self.emailEdit=QLineEdit()
        self.addEdit=QLineEdit()
        self.custidcombo=QComboBox()
        self.brandidcombo=QComboBox()
        self.catidcombo=QComboBox()
        self.subcatidcombo=QComboBox()
        self.itemidcombo=QComboBox()
        self.tableWidget=QTableWidget()

        lblqty = QLabel("Qty")
        self.qtyEdit = QLineEdit()
        self.qtyEdit.setToolTip("enter qty")
        self.btn = QPushButton("ADD Product")
        self.btngenerate=QPushButton("Generate Bill")
        lblqty.setFont(newfont)
        self.qtyEdit.setFont(newfont)
        self.addEdit.setFont(newfont)
        self.paidEdit.setFont(newfont)
        self.custnameEdit.setFont(newfont)
        self.contactEdit.setFont(newfont)
        self.emailEdit.setFont(newfont)
        self.custidcombo.setFont(newfont)
        self.brandidcombo.setFont(newfont)
        self.catidcombo.setFont(newfont)
        self.itemidcombo.setFont(newfont)
        self.subcatidcombo.setFont(newfont)
        self.btn.setFont(newfont)
        self.btngenerate.setFont(newfont)
        self.total.setFont(newfont)
        self.itemno.setFont(newfont)
        self.oldcontactEdit.setFont(newfont)

        #For making all the widgets inactive initially
        self.custnameEdit.setEnabled(False)
        self.contactEdit.setEnabled(False)
        self.emailEdit.setEnabled(False)
        self.addEdit.setEnabled(False)
        self.custidcombo.setEnabled(False)


        #Positioning of widgets
        grid.addWidget(self.rboldcust,1,0,1,2)
        grid.addWidget(self.rbnewcust, 1,4,1,2)

        grid.addWidget(lblcustid,2,0,1,2)
        grid.addWidget(self.custidcombo,2,2,1,2)

        grid.addWidget(lbloldcontact, 3, 0, 1, 2)
        grid.addWidget(self.oldcontactEdit, 3, 2, 1, 2)

        grid.addWidget(lblcust,2,4,1,2)
        grid.addWidget(lblcustname,3,4,1,2)

        grid.addWidget(self.custnameEdit,3,6,1,2)
        grid.addWidget(lblcontact,4,4,1,2)
        grid.addWidget(self.contactEdit,4,6,1,2)
        grid.addWidget(lblemail,5,4,1,1)
        grid.addWidget(self.emailEdit,5,6,1,2)


        grid.addWidget(lbladd,6,4,1,1)
        grid.addWidget(self.addEdit,6,6,1,2)
        grid.addWidget(lblbid,7,0,1,2)
        grid.addWidget(self.brandidcombo,7,2,1,2)
        grid.addWidget(lblsubid, 7, 4, 1, 2)
        grid.addWidget(self.subcatidcombo, 7, 6, 1, 2)
        grid.addWidget(lblcid, 8, 0,1,2)
        grid.addWidget(self.catidcombo, 8, 2,1,2)

        grid.addWidget(lblid, 8,4,1,2 )
        grid.addWidget(self.itemidcombo, 8, 6,1,2)
        grid.addWidget(lblpaid, 8, 8, 1, 1)
        grid.addWidget(self.paidEdit, 8, 9, 1, 2)
        grid.addWidget(lblqty,9,0,1,2)
        grid.addWidget(self.qtyEdit,9,2,1,2)
        grid.addWidget(lblitemno, 9, 4, 1, 1)
        grid.addWidget(self.itemno, 9, 5, 1, 1)
        grid.addWidget(lbltotal, 9, 6, 1, 1)
        grid.addWidget(self.total, 9, 7, 1, 1)
        grid.addWidget(self.btn, 9, 8, 1, 1)
        grid.addWidget(self.btngenerate, 9, 9, 1, 2)

        grid.addWidget(self.tableWidget,10,0,1,15)
        self.custidcombo.addItem("Choose CustomerID")
        self.brandidcombo.addItem("BrandID")
        self.catidcombo.addItem("CategoryID")
        self.ComboFunc()
        # To make one of of the radiobutton actions active at a time
        self.rboldcust.toggled.connect(self.OldCustomer)
        self.rbnewcust.toggled.connect(self.NewCustomer)
        self.btn.clicked.connect(self.AddProduct)
        self.tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        deleteAction = QAction("Delete Record", self.tableWidget)

        self.tableWidget.addAction(deleteAction)



        deleteAction.triggered.connect(self.DeleteRecord)

        self.btngenerate.clicked.connect(self.GenerateBill)

        self.setLayout(grid)

        #self.show()
    def OldCustomer(self,enabled):
        try:
            self.custidcombo.setEnabled(enabled)
            self.PrepareCustcombo()
            self.custidcombo.currentTextChanged.connect(self.ChangeCombo)
            self.catidcombo.currentIndexChanged.connect(self.CatChange)
            self.subcatidcombo.currentIndexChanged.connect(self.SubCatChange)
        except BaseException as ex:
            print(ex)

    def ChangeCombo(self):
        try:
            index = self.custidcombo.currentIndex()
            if index > 0 and (index - 1) <= len(self.cust_records):

                record = self.cust_records[index - 1]

                self.oldcontactEdit.setText(record[2])
            else:
                self.oldcontactEdit.setText("")
        except BaseException as ex:
            print(ex)

    def NewCustomer(self, enabled):
        try:

            self.custnameEdit.setEnabled(enabled)
            self.contactEdit.setEnabled(enabled)
            self.emailEdit.setEnabled(enabled)
            self.addEdit.setEnabled(enabled)

            self.catidcombo.currentIndexChanged.connect(self.CatChange)
            self.subcatidcombo.currentIndexChanged.connect(self.SubCatChange)


        except BaseException as ex:
            print(ex)




    def CatChange(self, index):
        try:

            self.subcatidcombo.clear()

            self.subcatidcombo.addItem("SubCatID")

            value=self.cat_records[index-1]


            con = Connections.Connection()

            query = "select SubcategoryId,SubCategoryName from subcategoryinfo where CategoryId="+str(value[0])

            self.subcat_records = con.ExecuteQuery(query)

            for record in self.subcat_records:
                value = record[1] + "(" + str(record[0]) + ")"
                self.subcatidcombo.addItem(value)
        except BaseException as ex:
            print(ex)


    def SubCatChange(self, index):
        try:
            self.itemidcombo.clear()
            self.itemidcombo.addItem("ItemID")
            value=self.subcat_records[index-1]
            subcat=value[0]

            con = Connections.Connection()

            query = "select ItemId,ItemName,Price,AvailableQty from iteminfo where SubCategoryId=" + str(value[0])

            self.item_records = con.ExecuteQuery(query)

            for record in self.item_records:
                value = record[1] + "(" + str(record[0]) + ")"
                self.itemidcombo.addItem(value)
        except BaseException as ex:
            print(ex)

    def PrepareCombo(self):
        con=Connections.Connection()
        table_name="brandinfo"
        column_values=("BrandId","BrandName")
        query=con.CreateSelectQuery(column_values,table_name)
        #print(query)
        self.brand_records=con.ExecuteQuery(query)

        for record in  self.brand_records:
            value=record[1]+"("+str(record[0])+")"
            self.brandidcombo.addItem(value)


        table_name = "categoryinfo"
        column_values = ("CategoryId", "CategoryName")
        query = con.CreateSelectQuery(column_values, table_name)
        #print(query)
        self.cat_records = con.ExecuteQuery(query)
        #print(self.cat_records)
        for record in self.cat_records:
            value = record[1] + "(" + str(record[0]) + ")"
            self.catidcombo.addItem(value)

    def PrepareCustcombo(self):
        con=Connections.Connection()
        table_name="customerinfo"
        column_values=("CustomerId","CustomerName,contact")
        query=con.CreateSelectQuery(column_values,table_name)
        self.cust_records=con.ExecuteQuery(query)
        if self.cust_records is not None:
            for record in self.cust_records:
                value=str(record[1])+" ("+ str(record[0])+")"
                self.custidcombo.addItem(value)

    def AddProduct(self):
        try:
            message=""

            bid=self.brandidcombo.currentIndex()

            record=self.brand_records[bid-1]
            brand=record[1]



            cid = self.catidcombo.currentIndex()
            record = self.cat_records[cid - 1]
            category = record[1]

            subcatid = self.subcatidcombo.currentIndex()
            record = self.subcat_records[subcatid - 1]
            subcat = record[1]

            itemid = self.itemidcombo.currentIndex()

            record = self.item_records[itemid - 1]
            itemId=record[0]
            item = record[1]

            price = int(record[2])
            qty = self.qtyEdit.text()
            qt = 0

            if self.ProductList is not None:
                for record in self.ProductList:
                    if record[7] == itemId:
                        qt += int(record[4])


            Qty=int(qty)  + qt

            if itemId is not None:
                con=Connections.Connection()
                query="select AvailableQty from iteminfo where itemid = "+str(itemId)

                self.itemqty=con.ExecuteQuery(query)

                if self.itemqty[0][0]>= Qty:
                    self.diff=self.itemqty[0][0]-Qty

                    if IsEmpty(brand):
                        message+="Select Brand\n\n"

                    if IsEmpty(category):
                        message+="Select Category\n\n"

                    if IsEmpty(subcat):
                        message+="Select SubCategory\n\n"

                    if IsEmpty(item):
                        message+="Select Item\n\n"
                    if IsEmpty(qty):
                        message += "Enter Quantity\n\n"
                    elif not IsFloat(qty) or not IsNumber(qty):
                        message += "Enter Quantity In digits\n\n"

                    subtotal=price*int(qty)

                    #It will send all the values of a particular item to product List
                    self.value=(item,brand,category,subcat,qty,price,subtotal,itemId)

                    self.ProductList.append(self.value)
                    self.ptotal+=int(subtotal)
                    self.itemnum+=int(qty)


                    self.itemno.setText(str(self.itemnum))
                    self.total.setText(str(self.ptotal))


                    self.PrepareTable()
                    message="Item Added"

                else:
                    self.diff=Qty-self.itemqty[0][0]
                    message="Demand is Out of Range\n\nShortage= "+ str(self.diff)
            else:
                message="Select Item"
            ShowMessageDialog(self,message)
        except BaseException as ex:
            print(ex)
    def PrepareTable(self):
        column_values=("ItemName","BrandName","CategoryName","SubcategoryName","Qty","Price","Sub-Total")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(column_values)
        row=0
        if len(self.ProductList)>0:
            self.tableWidget.setRowCount(len(self.ProductList))
            for record in self.ProductList:
                self.tableWidget.setItem(row,0,QTableWidgetItem(record[0]))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(record[1]))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(record[2]))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(record[3]))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(str(record[4])))
                self.tableWidget.setItem(row, 5, QTableWidgetItem(str(record[5])))
                self.tableWidget.setItem(row, 6, QTableWidgetItem(str(record[6])))

                row+=1


    def ComboFunc(self):
        self.PrepareCombo()


    def DeleteRecord(self):
        try:
            message = ""
            srow = self.tableWidget.currentRow()
            bid = self.tableWidget.item(srow, 0).text()
            qty = self.tableWidget.item(srow, 4).text()
            price = self.tableWidget.item(srow, 5).text()
            del(self.ProductList[srow])
            self.tableWidget.removeRow(self.tableWidget.currentRow())
            self.itemnum-=int(qty)
            self.ptotal-=float(price)
            self.itemno.setText(str(self.itemnum))
            self.total.setText(str(self.ptotal))
        except BaseException as ex:
            print(ex)

    def GenerateBill(self):
        #print("cash")
        try:


            if self.rboldcust.isChecked():
                message=" "
                con=Connections.Connection()
                custid=self.custidcombo.currentIndex()
                cust_record=self.cust_records[custid-1]
                customerid=cust_record[0]
                Date = datetime.datetime.now()
                EntryDate = Date.date()
                pay="cash"

                table_bname='billinfo'
                column_bvalues={"CustomerId":str(custid),"BillDate":str(EntryDate),"UserName":str(self.username),"PaymentDescription":str(pay)}
                query=con.CreateInsertQuery(table_bname,column_bvalues)
                print(query)
                if con.InsertQuery(query):
                    query='select last_insert_id()'
                    billid=con.ExecuteQuery(query)

                    for products in self.ProductList:
                        table_billdetail = "billdetails"
                        column_bdetailvalues = {"BillId": str(billid[0][0]), "ItemId":str(products[7]),"Qty":str(products[4]),"Price":str(products[5])}
                        query=con.CreateInsertQuery(table_billdetail,column_bdetailvalues)
                        if con.InsertQuery(query):
                            query="update iteminfo set AvailableQty="+ str(self.diff)
                            query+=" where ItemId= "+str(products[7])


                            if con.InsertQuery(query):
                                message = "Bill genertaed successfully"
                            ShowMessageDialog(self,message)

                            self.Dialog()

                else:
                    message="Failure Due To: "+ con.GetErrorMessage()


            elif self.rbnewcust.isChecked():
                try:
                    message=""
                    allvalid=True
                    cname=self.custnameEdit.text()
                    contact=self.contactEdit.text()
                    email=self.emailEdit.text()
                    add=self.addEdit.text()
                    if IsEmpty(cname) or IsEmpty(contact) or IsEmpty(add):
                        message="Enter all fields(name,contact,address)\n\n"
                        allvalid=False
                    if IsEmpty(self.paidEdit):
                        message="Enter amount to be paid"
                        allvalid=False
                    if not IsAlphabet(cname):
                        message+="Enter valid Name\n\n"
                        allvalid=False
                    if not ValidContact(contact):
                        message+="Enter a valid contact\n\n"
                        allvalid=False

                    if len(self.ProductList)<=0:
                        message+="Select the items to be purchased\n\n"
                        allvalid=False

                    if allvalid==True:
                        con=Connections.Connection()
                        table_name="customerinfo"
                        column_values={"CustomerName":cname,"contact":str(contact),"EmailId":str(email),"Address":add}
                        query=con.CreateInsertQuery(table_name,column_values)

                        if con.InsertQuery(query):

                            query='select last_insert_id()'
                            self.custId=con.ExecuteQuery(query)
                            uname=self.username
                            pay="cash"
                            Date = datetime.datetime.now()
                            EntryDate = Date.date()
                            table_bname = 'billinfo'
                            column_bvalues = {"CustomerId": str(self.custId[0][0]), "BillDate": str(EntryDate), "UserName": uname,
                                              "PaymentDescription": pay}
                            query = con.CreateInsertQuery(table_bname, column_bvalues)
                            if con.InsertQuery(query):
                                query = 'select last_insert_id()'
                                billid = con.ExecuteQuery(query)
                                print(billid)
                                print(self.ProductList)

                                for products in self.ProductList:
                                    table_billdetail = "billdetails"
                                    column_bdetailvalues = {"BillId": str(billid[0][0]), "ItemId": str(products[7]),
                                                            "Qty": str(products[4]), "Price": str(products[5])}
                                    query = con.CreateInsertQuery(table_billdetail, column_bdetailvalues)
                                    print(query)
                                    if con.InsertQuery(query):
                                        query = "update iteminfo set AvailableQty=" + str(self.diff)
                                        query += "where ItemId= " + str(products[7])
                                        con.InsertQuery(query)
                                    message="Bill generated successfully"
                            else:
                                message = "Failure Due To: " + con.GetErrorMessage()
                        else:
                            message="Failure due to: "+ con.GetErrorMessage()


                except BaseException as ex:
                    print(ex)
                ShowMessageDialog(self,message)

                self.Dialog()


        except BaseException as ex:
            print(ex)

    def Dialog(self):
        try:



            #self.setStyleSheet("Font-Family:Bell MT;Font-Size:25px;Font-weight: Bold")
            paid = self.paidEdit.text()
            amt = self.ptotal
            bal = float(paid) - amt

            balance = "Balance : " + str(bal)

            ShowMessageDialog(self,balance)

        except BaseException as ex:
            print(ex)