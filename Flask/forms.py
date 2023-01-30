from ast import Pass

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length
from wtforms.widgets import TextArea


class SignupForm(FlaskForm):
    name = StringField("nombre", validators=[DataRequired(), Length(max=25)])
    password = PasswordField("contra", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired(), Email()])
    remember_me = BooleanField("Recuerdame")
    submit = SubmitField("envio_formulario")


class PostForm(FlaskForm):
    title = StringField("Titulo", validators=[DataRequired(), Length(max=128)])
    title_slug = StringField("Titulo slug", validators=[Length(max=128)])
    content = StringField("Contenido", widget=TextArea())
    submit = SubmitField("Enviar")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("Recuerdame")
    submit = SubmitField("envio_formulario")
