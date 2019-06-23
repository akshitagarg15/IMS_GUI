if self.rboldcust.isChecked():
    print(self.cust_records)
    custid = self.custidcombo.currentIndex()
    record = self.cust_records[custid - 1]

    customerid = record[0]

    custname = record[1]
    print(customerid)
    print(custname)
if self.rbnewcust.isChecked():
    con = Connections.Connection()
    query = "select last_insert_id()"
    cid = con.ExecuteQuery(query)
    cname = self.custnameEdit.text()
    print(cid)
    print(cname)




                custname=self.custnameEdit.text()
                contact=self.contactEdit.text()
                email=self.emailEdit.text()
                add=self.addEdit.text()
                allvalid=True

                if IsEmpty(custname):
                    message+="enter new customer name\n\n"
                    allvalid=False
                elif IsNumber(custname):
                    message += "enter valid customer name\n\n"
                    allvalid = False
                if IsEmpty(contact):
                    message+="enter new customer contact\n\n"
                    allvalid=False
                elif ValidContact(contact):
                    message += "enter valid customer contactNo\n\n"
                    allvalid = False
                if IsEmpty(add):
                    message+="enter new customer address\n\n"
                    allvalid=False
                if allvalid==True:
                    con = Connections.Connection()
                    table_name="customerinfo"
                    column_values={"CustomerName":custname,"contact":contact,""}
