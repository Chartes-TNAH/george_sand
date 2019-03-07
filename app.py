# Création d'une application nommée George Sand
# Nous avons importé Flask afin de faire fonctionner notre application
# Nous avons importé également la fonction render_template depuis le module flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")

app = Flask("George Sand", template_folder=templates, static_folder=statics)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/celinechampcourt/application_george_sand/data-4.sqlite'
db = SQLAlchemy(app)


class Lettre(db.Model):
    lettre_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    titre = db.Column(db.Text, nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    date_label = db.Column(db.Text, nullable=False)
    date_norm = db.Column(db.Text, nullable=False)
    lettre_expediteur = db.Column(db.Text, db.ForeignKey('correspondant.id_correspondant'))
    lettre_destinataire=db.Column(db.Text, db.ForeignKey('correspondant.id_correspondant'))
    depuis_lieu=db.Column(db.Text, db.ForeignKey('lieu.lieu_id'))
    vers_lieu=db.Column(db.Text, db.ForeignKey('lieu.lieu_id'))

class Correspondant(db.Model):
    id_correspondant = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    nom = db.Column(db.Text, nullable=False)
    prenom = db.Column(db.Text, nullable=False)

class Lieu(db.Model):
    lieu_id=db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    label=db.Column(db.Integer, unique=True, nullable=False)

# Nous avons défini une route en précédent une fonction de '@app.route'

# Nous avons créé un dictionnaire des lettres de George Sand dans le fichier app.py


@app.route("/")
def accueil():
    correspondances=Lettre.query.all()
    return render_template("pages/accueil.html", nom = "Correspondance George Sand", correspondances=correspondances)

# Nous avons utilisé la fonction render_template pour prendre le chemin du template ainsi que des arguments nommés pour le reste


# Ici nous avons écrit une fonction qui renvoie le contenu de la réponse.


# On lance un serveur de test via app.run()

@app.route("/lettre/<int:lettre_id>")
def correspondance(lettre_id):
   unique_correspondance = Lettre.query.get(lettre_id)
   return render_template("pages/lettre.html", nom="Index des lettres de George Sand", correspondance=unique_correspondance)


if __name__ == "__main__":

    db.create_all()
    app.run()
