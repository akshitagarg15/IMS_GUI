from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from screens import Custcashier, BillScreen
from utilities import *
import sys
import pymysql
import os
import shutil


class AddEmpPhoto(QWidget):
    def __init__(self):
        super().__init__()
        self.PrepareScreen()

    def PrepareScreen(self):
        self.setWindowTitle("Add Employee Photo")

        self.emp_records=list()
        self.image_path=""
        newfont = QFont("Bell MT", 18, QFont.Bold)
        lblemp=QLabel("Choose Employee")
        lblphoto = QLabel("Choose Photo")
        self.lblpic=QLabel()
        self.comboemp=QComboBox()

        self.comboemp.addItem("Choose Employee")
        self.btnpic=QPushButton("Browse Photo")
        self.btnadd=QPushButton("Add Photo")

        lblphoto.setFont(newfont)
        lblemp.setFont(newfont)
        self.comboemp.setFont(newfont)
        self.btnpic.setFont(newfont)
        self.btnadd.setFont(newfont)

        grid=QGridLayout()
        grid.addWidget(lblemp,1,0)
        grid.addWidget(self.comboemp,1,1,1,3)

        grid.addWidget(lblphoto,2,0)
        grid.addWidget(self.btnpic,2,1,1,3)

        grid.addWidget(self.lblpic,3,0,3,4)
        grid.addWidget(self.btnadd,6,0,1,4)
        self.setLayout(grid)
        #self.show()
        self.btnadd.clicked.connect(self.AddPhoto)
        self.btnpic.clicked.connect(self.BrowsePhoto)
        self.PrepareComboData()

    def BrowsePhoto(self):
        options=QFileDialog.Options()
        options |=QFileDialog.DontUseNativeDialog
        files,_=QFileDialog.getOpenFileNames(self,"Choose any file","","All Files(*)",options=options)
        if files:
            path=files[0]
            filename , extension=os.path.splitext(path)
            extensions=".png,.jpg,.gif,.jpeg"
            if extension.lower() not in extensions:
                ShowMessageDialog(self,"Please Choose a valid image")
            else:
                pixmap=QPixmap(path)
                self.lblpic.setPixmap(pixmap.scaledToWidth(100))
                self.image_path=path


    def PrepareComboData(self):
        con=Connections.Connection()
        query="select EmpId, EmpName from employeeinfo"
        self.emp_records=con.ExecuteQuery(query)
        if len(self.emp_records)>0:
            for record in self.emp_records:
                value =record[1]+"("+str(record[0])+")"
                self.comboemp.addItem(value)

    def AddPhoto(self):
        employeeid=0
        message=""
        if "Choose" not in self.comboemp.currentText():
            index=self.comboemp.currentIndex()
            record= self.emp_records[index-1]
            employeeid=record[0]
            allvalid=True

        if IsEmpty(self.image_path):
            message+= "Choose a valid image\n\n"
            allvalid=False

        if employeeid==0:
            message="Please choose a employee id\n\n"
            allvalid=False
        if allvalid:
            photoname, extension =os.path.splitext(self.image_path)
            table_name="empphotos"
            column_values=dict()
            column_values["EmpId"]=employeeid
            column_values["Extension"]=extension
            con=Connections.Connection()
            query=con.CreateInsertQuery(table_name,column_values)
            if con.InsertQuery(query):
                query="select last_insert_id()"
                result=con.ExecuteQuery(query)
                if len(result)>0:
                    try:
                        photoid =result[0][0]  # we want to save img on the name of photoid
                        destination="../Emp_Photos/" +str(photoid)+ extension
                        shutil.copy(self.image_path,destination)
                    except BaseException as ex:
                        print(ex)
                self.image_path=""
                message="Employee photo is added successfully"
            else:
                    message= "Insertion Failure due to: "+ con.GetErrorMessage()
        ShowMessageDialog(self,message)


# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     ex=AddEmpPhoto()
#     sys.exit(app.exec_())
