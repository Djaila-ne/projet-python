import sqlite3
# from rqt_sql import Inserer_pers
creation_base = sqlite3.connect("base.db")

sql_2 = "ALTER TABLE personnels RENAME TO personnels_2" 
creation_table = """ CREATE TABLE IF NOT EXISTS personnels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    pseudo VARHCAR(50) NOT NULL UNIQUE,
    age INTEGER,
    contact TEXT,
    email TEXT NOT NULL UNIQUE,
    date DATE NOT NULL,
    password TEXT NOT NULL CHECK(length(password)>=8),
    sexe TEXT NOT NULL,
    image TEXT NOT NULL,
    nationnalites TEXT NOT NULL,
    postes_id INTEGER,
    matricule VARCHAR(50),
    FOREIGN KEY (postes_id) REFERENCES postes(id)

    )"""



req_3 = "INSERT INTO personnels(id, nom, pseudo , age, contact, email,date,password,sexe,image,nationnalites,postes_id,matricule) SELECT * FROM personnels_2"

effacer_2 = " DROP TABLE personnels_2"
# excecution anle table / request
# rehefa micreer poste vao2 de
cursor = creation_base.cursor()
# sql = cursor.execute(effacer_2)
# creation_base.commit()
# creation_base.close()



# rename poste
sql = "ALTER TABLE postes RENAME TO postes_pers" 

# rehefa micreer poste vao2 de 
creation_poste = """ CREATE TABLE IF NOT EXISTS postes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_poste VARCHAR(100),
    description TEXT
    )"""

# ajouter les info de postes_pers dans poste
req_2 = "INSERT INTO postes(id,nom_poste,description) SELECT id , nom_poste, description  FROM postes_pers"

effacer = " DROP TABLE postes_pers"

# ajouter une colonne
ajout_1 = "ALTER TABLE personnels ADD COLUMN postes_id INTEGER"

ajout_2 = " ALTER TABLE personnels ADD COLUMN matricule VARCHAR(50)"

# ajout_3 = "ALTER TABLE personnels ADD COLUMN FOREIGN KEY (postes_id) REFERENCES postes(id)"



# cursor.execute()
# creation_base.commit()
# creation_base.close()

# Inserer_pers(creation_table)