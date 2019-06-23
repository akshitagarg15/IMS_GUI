from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
#from screens import AdminMainWindow, UserMainWindow, CashierMainWindow
import sys



class MdiArea(QMdiArea):
    def __init__(self, parent=None):
        QMdiArea.__init__(self, parent=parent)

    def paintEvent(self, event):
        QMdiArea.paintEvent(self, event)
        painter = QPainter(self.viewport())
        painter.drawPixmap(self.rect(), QPixmap("MDI.png"))