import sqlite3


def Inserer_pers(nom, pseudo, age, contact, email, data, password, sexe, image, nationnalites, postes_id,matricule):
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()
    sql = "INSERT INTO personnels(nom,pseudo,age,contact,email,date,password,sexe,image,nationnalites,postes_id,matricule) VALUES (?,?,?,?,?,?,?,?,?,?,?,?) "
    valeur = (nom, pseudo, age, contact, email, data,
              password, sexe, image, nationnalites, postes_id,matricule)
    cu.execute(sql, valeur)

    # effectuer changement dans un base de donne
    connection.commit()

    # ferneture
    connection.close()

# manka anle donnes rehetra ao anaty base de donnes


# def affichage_PERS():
#     connection = sqlite3.connect("base.db")
#     cu = connection.cursor()
#     sql = "SELECT id,nom,pseudo,age,contact,email,date,password,sexe,image,nationnalites,postes_id,matricule FROM personnels"
#     data = cu.execute(sql)

#     # prendre tous les donne dans la bd
#     res = data.fetchall()

#     connection.close()

#     return res

# print(affichage_PERS())


def suppression(id):
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()
    sql = "DELETE FROM personnels WHERE id = ?"
    cu.execute(sql, (id,))
    connection.commit()
    connection.close()


def modifications(id, nom, pseudo, age, contact, email, data, sexe, nationnalites):
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()
    sql = f" UPDATE personnels SET nom = ?,pseudo = ?,age = ?,contact = ?,email = ?,date = ?,sexe = ?,nationnalites = ? WHERE id = {id}"
    valeur = (nom, pseudo, age, contact, email, data, sexe, nationnalites)
    cu.execute(sql, valeur)
    connection.commit()
    connection.close()


def faire_recherche(mot):
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()
    # requete sql pour recherche dans bases de donne

    sql = "SELECT id,nom,pseudo,age,contact,email,date,password,sexe,image,nationnalites FROM personnels WHERE nom LIKE ? OR pseudo LIKE ? OR age LIKE ?"
    data = cu.execute(sql,(f'%{mot}',f'%{mot}',f'%{mot}',))

    res = data.fetchall()
    connection.close()
    return res


# resaka poste

def inser_postes(nom,desciptions):
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()

    sql = "INSERT INTO postes(nom_poste,description) VALUES (?,?)"
    valeur = (nom,desciptions)

    cu.execute(sql,valeur)
    connection.commit()
    connection.close()

# inser_postes("Informaticien","postes python")
# inser_postes("Mecanicien","specilistes moteur")

def affichage_poste():
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()
    sql = "SELECT DISTINCT nom_poste FROM postes"
    data = cu.execute(sql)

    # prendre tous les donne dans la bd
    res = data.fetchall()

    connection.close()

    return res

# print(affichage_poste())

def prendre_id_postes(nom_poste):
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()

    sql = f'SELECT id FROM postes WHERE nom_poste =?'
    nom = nom_poste
    data = cu.execute(sql,(nom,))
    resu = data.fetchone()
    connection.close()

    return resu

# print(prendre_id_postes('Informaticien'))

def affichage_PERS():
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()
    # left join maka donne ao aminy postes makany aminy pers,right join ou full join aminy alalany id 
    # eto ny postes mjoindre a gauche c'est a dire makao aminy pres
    # --le id voalohany mila precisena
    sql = """SELECT personnels.id,nom,pseudo,age,contact,email,date,password,sexe,image,nationnalites,postes.nom_poste,matricule FROM personnels
    LEFT JOIN postes ON personnels.postes_id = postes.id
    """

    data = cu.execute(sql)
    res =data.fetchall()

    connection.close()
    return res

def prendre_selectionner(id):
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()

    sql = f'SELECT * FROM personnels WHERE id = {id}'
    data = cu.execute(sql)
    res  = data.fetchall()
    connection.close()
    return res


def faire_recherche_poste(mot):
    connection = sqlite3.connect("base.db")
    cu = connection.cursor()
    # requete sql pour recherche dans bases de donne

    sql = f"SELECT personnels.id,personnels.nom,personnels.pseudo,personnels.age,personnels.contact,personnels.email,personnels.date,personnels.password,personnels.sexe,personnels.image,personnels.nationnalites,postes.nom_poste,personnels.matricule FROM personnels JOIN postes ON personnels.postes_id = postes.id WHERE postes.nom_poste LIKE '{mot}' "
    data = cu.execute(sql)

    res = data.fetchall()
    connection.close()
    return res