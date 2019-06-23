import sys, time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from screens import  AdminMainWindow

class MySplashScreen(QSplashScreen):

    def __init__(self,movie,parent = None):
        movie.jumpToFrame(0)
        pixmap = QPixmap(movie.frameRect().size())
        QSplashScreen.__init__(self, pixmap)
        self.movie = movie
        self.movie.frameChanged.connect(self.repaint)

    def showEvent(self, event):
        self.movie.start()

    def hideEvent(self,event):
        self.movie.stop()

    def paintEvent(self,event):
        painter = QPainter(self)
        pixmap = self.movie.currentPixmap()
        self.setMask(pixmap.mask())
        painter.drawPixmap(0,0,pixmap)

    def sizeHint(self):
        return self.movie.scaledSize()

app = QApplication(sys.argv)
movie = QMovie("Splash.gif")
splash = MySplashScreen(movie)
splash.show()

start = time.time()

while movie.state() == QMovie.Running and time.time() < start + 12:
    app.processEvents()

window = AdminMainWindow.AdminMainWindow()
window.show()
splash.finish(window)

sys.exit(app.exec_())


