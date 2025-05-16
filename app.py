from flask import Flask, Response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from models import db, User, Despesa  # importa o db e as classes do models.py
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db' # define url do banco de dados
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # inicializa o db 


@app.route("/")
def home():
    return "Olá, Flask!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# select usuarios
@app.route('/usuarios', methods=["GET"])
def select_users():
    users_classe = User.query.all()
    print(users_classe)

    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)