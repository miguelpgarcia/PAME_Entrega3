from app.extensions import db

class Receita (db.Model):
    __tablename__ = "receita"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(20), nullable = False)
    