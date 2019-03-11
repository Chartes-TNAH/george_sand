from application.main import db

# Nous avons ici créé une troisième classe (table) pour notre base de données.

class Lieu(db.Model):
    __tablename__  = "lieu"
    lieu_id=db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    label=db.Column(db.Integer, unique=True, nullable=False)
    lettre = db.relationship("Lettre", back_populates="lieu")
