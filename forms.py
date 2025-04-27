from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField(
        'E‑mail',
        validators=[DataRequired(message="O e‑mail é obrigatório"),
                    Email(message="Formato de e‑mail inválido"),
                    Length(max=150)]
    )
    password = PasswordField(
        'Senha',
        validators=[DataRequired(message="A senha é obrigatória"),
                    Length(min=6, message="Mínimo de 6 caracteres")]
    )
    remember = BooleanField('Lembrar‑me')
    submit = SubmitField('Entrar')