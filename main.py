
# ananganana fenetre principale
from PyQt6.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QPushButton
import sys
from PyQt6.QtGui import QIcon,QCursor
from PyQt6.QtCore import Qt

class fenetre(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1000,500)
        # self.setFixedHeight(300)
        # self.setFixedWidth(500)
        self.setFixedSize(1000,500)
        self.setWindowTitle("python APP")
        self.setWindowIcon(QIcon("Qt_lmm/image/2013_rainbow_6_patriots-1920x1080.jpg"))

        style_text = "color:black; background-color:red;font-size: 30px;border-radius: 10px;padding-left: 20px;"
        self.titre = (QLabel(self,text="Application Bureau"))
        self.titre.setGeometry(350,20,300,70)
        self.titre.setStyleSheet(style_text)
        self.search = QLabel(self,text="recherche :")
        self.search.setGeometry(150,90,200,50)
        self.search.setStyleSheet("""
            QLabel{
                                  color:back;
                                  font-size:20px;
                                  }
        """)


        self.input_search = QLineEdit(self)
        self.input_search.setGeometry(260,100,250,30)
        self.input_search.setPlaceholderText("Entrer mot")
        self.btn = QPushButton(self,text="rechercher")
        self.btn.setGeometry(520,100,150,30)
        self.btn.setStyleSheet("""
            QPushButton{
                               color:black;
                               background-color:red;
                               font-size:20px;
                               border-radius:15px;
                               font-weight:500;
                               }
            QPushButton:hover{
                               background-color:green;}
""")
        self.btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

# verification script python execution
if __name__ =="__main__":
    app = QApplication(sys.argv)
    fen = fenetre()
    fen.show()
    sys.exit(app.exec())




