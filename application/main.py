# Création d'une application nommée George Sand
# Avant toute chose, nous avons installé flask-sqlalchemy via le terminal de l'environnement virtuel sur PyCharm.
# Nous avons importé Flask afin de faire fonctionner notre application
# Nous avons importé également la fonction render_template depuis le module flask
from flask import Flask
# Nous avons ensuite importé SQLAlchemy afin de pouvoir travailler sur notre base de données via notre application Python.
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, cast
from sqlalchemy.orm import backref
from sqlalchemy.dialects.postgresql import INET

import os

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")
chemin_db = os.path.join(chemin_actuel, "george_sand.sqlite")

# initialize the application
# Nous avons instancié  flask
app = Flask("George Sand", template_folder=templates, static_folder=statics)
app.config['DEBUG'] = True
# La seule configuration dont nous avons eu besoin était la Database_URI.
# Nous avons configuré notre base de données en indiquant en appelant le chemin vers notre
# database qui s'intitule "george_sand.sqlite".
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + chemin_db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# intialize the database
# Nous avons instancié flask-SQLAlchemy par la commande suivante :
db = SQLAlchemy(app)

# A partir de ces quelques manipulations, nous avons pu créer notre base de données.

# import the different sqlalchemy models
from application.models import lettres, correspondants, lieux
# La ligne de code suivante nous a permis de remplir notre base de données à partir d'une base vide.
# Cela nous a permis de la créer en quelque sorte :
db.create_all()


# import the different routes
import application.routes

# Nous avons défini une route en précédent une fonction de '@app.route'

# Nous avons créé un dictionnaire des lettres de George Sand dans le fichier app.py


