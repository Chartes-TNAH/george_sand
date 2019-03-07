# Création d'une application nommée George Sand
# Nous avons importé Flask afin de faire fonctionner notre application
# Nous avons importé également la fonction render_template depuis le module flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask("George Sand")

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users/celinechampcourt/data.sqlite"
db = SQLAlchemy(app)

class lettre(db.Model):
    lettre_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    titre = db.Column(db.Text, nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    date_label = db.Column(db.Text, nullable=False)
    date_norm = db.Column(db.Text, nullable=False)
    lettre_expediteur = db.Column(db.Text, db.ForeignKey('correspondant.id_correspondant'))
    lettre_destinataire=db.Column(db.Text, db.ForeignKey('correspondant.id_correspondant'))

class correspondant(db.Model):
    id_correspondant = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    nom = db.Column(db.Text, nullable=False)
    prenom = db.Column(db.Text, nullable=False)

class lieu(db.Model):
    lieu_id=db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    label=db.Column(db.Integer, unique=True, nullable=False)

# Nous avons défini une route en précédent une fonction de '@app.route'

# Nous avons créé un dictionnaire des lettres de George Sand dans le fichier app.py

lettres = {
        0: {
        "titre" : "Lettre 277",
        "date" : "20 mai 1848",
        "destinataire" : "Marc Caussidière",
        "lieu_destinataire" :"Paris"
         },

         1: {
        "titre" : "Lettre 278",
        "date" : "24 mai 1848",
        "destinataire" : "Théophile Thoré",
        "lieu_destinataire" : "Paris"
         },

          2: {
        "titre" : "Lettre 279",
        "date" : "28 mai 1848",
        "destinataire" : "Alexandre Ledru-Rollin",
        "lieu_destinataire" : "Paris"
         },

         3:{
        "titre" : "Lettre 280",
        "date" : "28 mai 1848",
        "destinataire" : "Théophile Thoré",
        "lieu_destinataire" : "Paris"
         },
          4: {
        "titre" : "Lettre 281",
        "date" : "10 juin 1848",
        "destinataire" : "Armand Barbès",
        "lieu_destinataire" : "Vincennes"
           },
         5: {
        "titre" : "Lettre 737",
        "date" : "14 juillet 1870",
        "destinataire" : "Edmond Plauchut",
        "lieu_destinataire" : "Paris"
         },
         6: {
        "titre" : "Lettre 738",
        "date" : "14 juillet 1870",
        "destinataire" : "Juliette Edmond Adam",
        "lieu_destinataire" : "Paris"
         },
        7: {
        "titre" : "Lettre 739",
        "date" : "26 juillet 1870",
        "destinataire" : "Gustave Flaubert",
        "lieu_destinataire" : "Croisset"
         },
         8: {
        "titre" : "Lettre 740",
        "date" : "30 juillet 1870",
        "destinataire" : "Marie-Sophie Leroyer de Chantepie",
        "lieu_destinataire" : "Angers"
        },
         9: {
        "titre" : "Lettre 741",
        "date" : "8 août 1870",
        "destinataire" : "Gustave Flaubert",
        "lieu_destinataire" : "Croisset"
         }
        }
@app.route("/")
def accueil():
    lettres=lettre.query.all()
    return render_template("pages/accueil.html", nom = "Correspondance George Sand", lettres=lettres)

# Nous avons utilisé la fonction render_template pour prendre le chemin du template ainsi que des arguments nommés pour le reste


# Ici nous avons écrit une fonction qui renvoie le contenu de la réponse.


# On lance un serveur de test via app.run()

@app.route("/index/<int:index_id>")
def lettre(index_id):
    unique_lettre=lettre.query.get(index_id)
    return render_template("pages/index.html", nom="Index des lettres de George Sand", lettre=lettres[index_id])


if __name__ == "__main__" :


    app.run()
