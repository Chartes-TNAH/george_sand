from application.main import db
from sqlalchemy.orm import relationship


# Nous avons ici créé une seconde classe (table) pour notre base de données.

# This is the second class (table) of our database

class Lettre(db.Model):
    __tablename__ = "lettre"
    lettre_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    titre = db.Column(db.Text, nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    date_label = db.Column(db.Text, nullable=False)
    date_norm = db.Column(db.Text, nullable=False)
    lettre_destinataire=  db.Column(db.Text, db.ForeignKey('correspondant.id_correspondant'))
    vers_lieu=db.Column(db.Text, db.ForeignKey('lieu.lieu_id'))
    correspondant = db.relationship("Correspondant", back_populates="lettre")
    lieu = db.relationship("Lieu", back_populates="lettre")



