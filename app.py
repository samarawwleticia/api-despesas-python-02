from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# Configurações
app.config['SECRET_KEY'] = '0000'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db' 

# Inicializa extensões
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Nome da função de login


# Roda o app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria as tabelas se ainda não existirem
    app.run(debug=True)


