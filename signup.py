from PyQt6.QtWidgets import QWidget, QApplication,QLabel,QLineEdit,QPushButton,QDateTimeEdit
from PyQt6.QtGui import QPixmap,QCursor
from PyQt6.QtCore import Qt
from inscsription import login
import sys

class signup(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,500)
        self.photo = QLabel(self)
        fond = QPixmap("image/2013_rainbow_6_patriots-1920x1080.jpg")
        taille_image = fond.scaled(800,500)
        self.photo.setPixmap(taille_image)
        self.photo.setGeometry(0,0,800,500)

        style_text = "color:black; background-color:red;font-size: 30px;border-radius: 10px;padding-left: 20px;padding-left:80px;"
        self.carre = (QLabel(self,text=""))
        self.carre.setGeometry(200,0,400,500)
        self.carre.setStyleSheet("""
            QLabel{
                    background-color:rgba(1,1,0.5,0.5);
            }
        """)
        self.titre = (QLabel(self,text="insription"))
        self.titre.setGeometry(250,20,300,70)
        self.titre.setStyleSheet(style_text)

        self.search = QLabel(self,text="nom")
        self.search.setGeometry(250,90,200,20)
        self.search.setStyleSheet("""
            QLabel{
                                  color:back;
                                  font-size:20px;

                                  }
        """)


        self.input_search = QLineEdit(self)
        self.input_search.setGeometry(250,120,300,30)
        self.input_search.setPlaceholderText("Entrer votre nom")
        self.input_search.setStyleSheet("""
            QLineEdit{
                                        border-radius:15px;
                                        padding-left:10px;
                                        
                                        }

                                        
                                        
        """)
        self.prenom = (QLabel(self,text="prenom"))
        self.prenom.setGeometry(250,160,100,20)
        self.prenom.setStyleSheet("""
            QLabel{
                                  color:black;
                                  font-size:20px;
                                  }

        """)
        self.input_prenom = QLineEdit(self)
        self.input_prenom.setGeometry(250,190,300,30)
        self.input_prenom.setPlaceholderText("Entrer votre prenom")
        self.input_prenom.setStyleSheet("""
            QLineEdit{
                                        border-radius:15px;
                                        padding-left:10px;
                                        }

                                        
                                        
        """)
        self.email= (QLabel(self,text="email"))
        self.email.setGeometry(250,230,100,20)
        self.email.setStyleSheet("""
            QLabel{
                                  color:black;
                                  font-size:20px;
                                  }

        """)
        self.input_email = QLineEdit(self)
        self.input_email.setGeometry(250,260,300,30)
        self.input_email.setPlaceholderText("Email@gmail.com")
        self.input_email.setStyleSheet("""
            QLineEdit{
                                        border-radius:15px;
                                        padding-left:10px;
                                        }

                                        
                                        
        """)

        self.pwd= (QLabel(self,text="password"))
        self.pwd.setGeometry(250,300,100,20)
        self.pwd.setStyleSheet("""
            QLabel{
                                  color:black;
                                  font-size:20px;

                                  }

        """)
        self.input_pwd = QLineEdit(self)
        self.input_pwd.setGeometry(250,330,300,30)
        self.input_pwd.setPlaceholderText("entrer le mot de passe")
        self.input_pwd.setStyleSheet("""
            QLineEdit{
                                        border-radius:15px;
                                        padding-left:10px;
                                        }

                                        
                                        
        """)
        self.input_pwd.setEchoMode(QLineEdit.EchoMode.Password)
        self.pdw_verif= (QLabel(self,text="verification"))
        self.pdw_verif.setGeometry(250,370,100,20)
        self.pdw_verif.setStyleSheet("""
            QLabel{
                                  color:black;
                                  font-size:20px;

                                  }

        """)
        self.input_pdw_verif = QLineEdit(self)
        self.input_pdw_verif.setGeometry(250,400,300,30)
        self.input_pdw_verif.setPlaceholderText("repeter votre mot de passe")
        self.input_pdw_verif.setStyleSheet("""
            QLineEdit{
                                        border-radius:15px;
                                        padding-left:10px;
                                        }
                                
        """)
        self.input_pdw_verif.setEchoMode(QLineEdit.EchoMode.Password)

        self.date = QDateTimeEdit(self)
        self.date.setGeometry(0,0,200,50)


        self.btn = QPushButton(self,text="sign up")
        self.btn.setGeometry(320,440,150,30)
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
        self.btn.clicked.connect(self.login25)
    def login25(self):
        self.login2 = login()
        self.close()
        self.login2.show()
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    inscription =  signup()
    inscription.show()
    sys.exit(app.exec())

