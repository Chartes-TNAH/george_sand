# george_sand

Application : Correspondances de George Sand, 1840-1870
===

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

*Tous les contenus originaux sont sous licence CC BY-NC-SA 4.0, les ressources extérieures (comme bootstrap) sont sous leur licence respective*


Ce document contient l’ensemble des procédures d'installation des logiciels nécessaires pour démarrer l'application des Correspondance de George Sand, 1840-1870.

##  PyCharm
Nous vous conseillons d'installer [PyCharm](https://www.jetbrains.com/pycharm)

Pour faire fonctionner l'application, Pycharm fonctionne très bien avec Firefox et Chrome. Safari fonctionnera aussi, Internet Explorer peut poser des problèmes.

## Python X ?

Nous avons utilisé Python 3.6. Les versions précédentes peuvent poser des problèmes.


## Installation

### OS X

**Nous vous conseillons d'installer la distribution Anaconda**. Elle contient tous les modules et packages nécessaires pour cette application. Elle est disponible pour toutes les plateformes et possède une procédure d'installation assez simple. Vous pouvez la télécharger depuis http://continuum.io/downloads.  Des détails pour l'installation peuvent être trouvés ici : http://docs.continuum.io/anaconda/install.html 

Utilisez bien la version 3.6 proposée. Une fois installée, clonez ce repository Git.

Les commandes pour installer l'application :
- clonez le repository git en tapant la commande suivante dans votre terminal : git clone https://github.com/Chartes-TNAH/george_sand.git
Puis tapez :
- `cd george_sand` *vous met dans le dossier de l'application*
- `python3 -m venv env` *crée un environnement virtuel dans un sous-dossier. Alternative à `virtualenv -p python3 env` (**A exécuter une fois seulement**)
- `source env/bin/activate` *remplace dans votre session de terminal le lien vers le python 3 global par un lien vers le python 3 de votre environnement virtuel*
- `pip install flask` *installe flask dans votre environnement virtuel* (**A exécuter une fois seulement**)

Soit si l'on sépare entre le à-faire-pour-mettre-en-place et le à-faire-à-chaque-fois :

```sh
git clone https://github.com/Chartes-TNAH/george_sand.git
cd george_sand
python3 -m venv env
source env/bin/activate
pip install flask
```

et 

```sh
cd ~/george_sand
source env/bin/activate
```

#### Note : Suis-je dans un environnement virtuel ?
Si un environnement virtuel est chargé, votre terminal affiche généralement son nom entre parenthèse. Sur ma machine, cela correspond à cela :

```
nom@xxx:~$ source env/bin/activate
(env) nom@xxx:~$
```

On peut tapper la commande `which python` pour savoir où se trouve notre python :

```
nom@xxx:~$ which python
/usr/bin/python
nom@xxx:~$ source env/bin/activate
(env) nom@xxx:~$ which python
home/nom/env/bin/python
```

*Pour savoir quels packages sont installés, vous pouvez taper `pip freeze` dans votre terminal sous votre environnement virtuel*

### Une application simple

Ouvrez le dossier dans Pycharm. Vérifiez que l'application démarre depuis le fichier "run.py". Une fois le code lancé, allez sur [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


## Contributeurs

- Mike Kestemont
- Folgert Karsdorp
- Maarten van Gompel
- Matt Munson
- Thibault Clérice

## Ressources supplémentaires
- http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/
