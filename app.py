from flask               import Flask, render_template, redirect, url_for, flash, request
from werkzeug.security   import check_password_hash
from flask_login         import login_user, logout_user, login_required, current_user

from extensions          import db, login_manager
from forms               import LoginForm
from models              import User

app = Flask(__name__)

# Configurações
app.config['SECRET_KEY'] = '0000'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'

# Inicializa extensões
db.init_app(app)                    # liga o SQLAlchemy à sua app
login_manager.init_app(app)         # liga o LoginManager à sua app
login_manager.login_view = 'login'  # type: ignore[attr-defined]

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Se já estiver logado, vai direto para a página principal
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('index'))
        flash('E‑mail ou senha incorretos.', 'danger')

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return 'Você está na página inicial!'

    if __name__ == '__main__':
        with app.app_context():
            db.create_all()  # cria tabelas no SQLite (não alterar)
app.run(debug=True)
