from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QDateTimeEdit, QTableWidget, QTableWidgetItem, QAbstractItemView, QFrame, QMessageBox, QFileDialog,QComboBox
from PyQt6.QtGui import QPixmap, QCursor, QColor
from PyQt6.QtCore import Qt
from openpyxl import Workbook
import pdfkit
import sys
import os
from rqt_sql import affichage_PERS, suppression, modifications, faire_recherche,prendre_selectionner,faire_recherche_poste,affichage_poste


class Affichage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tableau d'affichage")
        self.setFixedSize(1000, 600)

        self.listes_pers = QLabel(self, text="nombre pers :")
        self.listes_pers.setGeometry(50, 50, 200, 50)
        self.listes_pers.setStyleSheet("color:red; font-size:25px; ")

        self.recherche = QLineEdit(self)
        self.recherche.setGeometry(300, 60, 200, 30)
        self.recherche.setStyleSheet(
            "border-radius:15px;font-size:15px;padding-left:15px;border:1px solid black;")
        self.recherche.setPlaceholderText("recherche")
        # --fonction recherche
        self.recherche_btn = QPushButton("recherche", self)
        self.recherche_btn.setGeometry(510, 60, 100, 30)
        self.recherche_btn.setStyleSheet(
            "border-radius:15px;font-size:15px;background-color:red;border:1px solid black;")
        self.recherche_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.recherche_btn.clicked.connect(self.rechercher)

        # --button to transforme en excel
        self.btn_excelpopop = QPushButton(self, text='Imprimer excel')
        self.btn_excelpopop.setGeometry(100, 520, 200, 50)
        self.btn_excelpopop.clicked.connect(self.importer_excel)
        # filter par poste
        self.poste_filter = QComboBox(self)
        self.poste_filter.setGeometry(700,60,200,30)
        option = ["postes",]
        for x in affichage_poste():
            for y,o in enumerate(x):
                option.append(o)
        self.poste_filter.addItems(option)
        # maka anle mot ao amle combo box
        self.poste_filter.currentIndexChanged.connect(self.affiche_filter)
        # --boutton transforme en pdf
        self.btn_pdf = QPushButton(self, text="transformer en pdf")
        self.btn_pdf.setGeometry(700, 520, 200, 50)
        self.btn_pdf.clicked.connect(self.importer_pdf)

        # autre
        donne_pers = affichage_PERS()

        print(donne_pers)

        self.nbr = QLabel(self, text=str(len(donne_pers)))
        self.nbr.setGeometry(250, 50, 100, 50)
        self.nbr.setStyleSheet("font-size:25px;")

        # creation tableau
        nbr_ligne = len(donne_pers)
        nbr_colonne = 15
        self.table = QTableWidget(nbr_ligne, nbr_colonne, self)
        # self.table.setRowCount(10)
        # self.table.setColumnCount(13)
        self.table.setGeometry(100, 120, 800, 400)
        # changer le nom des colomn
        self.table.setHorizontalHeaderLabels(["id", "nom", "pseudo", "age", "contact", "email", "date",
                                             "password", "sexe", "image", "nationnaliter", "poste id", "matricule", "modifier", "supprimer"])
        self.table.setStyleSheet("""
                QTableWidget{
                                 background-color:#333;
                                 border:1px solid black;
                                 font-size:15px;
                                 }
                QTableWidget::item{
                                 padding:2px;
                                 }
                QTableWidget::item:selected{
                                background-color:orange;
                                color:white;
                                 }
""")
        # modification header
        header = self.table.horizontalHeader()
        header.setStyleSheet("""
                QHeaderView::section{
                             background-color:red;
                             color:white;
                             font-weight:bold;
                             }
""")
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)

        # manageza anle colomn
        self.table.setColumnWidth(3, 50)
        self.table.setColumnWidth(0, 0)
        self.table.setColumnWidth(9, 55)

        # augmenter la taille de l'image
        self.table.itemClicked.connect(self.afficher_image)

        # le btn_modifier en fonstion du ligne
        for i in range(nbr_ligne):
            btn_modifier = QPushButton("modifier")
            btn_modifier.setStyleSheet("background-color:aqua;")
            self.table.setCellWidget(i, 13, btn_modifier)
            btn_modifier.clicked.connect(self.modifier(i))

        for i in range(nbr_ligne):
            btn_supprimer = QPushButton("suppriner")
            btn_supprimer.setStyleSheet("background-color:green;")
            self.table.setCellWidget(i, 14, btn_supprimer)
            btn_supprimer.clicked.connect(self.supprimer_ligne(i))

        for ligne, liste in enumerate(donne_pers):
            for col, value in enumerate(liste):
                # print(col)
                if col == 9:
                    if value:
                        label = QLabel()
                        pixmap = QPixmap(f"images_pers/{value}")
                        taille = pixmap.scaled(50, 50)
                        label.setPixmap(taille)
                        self.table.setCellWidget(ligne, col, label)
                        item = QTableWidgetItem(f"images_pers/{value}")
                        self.table.setItem(ligne, 9, item)
                        item.setForeground(QColor(0, 0, 0, 0))
                else:
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(ligne, col, item)

        self.fenetre_popup = QFrame(self)
        self.fenetre_popup.setGeometry(100, 120, 500, 300)
        self.fenetre_popup.setVisible(False)
        self.fenetre_popup.setStyleSheet(
            "background-color:blue;border-radius:10px;")

        self.label_image = QLabel(self.fenetre_popup)
        self.label_image.setGeometry(0, 0, 500, 300)

        self.btn_fermer = QPushButton(self.fenetre_popup, text="X")
        self.btn_fermer.setGeometry(460, 0, 40, 20)
        self.btn_fermer.setStyleSheet("""
            QPushButton{
                                      background-color:none;
                                      color:black;
                                      }
            QPushButton:hover{
                                      background-color:red;
                                      color:black;
                                      border-radius:none;
                                      }                                      
""")
        self.btn_fermer.clicked.connect(self.fermer)

    # modifications()
    def afficher_image(self, item):
        res = self.table.selectedItems()
        res.sort(key=lambda x: x.row())
        valeur = [item.text() for item in res]
        # print(valeur)
        col = item.column()
        row = item.row()
        # print(row)
        chemin_image = item.text()

        if col == 9:
            self.images = QPixmap(chemin_image)
            self.label_image.setPixmap(self.images.scaled(800, 380))
            self.fenetre_popup.setVisible(True)
        

        self.id = self.table.item(row,0).text()
        # print(self.id)

        self.resultat = prendre_selectionner(self.id)
        print(self.resultat)

    # affiche poste
    def affiche_filter(self,index):
        valeur = self.poste_filter.currentText()
        resultat = faire_recherche_poste(valeur)
        print(resultat)
        self.table.setRowCount(len(resultat))
        for i in range(len(resultat)):
            btn_modifier = QPushButton("modifier")
            btn_modifier.setStyleSheet("background-color:aqua;")
            self.table.setCellWidget(i, 13, btn_modifier)
            btn_modifier.clicked.connect(self.modifier(i))

        for i in range(len(resultat)):
            btn_supprimer = QPushButton("suppriner")
            btn_supprimer.setStyleSheet("background-color:green;")
            self.table.setCellWidget(i, 14, btn_supprimer)
            btn_supprimer.clicked.connect(self.supprimer_ligne(i))

        for ligne, liste in enumerate(resultat):
            for col, value in enumerate(liste):
                if col == 9:
                    if value:
                        label = QLabel()
                        pixmap = QPixmap(f"images_pers/{value}")
                        taille = pixmap.scaled(50, 50)
                        label.setPixmap(taille)
                        self.table.setCellWidget(ligne, col, label)
                        item = QTableWidgetItem(f"images_pers/{value}")
                        self.table.setItem(ligne, 9, item)
                        item.setForeground(QColor(0, 0, 0, 0))
                else:
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(ligne, col, item)

    # ouvrir excel
    def importer_excel(self):
        try:
            donner = affichage_PERS()
            ouvr_excel = Workbook()
            fenetre_excel = ouvr_excel.active
            header = ["id", "nom", "pseudo", "age", "contact", "email", "date",
                      "password", "sexe", "image", "nationnaliter", "poste id", "matricule",]
            fenetre_excel.append(header)
            for listes in donner:
                fenetre_excel.append(listes)
            dest, _ = QFileDialog.getSaveFileName(
                self,'enregistrer', '', 'fichier excele(*.xlsx)')
            ouvr_excel.save(dest)
        except ValueError as e:
            print(f'erreur{e}')
    
    # transformer un pdf en site
    def importer_pdf(self):
        chemin_pdf, _ = QFileDialog.getSaveFileName(
            self, 'Enregistrer', '', 'fichier pdf(*.pdf)')
        if chemin_pdf:
            htmlpdf = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Facture</title>
            </head>
            <body style="font-family: Arial, sans-serif; margin: 20px;">
                <header style="text-align: center; margin-bottom: 40px;">
                    <h1 style="margin: 0;">Facture</h1>
                    <p style="margin: 0;">Date: <span id="date">01/01/2023</span></p>
                </header>
                   <section style="margin-bottom: 40px;">
                    <h2 style="margin-bottom: 10px;">Informations du client</h2>
                    <p style="margin: 5px 0;">Nom: <span id="client-name">Jean Dupont</span></p>
                    <p style="margin: 5px 0;">Adresse: <span id="client-address">123 Rue Exemple, Paris</span></p>
                    <p style="margin: 5px 0;">Téléphone: <span id="client-phone">+33 6 12 34 56 78</span></p>
                </section>

                <section style="margin-bottom: 40px;">
                    <h2 style="margin-bottom: 10px;">Détails de la facture</h2>
                    <table style="width: 100%; border-collapse: collapse;">
                        <thead>
                            <tr>
                                <th style="border: 1px solid #000; padding: 8px; text-align: left;">Description</th>
                                <th style="border: 1px solid #000; padding: 8px; text-align: right;">Quantité</th>
                                <th style="border: 1px solid #000; padding: 8px; text-align: right;">Prix Unitaire</th>
                                <th style="border: 1px solid #000; padding: 8px; text-align: right;">Total</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="border: 1px solid #000; padding: 8px;">{self.resultat[0][5]}</td>
                                <td style="border: 1px solid #000; padding: 8px; text-align: right;">2</td>
                                <td style="border: 1px solid #000; padding: 8px; text-align: right;">50€</td>
                                <td style="border: 1px solid #000; padding: 8px; text-align: right;">100€</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #000; padding: 8px;">{self.resultat[0][1]}</td>
                                <td style="border: 1px solid #000; padding: 8px; text-align: right;">1</td>
                                <td style="border: 1px solid #000; padding: 8px; text-align: right;">30€</td>
                                <td style="border: 1px solid #000; padding: 8px; text-align: right;">30€</td>
                            </tr>
                        </tbody>
                        <tfoot>
                             <tr>
                                <td colspan="3" style="border: 1px solid #000; padding: 8px; text-align: right; font-weight: bold;">Total</td>
                                <td style="border: 1px solid #000; padding: 8px; text-align: right; font-weight: bold;">130€</td>
                            </tr>
                        </tfoot>
                    </table>
                </section>
                <footer style="text-align: center; margin-top: 40px;">
                    <p style="margin: 0;">{self.resultat[0][11]}</p>
                </footer>
            </body>
            </html>
            """
            # r = rowstring mamadika ho caractere str 
            # teto ny \\ no nahatonga anle izy
            try:
                path_html_pdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
                config = pdfkit.configuration(wkhtmltopdf = path_html_pdf)
                pdfkit.from_string(htmlpdf,chemin_pdf,configuration=config)
            except Exception as e:
                print(f'erreur {e}')
    
    def fermer(self):
        self.fenetre_popup.setVisible(False)

        # print(col,row,chemin_image)
    
    def supprimer_ligne(self, row):
        return lambda: self.action_supprimer(row)
    
    def action_supprimer(self, row):
        self.id = self.table.item(row, 0).text()
        self.table.removeRow(row)
        suppression(self.id)
    
    def modifier(self, row):
        return lambda: self.action_modification(row)

    def action_modification(self, row):
        self.id = self.table.item(row, 0).text()
        # print(self.id)
        nom = self.table.item(row, 1).text()
        pseudo = self.table.item(row, 2).text()
        age = self.table.item(row, 3).text()
        contact = self.table.item(row, 4).text()
        email = self.table.item(row, 5).text()
        date = self.table.item(row, 6).text()
        sexe = self.table.item(row, 8).text()
        nation = self.table.item(row, 10).text()
        # matricule = self.table.item(row,11).text()
        try:
            modifications(self.id, nom, pseudo, age,
                          contact, email, date, sexe, nation)
            QMessageBox.information(
                self, " success ", "personnel modifier avec success")

        except Exception as e:
            QMessageBox.critical(self, 'erreur', f'erreur de modification {e}')

    def rechercher(self):
        mot_rechercherna = self.recherche.text()
        resultat = faire_recherche(mot_rechercherna)
        self.table.setRowCount(len(resultat))

        for i in range(len(resultat)):
            btn_modifier = QPushButton("modifier")
            btn_modifier.setStyleSheet("background-color:aqua;")
            self.table.setCellWidget(i, 12, btn_modifier)
            btn_modifier.clicked.connect(self.modifier(i))

        for i in range(len(resultat)):
            btn_supprimer = QPushButton("suppriner")
            btn_supprimer.setStyleSheet("background-color:green;")
            self.table.setCellWidget(i, 13, btn_supprimer)
            btn_supprimer.clicked.connect(self.supprimer_ligne(i))

        for ligne, liste in enumerate(resultat):
            for col, value in enumerate(liste):
                if col == 9:
                    if value:
                        label = QLabel()
                        pixmap = QPixmap(f"images_pers/{value}")
                        taille = pixmap.scaled(50, 50)
                        label.setPixmap(taille)
                        self.table.setCellWidget(ligne, col, label)
                        item = QTableWidgetItem(f"images_pers/{value}")
                        self.table.setItem(ligne, 9, item)
                        item.setForeground(QColor(0, 0, 0, 0))
                else:
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(ligne, col, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    aff = Affichage()
    aff.show()
    sys.exit(app.exec())