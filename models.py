from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def set_password(self, raw_password: str):
        """Gera o hash da senha e salva em self.password."""
        self.password = generate_password_hash(raw_password)

    def check_password(self, raw_password: str) -> bool:
        """Compara raw_password com o hash salvo."""
        return check_password_hash(self.password, raw_password)

    def __repr__(self):
        return f'<User {self.email}>'