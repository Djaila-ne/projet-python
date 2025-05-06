from PyQt6.QtWidgets import QWidget, QApplication,QLabel,QLineEdit,QPushButton
from PyQt6.QtGui import QPixmap,QCursor
from PyQt6.QtCore import Qt

import sys

class login(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,500)
        self.photo = QLabel(self)
        fond = QPixmap("image/2013_rainbow_6_patriots-1920x1080.jpg")
        taille_image = fond.scaled(800,500)
        self.photo.setPixmap(taille_image)
        self.photo.setGeometry(0,0,800,500)

        self.espace_log = QLabel(self)
        self.espace_log.setGeometry(200,50,400,400)
        self.espace_log.setStyleSheet("background-color:rgba(1,1,0.5,0.7);border-radius:15px;")

        style = "color:white;font-size:20px;"
        style_btn = "color:black;font-size:15px; border-radius:15px;padding-left:10px;"

        self.email = QLabel(self,text="Email :")
        self.email.setGeometry(225,150,150,50)
        self.email.setStyleSheet(style)

        self.input_email = QLineEdit(self)
        self.input_email.setGeometry(350,150,200,40)
        self.input_email.setStyleSheet(style_btn)
        self.input_email.setPlaceholderText("nomprenom@gmail.com")
        
        self.mdp= QLabel(self,text="password :")
        self.mdp.setGeometry(225,220,150,50)
        self.mdp.setStyleSheet(style)

        self.inputmdp = QLineEdit(self)
        self.inputmdp.setGeometry(350,220,200,40)
        self.inputmdp.setStyleSheet(style_btn)
        self.inputmdp.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn = QPushButton(self,text="connexion")
        self.btn.setGeometry(350,280,120,40)
        self.btn.setStyleSheet("""
            QPushButton{
                               font-size:25px;
                               font-weight:500;
                               border-radius:10px;
                               background-color:white;
                               }
            QPushButton:hover{
                               color:red;
                               background-color:black;
                               }
        """)
        self.btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.btn_to_signup = QPushButton(self,text="si pas de compte !! cliquer ici ")
        self.btn_to_signup.setGeometry(300,340,200,50)
        self.btn_to_signup.setStyleSheet("border:none;border-bottom:1px solid black;color:white;")
        self.btn_to_signup.clicked.connect(self.inscription)
    def inscription(self):
        from signup import signup
        self.ouvrir = signup()
        self.ouvrir.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    connex =  login()
    connex.show()
    sys.exit(app.exec())