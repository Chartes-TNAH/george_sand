from application.main import db

class Lieu(db.Model):
    lieu_id=db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    label=db.Column(db.Integer, unique=True, nullable=False)
