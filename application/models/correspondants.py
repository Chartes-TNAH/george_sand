from application.main import db


# Nous avons ici créé une première classe (table) pour notre base de données.
class Correspondant(db.Model):
    __tablename__ = "correspondant"
    id_correspondant = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    nom = db.Column(db.Text, nullable=False)
    prenom = db.Column(db.Text, nullable=False)
    lettre = db.relationship("Lettre", back_populates="correspondant")

