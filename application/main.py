# Création d'une application nommée George Sand
# Avant toute chose, nous avons installé flask-sqlalchemy via le terminal de l'environnement virtuel sur PyCharm.
# Nous avons importé Flask afin de faire fonctionner notre application
# Nous avons importé également la fonction render_template depuis le module flask

# Creation of an application entitled George Sand
# First, we installed flask-sqlalchemy using the terminal of the virtual environment on PyCharm
# Then we imported Flask in order to run our application properly
# And we imported the render_template function from the flask module

from flask import Flask, request

# Nous avons ensuite importé SQLAlchemy afin de pouvoir travailler sur notre base de données via notre application Python.

# We imported SQLAlchemy to work on our database via the Python application

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, cast
from sqlalchemy.orm import backref
from sqlalchemy.dialects.postgresql import INET

import os


chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")
chemin_db = os.path.join(chemin_actuel, "george_sand.sqlite")

# Nous avons instancié  flask

# initialize the application by instancing flask

app = Flask("George Sand", template_folder=templates, static_folder=statics)

#grâce à la configuration debug = True, si nous avons une erreur, la page montrera les détails de cette erreur

# configuration of debug = True so that whenever we get an error, details are shown on the landing page

app.config['DEBUG'] = True
# La seule configuration dont nous avons eu besoin était la Database_URI.
# Nous avons configuré notre base de données en indiquant le chemin vers notre
# database qui s'intitule "george_sand.sqlite".

# The only configuration we needed here was Database_URI
# we configured our database by pointing out the path leading to our database
# entitled "george_sand.sqlite"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + chemin_db
# Track_modifications nous permet ici de suivre les modifications faites dans notre base de données.

# Track_modifications allows us to follow modifications in our database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Nous avons instancié flask-SQLAlchemy par la commande suivante :

# intialize the database and instancing flask-SQLAlchemy by the following command :
db = SQLAlchemy(app)

# A partir de ces quelques manipulations, nous avons pu créer notre base de données.

# After some manipulations we were able to create our database

# import the different sqlalchemy models
from application.models.donnees import Lettre, Lieu, Correspondant

# La ligne de code suivante nous a permis de remplir notre base de données à partir d'une base vide.

#db.create_all()


# import the different routes
import application.routes




