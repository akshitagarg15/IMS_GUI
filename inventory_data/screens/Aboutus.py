from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *

class Aboutus():
    def __init__(self):
        #super().__init__()
        #font2 = QFont("Segoe UI", 15)

        #message.setFont(font2)
        #lbl = QLabel(self)
        #pixmap = QPixmap("gmail.png")
        #lbl.setPixmap(pixmap)
        #lbl.move(50, 240)
        #self.setGeometry(100,200,300,300)
        #self.lbltitle = QLabel("IMS")

        #message+=str(lbl)+" akshitagarg15@gmail.com"
        #self.setWindowTitle("About Us")
        #self.setStyleSheet("background-color:green")
        #self.lbltitle.move(100,50)
        #self.lblversion=QLabel("",self)
        #self.lblversion.move(50,150)
        #font1=QFont("Segoe UI",18,QFont.Bold)
        #self.lbltitle.setStyleSheet("text-align:center;color:white;")
        #self.lbltitle.setFont(font1)

        #self.lblversion.setFont(font2)
        #self.lblversion.setStyleSheet("text-align:left;color:white;")

        #self.lbldevelop=QLabel("",self)
        #self.lbldevelop.move(50,200)
        #self.lbldevelop.setFont(font2)
        #self.lbldevelop.setStyleSheet("text-align:left;color:white;")


        #lbl.setStyleSheet("text-align:center")
        #lbl.setStyleSheet("height:20%;width:30%")
        #lblmail=QLabel("",self)
        #lblmail.move(60,300)
        ShowMessageDialog(self,message)
