from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def ShowMessageDialog(self,message):
    QMessageBox.question(self,'Message from controller',message,QMessageBox.Ok)
def ShowConfirmation(self):
    return QMessageBox.question(self,"Message From Controller","Are You Sure?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)

def IsEmpty(Value):
    return len(Value)==0

def IsNumber(Value):
    try:
        val=int(Value)
        return True
    except:
        return False


def IsFloat(Value):
    try:
        val=float(Value)
        return True
    except:
        return False

def IsAlphabet(Value):
    try:
        val=str(Value)
        return True
    except:
        return False

def ValidContact(Value):
    if len(Value)==10:
        for ch in Value:
            if not IsNumber(ch):
                return False
        return  True

def ValidGST(Value):
    if len(Value)==15:
        if Value.isalnum():
            return True
        else:
            return False
    else:
        return False

def ValidAdhaar(Value):
    if len(Value)==12:
        if IsNumber(Value):
            return True
        else:
            return False
    else:
        return False

def ValidLicence(Value):
    valid=False
    if len(Value) == 13:

        for ch in Value:
            if not IsNumber(ch[0]) and not IsNumber(ch[1]):
                valid=True
            else:
                return False
    else:
        return False

    if valid==True:
        num=2
        for ch in Value:
            if IsNumber(ch[num]):
                num+=1
            else:
                return False
    return True


