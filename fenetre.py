

from PyQt6.QtWidgets import QWidget, QApplication,QPushButton,QLineEdit,QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize,Qt
import sys

class Fenetre(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Accueil")
        self.setFixedSize(800,600)

        self.btn = QPushButton(self)
        self.btn.setGeometry(100,100,150,150)
        self.btn.setIcon(QIcon("image/2013_rainbow_6_patriots-1920x1080.jpg"))
        self.btn.setIconSize(QSize(150,150))
        self.btn.setStyleSheet("border:2px solid black;border-radius:15px;")
        self.btn.setCursor(Qt.CursorShape.PointingHandCursor)

        self.btn_cliquer = QPushButton(self,text="cliquer ici")
        self.btn_cliquer.setGeometry(250,100,150,50)
        self.btn_cliquer.setIcon(QIcon("image/2013_rainbow_6_patriots-1920x1080.jpg"))
        self.btn_cliquer.setIconSize(QSize(50,30))
        self.btn_cliquer.setStyleSheet("border:2px solid black;border-radius:15px;color:red;font-size:20px;")
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    test=  Fenetre()
    test.show()
    sys.exit(app.exec())