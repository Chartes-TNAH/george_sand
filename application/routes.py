from flask import render_template
from .main import app
from .models.lettres import Lettre
from .models.lieux import Lieu
from .models.correspondants import Correspondant



@app.route("/")
def accueil():
    correspondances = Lettre.query.all()
    return render_template("pages/accueil.html", correspondances = correspondances)

# Nous avons utilisé la fonction render_template pour prendre le chemin du template ainsi que des arguments nommés pour le reste


# Ici nous avons écrit une fonction qui renvoie le contenu de la réponse.

@app.route("/about")
def about():
    return render_template("pages/about.html")

@app.route("/lettre/<int:lettre_id>")
def correspondance(lettre_id):
    unique_correspondance = Lettre.query.get(lettre_id)
    return render_template("pages/lettre.html", correspondance = unique_correspondance)
def correspondant(nom):
    unique_correspondant = Correspondant.query.get(nom)
    return render_template("pages/lettre.html", correspondant = unique_correspondant)