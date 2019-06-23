from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from dao import Connections
from utilities import *
import sys


class ImagePlayer(QWidget):
    def __init__(self):
        super().__init__()

        #lbl=QLabel(self)
        #pixmap=QPixmap("inventory-track.gif")
        #lbl.setPixmap(pixmap)
        self.movie = QMovie('inventory-track.gif', QByteArray(),self)
        size = self.movie.scaledSize()
        self.movie_screen = QLabel()
        self.movie_screen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.movie_screen.setMovie(self.movie)
        self.movie.start()

        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.movie_screen.setAlignment(Qt.AlignCenter)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.movie_screen)

        self.setLayout(main_layout)

        self.show()
if __name__=='__main__':
    app = QApplication(sys.argv)
    ex=ImagePlayer()
    sys.exit(app.exec_())