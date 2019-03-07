from flask import render_template
from .main import app
from .models.lettres import Lettre

@app.route("/")
def accueil():
    correspondances=Lettre.query.all()
    return render_template("pages/accueil.html", nom = "Sand", correspondances=correspondances)

# Nous avons utilisé la fonction render_template pour prendre le chemin du template ainsi que des arguments nommés pour le reste


# Ici nous avons écrit une fonction qui renvoie le contenu de la réponse.


# On lance un serveur de test via app.run()

@app.route("/lettre/<int:lettre_id>")
def correspondance(lettre_id):
   unique_correspondance = Lettre.query.get(lettre_id)
   return render_template("pages/lettre.html", nom="Sand", correspondance=unique_correspondance)
