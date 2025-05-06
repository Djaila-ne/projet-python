from PyQt6.QtWidgets import QWidget, QApplication,QPushButton,QLabel,QLineEdit,QComboBox,QFileDialog

from tkinter import filedialog
from yt_dlp import YoutubeDL
import sys

class youtubedown(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600,500)
        self.setWindowTitle("telecharger youtube")

        self.titre = QLabel(self,text="telecharger video youtube")
        self.titre.setGeometry(100,20,500,40)
        self.titre.setStyleSheet('color:red; font-size:15px;')

        self.text = QLabel(self,text=" Ampidiro eto ny rohy \n youtube :")
        self.text.setGeometry(100,100,400,100)
        self.text.setStyleSheet("color :green;font-size:40px;")

        self.lien = QLineEdit(self)
        self.lien.setGeometry(100,220,250,40)
        self.lien.setStyleSheet("border-radius:15px;border:2px solid black;")

        self.btn = QPushButton(self,text="Telecharger")
        self.btn.setGeometry(100,380,200,40)
        self.btn.setStyleSheet("border-radius:15px;border:2px solid black;")
        self.btn.clicked.connect(self.telecharger)

        self.format = QComboBox(self)
        self.format.addItems(["choix","mp3","mp4"])
        self.format.setGeometry(100,300,100,40)


    def telecharger(self):
        dest_fichier = filedialog.askdirectory()
        lien = self.lien.text()
        format = self.format.currentText()

        if lien and format and dest_fichier:
            try:
                videos_down = {
                    "format":format,
                    "outtmpl" : f"{dest_fichier}/%(title)s.%(ext)s",
                }

                with YoutubeDL(videos_down) as ydl:
                    ydl.download([lien])
                    print('videos bien telecharger')
            except:
                print('error')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    telecharger58 =  youtubedown()
    telecharger58.show()
    sys.exit(app.exec())