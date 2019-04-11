from application.main import db


class Correspondant(db.Model):
    __tablename__ = "correspondant"
    id_correspondant = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    nom = db.Column(db.Text, nullable=False)
    prenom = db.Column(db.Text, nullable=False)
    lettre = db.relationship("Lettre", back_populates="correspondant")


class Lettre(db.Model):
    __tablename__ = "lettre"
    lettre_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    titre = db.Column(db.Text, nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    date_label = db.Column(db.Text, nullable=False)
    date_norm = db.Column(db.Text, nullable=False)
    lettre_destinataire = db.Column(db.Text, db.ForeignKey('correspondant.id_correspondant'))
    lettre_expediteur = db.Column(db.Text)
    vers_lieu = db.Column(db.Text, db.ForeignKey('lieu.lieu_id'))
    depuis_lieu = db.Column(db.Text, db.ForeignKey('lieu.lieu_id'))
    correspondant = db.relationship("Correspondant", back_populates="lettre")

    lieu_envoi = db.relationship("Lieu", foreign_keys=[vers_lieu])
    lieu_expe = db.relationship("Lieu", foreign_keys=[depuis_lieu])


class Lieu(db.Model):
    __tablename__ = "lieu"
    lieu_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    label = db.Column(db.Integer, unique=True, nullable=False)
