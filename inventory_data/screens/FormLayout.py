from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
from PyQt5.QtCore import *
import sys

conn = sqlite3.connect('hdb.db')
c = conn.cursor()

class add_doctor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 220)
        self.setWindowTitle("Doctor's Details")
        font = QFont()
        font.setPointSize(11)
        self.setFont(font)
        self.font = QFont("Arial")


        layout = QVBoxLayout()
        layout.addWidget(self.create_form())
        # layout.addWidget(btn)
        self.setLayout(layout)
        self.show()

    def create_form(self):
        self.formGroupBox = QGroupBox("Doctor's Information")
        fbox = QFormLayout()

        ######## Labels ##########
        self.lbl3 = QLabel("DOCTOR's INFORMATION ")
        fbox.addRow(self.lbl3)
        self.lbl3.setAlignment(Qt.AlignCenter)

        # self.date = QLineEdit()
        self.date = QDateEdit()
        fbox.addRow(QLabel("Date : "), self.date)

        self.s_id = QLineEdit()
        fbox.addRow(QLabel("Staff Id  : "), self.s_id)

        self.combo_dept = QComboBox(self)
        self.combo_dept.addItems(["Select Department", "General Surgery", "Dermatology & venereology& lerprology",
                             "Drug de-addiction& treatment center", "Gynaecology", "Internal medicine",
                             "Obstetrics(For pregnant women)", "Ophthalmology(eye)", "Oral health centre(Dental)",
                             "Orthopaedics", "Otolaryngology", "Paediatric orthopaedics", "Peadiatric surgery",
                             "Peadiatric medicine", "Plastic surgery", "Psychiatry", "Urology"])
        fbox.addRow(QLabel("Enter the Department: "),self.combo_dept)

        self.lbl = QLabel("Personal Details: ")
        fbox.addRow(self.lbl)
        self.lbl.setAlignment(Qt.AlignCenter)

        self.name = QLineEdit()
        fbox.addRow(QLabel("Doctor's Name : "), self.name)

        self.age = QLineEdit()
        fbox.addRow(QLabel("Doctor's Age : "), self.age)

        self.fname = QLineEdit()
        fbox.addRow(QLabel("Father's Name : "), self.fname)

        self.pno = QLineEdit()
        fbox.addRow(QLabel("Phone Number : "), self.pno)

        self.an = QLineEdit()
        fbox.addRow(QLabel("Aadhar number : "), self.an)

        self.salary = QLineEdit()
        fbox.addRow(QLabel("Salary : "), self.salary)

        self.combo_gen = QComboBox(self)
        self.combo_gen.addItems(["Male", "Female", "Transgender"])
        fbox.addRow(QLabel("Gender: "), self.combo_gen)

        self.lbl2=QLabel("Address Details: ")
        fbox.addRow(self.lbl2)
        self.lbl2.setAlignment(Qt.AlignCenter)

        self.hno = QLineEdit()
        fbox.addRow(QLabel("Hno: "), self.hno)

        self.city = QLineEdit()
        fbox.addRow(QLabel("City : "), self.city)

        self.state = QLineEdit()
        fbox.addRow(QLabel("State : "), self.state)

        self.pc = QLineEdit()
        fbox.addRow(QLabel("Pincode : "), self.pc)
        print(9)
        self.btn1 = QPushButton("SAVE")
        self.btn2 = QPushButton("CANCEL")
        print(10)
        fbox.addRow(self.btn1, self.btn2)
        print(89)
        self.btn1.clicked.connect(self.add_aptmnt)

        self.setLayout(fbox)


    def add_aptmnt(self):
        val0=self.date.text()
        val1 = self.s_id.text()
        print(15)
        val2 = self.combo_dept.currentText()
        print(val1)

        val3 = self.name.text()
        val4 = self.age.text()
        val5 = self.fname.text()
        val6 = self.pno.text()
        val7 = self.an.text()
        val8 = self.salary.text()
        val9 = self.combo_gen.currentText()
        val10 = self.hno.text()
        val11 = self.city.text()
        val12 = self.state.text()
        val13 = self.pc.text()
        print(20)
        sql1 = "INSERT INTO drlist(date,sid,dept,name,age,fname,pno,aadhar,salary,gender,hno,city,state,pincode) values ('{}',{}, '{}','{}',{},'{}',{},{},{},'{}',{},'{}','{}',{})".format(val0,val1, val2, val3, val4,val5,val6,val7, val8, val9,val10,val11,  val12, val13)
        print(100)
        print(sql1)
        print(90)
        c.execute(sql1)
        print(200)

        conn.commit()
        QMessageBox.information(self, 'DOCTOR', "Record inserted successfully...", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = add_doctor()
    ex.show()
    sys.exit(app.exec_())


