from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QSpinBox, QDateEdit, QRadioButton, QComboBox, QFileDialog, QMessageBox
from PyQt6.QtCore import QDate, Qt
import sys
import os
from rqt_sql import Inserer_pers, affichage_poste,prendre_id_postes
import shutil


class Ajout(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(650, 800)

        style_text = "color:orange;font-size:20px;"
        style_input = "color:orange;border:2px solid black;border-radius:15px;font-size:15px;padding-left:15px"

        self.nom = QLabel("nom :", self)
        self.nom.setGeometry(100, 50, 150, 40)
        self.nom.setStyleSheet(style_text)

        self.input_nom = QLineEdit(self)
        self.input_nom.setGeometry(250, 50, 250, 40)
        self.input_nom.setStyleSheet(style_input)

        self.pseudo = QLabel("pseudo :", self)
        self.pseudo.setGeometry(100, 100, 150, 40)
        self.pseudo.setStyleSheet(style_text)

        self.input_pseudo = QLineEdit(self)
        self.input_pseudo.setGeometry(250, 100, 250, 40)
        self.input_pseudo.setStyleSheet(style_input)

        self.age = QLabel("age :", self)
        self.age.setGeometry(100, 150, 150, 40)
        self.age.setStyleSheet(style_text)

        self.input_age = QSpinBox(self)
        self.input_age.setGeometry(250, 150, 250, 40)
        self.input_age.setStyleSheet(style_input)

        self.email = QLabel("Email :", self)
        self.email.setGeometry(100, 200, 150, 40)
        self.email.setStyleSheet(style_text)

        self.input_email = QLineEdit(self)
        self.input_email.setGeometry(250, 200, 250, 40)
        self.input_email.setStyleSheet(style_input)

        self.contact = QLabel("Contact:", self)
        self.contact.setGeometry(100, 250, 150, 40)
        self.contact.setStyleSheet(style_text)

        self.input_contact = QLineEdit(self)
        self.input_contact.setGeometry(250, 250, 250, 40)
        self.input_contact.setStyleSheet(style_input)

        self.date = QLabel("Date :", self)
        self.date.setGeometry(100, 300, 150, 40)
        self.date.setStyleSheet(style_text)

        self.input_date = QDateEdit(self)
        self.input_date.setGeometry(250, 300, 250, 40)
        self.input_date.setStyleSheet(style_input)
        self.input_date.setCalendarPopup(True)
        self.input_date.setDate(QDate.currentDate())
        self.input_date.installEventFilter(self)

        self.Password = QLabel("Password :", self)
        self.Password.setGeometry(100, 350, 150, 40)
        self.Password.setStyleSheet(style_text)

        self.input_Password = QLineEdit(self)
        self.input_Password.setGeometry(250, 350, 250, 40)
        self.input_Password.setStyleSheet(style_input)
        self.input_Password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_Password.setPlaceholderText('enter un mot de passe')

        self.Password_conf = QLabel("matricule :", self)
        self.Password_conf.setGeometry(100, 400, 150, 40)
        self.Password_conf.setStyleSheet(style_text)

        self.input_Password_conf = QLineEdit(self)
        self.input_Password_conf.setGeometry(250, 400, 250, 40)
        self.input_Password_conf.setStyleSheet(style_input)
        self.input_Password_conf.setEchoMode(QLineEdit.EchoMode.Password)
        # self.input_Password_conf.setPlaceholderText('enter un mot de passe')

        self.sexe = QLabel("sexe", self)
        self.sexe.setGeometry(100, 450, 150, 50)
        self.sexe.setStyleSheet(style_text)

        self.sexe_h = QRadioButton('Homme', self)
        self.sexe_h.setGeometry(250, 450, 100, 50)

        self.sexe_f = QRadioButton('Femme', self)
        self.sexe_f.setGeometry(450, 450, 100, 50)

        self.nation = QLabel("Nation", self)
        self.nation.setGeometry(100, 500, 150, 50)
        self.nation.setStyleSheet(style_text)

        self.input_nation = QComboBox(self)
        self.input_nation.setGeometry(250, 500, 250, 50)
        self.input_nation.setStyleSheet(style_input)
        self.input_nation.addItems(
            ["choisir", "Malagasy", "Francais", "Chinois"])

        self.image = QLabel("Image :", self)
        self.image.setGeometry(100, 550, 150, 50)
        self.image.setStyleSheet(style_text)

        self.btn_parcourir = QPushButton("selectionner", self)
        self.btn_parcourir.setGeometry(250, 560, 150, 40)
        self.btn_parcourir.setStyleSheet("""
            QPushButton{
                                        border-radius:15px;
                                        font-size:15px;
                                        background-color:blue;
                                        color:orange;
                                         }
""")
        self.btn_parcourir.clicked.connect(self.prendre_image)

        self.chemin_photo = QLabel(self)
        self.chemin_photo.setGeometry(430, 560, 300, 40)

        self.btn_enregistrer = QPushButton("enregistrer", self)
        self.btn_enregistrer.setGeometry(200, 730, 200, 40)
        self.btn_enregistrer.setStyleSheet("""
            QPushButton{
                                        border-radius:15px;
                                        font-size:15px;
                                        background-color:orange;
                                        color:black;
                                         }
""")
        self.btn_enregistrer.clicked.connect(self.enregistrer)

        self.description = QLabel("poste id :", self)
        self.description.setGeometry(100, 630, 150, 40)
        self.description.setStyleSheet(style_text)

        self.input_description = QComboBox(self)
        self.input_description.setGeometry(250, 630, 250, 40)
        self.input_description.setStyleSheet(style_input)
        postes = affichage_poste()
        valeurs = []
        for x in postes:
            valeurs.append(x[0])
        self.input_description.addItems(valeurs)

                    
        # self.input_description.addItems(["choisir","Malagasy","Francais","Chinois"])

    def prendre_image(self):
        chemin_fichier = QFileDialog()
        chemin_fichier.setNameFilter("Images (*.png *.jpg *.gif *.jpeg *jfif)")
        if chemin_fichier.exec():
            select_fich = chemin_fichier.selectedFiles()
            if select_fich:
                image_path = select_fich[0]
                chemin_relative = os.path.basename(image_path)
                self.chemin_photo.setText(chemin_relative)
                dest = "images_pers"

                if not os.path.exists(dest):
                    os.makedirs(dest)

                chemin = os.path.join(dest, chemin_relative)
                shutil.copy(image_path, chemin)

    def enregistrer(self):
        nom = self.input_nom.text()
        pseudo = self.input_pseudo.text()
        email = self.input_email.text()
        age = self.input_age.value()
        contact = self.input_contact.text()
        date = self.input_date.text()
        mdp1 = self.input_Password.text()
        matricule = self.input_Password_conf.text()

        if self.sexe_h.isChecked():
            sexe = "homme"
        else:
            sexe = "femme"

        sexe = "homme" if self.sexe_h.isChecked() else "femme"

        nat = self.input_nation.currentText()
        image = self.chemin_photo.text()
        poste_id = self.input_description.currentText()

        id_poste = prendre_id_postes(f'{poste_id}')
        Inserer_pers(nom, pseudo, age, contact, email, date,
                     mdp1, sexe, image, nat,id_poste[0], matricule)
        self.message_info()

# envoie message si les inforamation sont bien enregistrer
    def message_info(self):
        message = QMessageBox()
        message.setIcon(QMessageBox.Icon.Information)
        message.setWindowTitle("inforamtion")
        message.setText("donner bien enregister")
        message.setStandardButtons(QMessageBox.StandardButton.Ok)
        message.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    inscription = Ajout()
    inscription.show()
    sys.exit(app.exec())
