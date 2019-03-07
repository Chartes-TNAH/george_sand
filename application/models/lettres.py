from application.main import db

class Lettre(db.Model):
    lettre_id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True, autoincrement=True)
    titre = db.Column(db.Text, nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    date_label = db.Column(db.Text, nullable=False)
    date_norm = db.Column(db.Text, nullable=False)
    lettre_expediteur = db.Column(db.Text, db.ForeignKey('correspondant.id_correspondant'))
    lettre_destinataire=db.Column(db.Text, db.ForeignKey('correspondant.id_correspondant'))
    depuis_lieu=db.Column(db.Text, db.ForeignKey('lieu.lieu_id'))
    vers_lieu=db.Column(db.Text, db.ForeignKey('lieu.lieu_id'))
