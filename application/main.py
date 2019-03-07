# Création d'une application nommée George Sand
# Nous avons importé Flask afin de faire fonctionner notre application
# Nous avons importé également la fonction render_template depuis le module flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
templates = os.path.join(chemin_actuel, "templates")
statics = os.path.join(chemin_actuel, "static")
chemin_db = os.path.join(chemin_actuel, "george_sand.sqlite")

# initialize the application
app = Flask("George Sand", template_folder=templates, static_folder=statics)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + chemin_db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# intialize the database
db = SQLAlchemy(app)

# import the different sqlalchemy models
from application.models import lettres, correspondants, lieux

db.create_all()


# import the different routes
import application.routes

# Nous avons défini une route en précédent une fonction de '@app.route'

# Nous avons créé un dictionnaire des lettres de George Sand dans le fichier app.py


