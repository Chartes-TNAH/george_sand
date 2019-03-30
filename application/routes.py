#
from flask import render_template, request, url_for
# Nous avons ici importé url_for pour créer des URL qui renvoient à nos fonctions et à nos pages HTML
# Import url_for in order to create URLS sending back functions for the HTML pages
from .main import app
from .models.lettres import Lettre
from .models.lieux import Lieu
from .models.correspondants import Correspondant
from sqlalchemy import and_, or_
from datetime import datetime
import random

# Nous avons défini une route en précédant une fonction de '@app.route'
# Chaque route renvoie à une page .html (voir dossier templates/pages)

# Defining route by '@app.route' followed by a function
# Each and every route refers to a .html page (see folder templates/pages)
@app.route("/")
def accueil():
    correspondances = Lettre.query.all()
    return render_template("pages/accueil.html", correspondances = correspondances)

# Nous avons utilisé la fonction render_template pour prendre le chemin du template ainsi que des arguments nommés pour le reste

# Use the render_template function so that it follows the template's path and the arguments

@app.route("/about")
def about():
    return render_template("pages/about.html")

# Nous définissons ici la route vers chacune des lettres, grâce à leur identifiant (sous forme de chiffres (int)).
# Il est important de remettre lettre_id dans les paramètres de la fonction correspondance sinon cela renvoie une erreur

# Here we defined a root leading to each letter, thanks to their id (using an integer)
# it is important to rewrite "lettre_id" in the correspondance function' parameters otherwise it shows an error.
@app.route("/lettre/<int:lettre_id>")
def correspondance(lettre_id):
    unique_correspondance = Lettre.query.get(lettre_id)
    return render_template("pages/lettre.html", correspondance = unique_correspondance)

# Voici la route permettant la recherche plein-texte

# Here is the route leading to a full-text search
@app.route("/search")
def search():
        """ Route permettant la recherche plein-texte
        """
        # On préfèrera l'utilisation de .get() ici
        #   qui nous permet d'éviter un if long (if "clef" in dictionnaire and dictonnaire["clef"])

        # .get() is a way to avoid writing a long "if" (if "key" in dictionary and dictionary["key"])
        motclef = request.args.get("keyword", None)

        date = request.args.get("date", None)

        person = request.args.get("person", None)

        lieu = request.args.get("lieu", None)

        page = request.args.get("page", 1)

        if isinstance(page, str) and page.isdigit():
            page = int(page)
        else:
            page = 1

        results = []

        titre = "Recherche"

        if motclef or date or person or lieu :
            results = Lettre.query.outerjoin(Correspondant).outerjoin(Lieu).filter(
                or_(
                    Lettre.titre.like("%{}%".format(motclef)),
                    Lettre.date_label.like("{}".format(motclef)),
                    Lettre.contenu.like("%{}%".format(motclef)),
                    Lettre.date_norm.like("%{}%".format(motclef)),
                    Correspondant.nom.like("%{}%".format(motclef)),
                    Correspondant.prenom.like("%{}%".format(motclef)),
                    Lieu.label.like("%{}%".format(motclef)),
                    Lettre.date_norm.like("%{}%".format(date)),
                    Lettre.date_label.like("%{}%".format(date)),
                    Correspondant.nom.like("%{}%".format(person)),
                    Correspondant.prenom.like("%{}%".format(person)),
                    Lieu.label.like("%{}%".format(lieu)),
                )
            ).order_by(Lettre.titre.asc()).all()


        return render_template("pages/search.html", results=results, titre=titre, keyword = motclef, date=date, person = person, lieu =lieu)


@app.route("/contact")
def contact():
    return render_template('pages/contact.html')

# Ici, nous écrivons une fonction définissant que si l'application ne trouve pas de contenu,
#  elle doit renvoyer une page erreur 404.
# Se reporter à la page "404.html" dans le dossier errors pour découvrir le message d'erreur renvoyé.

# Here, we wrote a function so that whenever the application does not find any content,
# it displays a special 404 error page.
# Feel free to visit the "404.html" page in the errors folder to discover the error message displayed.
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


# Ici, nous utilisons le module context_processor que nous avons importé plus haut. Il nous sert à mettre toujours
# à jour l'année qui se trouve dans le footer de nos pages, au niveau des crédits.
# Puis nous définissons une fonction appelée inject_now et qui nous permet d'injecter le temps courant.

# Here, we use the context_processor module that we previously imported. We use it so that the year in
# the footer of the pages next to credits is always up to date.
# Then we define a function called  inject_now which allow us to inject the current time.

@app.context_processor
def inject_now():
    return {'now' : datetime.now()}