#
from flask import render_template, request, url_for
# Nous avons ici importé url_for pour créer des URL qui renvoient à nos fonctions et à nos pages HTML
from .main import app
from .models.lettres import Lettre
from .models.lieux import Lieu
from .models.correspondants import Correspondant
from sqlalchemy import and_, or_

# Nous avons défini une route en précédent une fonction de '@app.route'

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

@app.route("/search")
def search():
        """ Route permettant la recherche plein-texte
        """
        # On préfèrera l'utilisation de .get() ici
        #   qui nous permet d'éviter un if long (if "clef" in dictionnaire and dictonnaire["clef"])
        motclef = request.args.get("keyword", None)
        page = request.args.get("page", 1)

        if isinstance(page, str) and page.isdigit():
            page = int(page)
        else:
            page = 1

        results = []

        titre = "Recherche"

        if motclef:
            results = Lettre.query.outerjoin(Correspondant).outerjoin(Lieu).filter(
                or_(
                    Lettre.titre.like("%{}%".format(motclef)),
                    Lettre.date_label.like("%{}%".format(motclef)),
                    Lettre.contenu.like("%{}%".format(motclef)),
                    Lettre.date_norm.like("%{}%".format(motclef)),
                    Correspondant.nom.like("%{}%".format(motclef)),
                    Correspondant.prenom.like("%{}%".format(motclef)),
                    Lieu.label.like("%{}%".format(motclef)),
                )
            ).order_by(Lettre.titre.asc()).all()
            titre = "Résultat pour la recherche `" + motclef + "`"

        return render_template("pages/search.html", results=results, titre=titre, keyword = motclef)

@app.route("/results")
def results():
    return render_template("pages/results.html")

@app.route("/contact")
def contact():
    return render_template('pages/contact.html')
