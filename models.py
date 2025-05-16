from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=True)
    senha = db.Column(db.String(13), nullable=True)

class Despesa(db.Model):
    __tablename__ = 'despesa'
    idDespesa = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.Text, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.Text, nullable=False)
    dataCompra = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", backref=db.backref("despesas", lazy=True))
