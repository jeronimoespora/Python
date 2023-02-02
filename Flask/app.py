from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

from forms import SignupForm, LoginForm, PostForm

from flask_login import (
    LoginManager,
    current_user,
    login_user,
    logout_user,
    login_required,
)


from models import User, db, login_manager

app = Flask(__name__)

app.config["SECRET_KEY"] = "prueba"

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:jero@localhost:5432/miwebFlask"


app.config["SQLAlCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager.init_app(app)

login_manager.login_view = "login"


@app.before_first_request
def create_table():
    db.create_all()


elNombre = ""

losPosts = []


@app.route("/")
@app.route("/inicio")
def inicio():

    return render_template("index.html", listaPosts=losPosts)


@app.route("/servicios")
def servicios():
    # return "Esta es la pagina de quienes somos"
    return render_template("servicios.html")


@app.route("/productos")
@login_required
def productos():
    # return "Esta es la pagina de quienes somos"
    return render_template("productos.html")


""" @app.route("/usuarios/<string:nombreusuario>")
def usuarios(nombreusuario):
    return "Bienvenido a la web " + nombreusuario """


@app.route("/usuarios/<int:numerousuario>")
def usuarios(numerousuario):
    # return "Bienvenido a la web. Usuario nº {} ".format(numusuario)
    return render_template("usuarios/usuarios.html", num_usuario=numerousuario)


@app.route("/usuarios/<int:id>/<string:nombreusuario>")
def datosusuario(id, nombreusuario):
    # return "Estos son los datos del usuario. Id: {}. Nombre de usuario: {}".format(
    #    id, nombreusuario
    # )
    return render_template(
        "usuarios/datosusuario.html", id=id, nombreusuario=nombreusuario
    )


@app.route("/posts", methods=["GET", "POST"], defaults={"post_id": None})
@app.route("/posts/<int:npost>", methods=["GET", "POST"])
def posts(post_id):
    global losPosts
    form = PostForm()

    if form.validate_on_submit():
        titulo = form.title.data

        contenido = form.content.data

        post = {"title": titulo, "content": contenido}

        losPosts.append(post)

        return redirect(url_for("inicio"))
    return render_template("entradaBlog.html", form=form)


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    global elNombre
    form = SignupForm()

    if form.validate_on_submit():
        nombre = form.name.data
        correo = form.email.data
        contra = form.password.data

        elNombre = nombre

        return redirect(url_for("inicio"))
    return render_template("contacto.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("inicio"))

    form = LoginForm()

    if form.validate_on_submit():
        email = request.form["email"]
        user = User.query.filter_by(email=email).first()

        if user is not None and user.check_password(request.form["password"]):
            login_user(user)
            return redirect("/productos")

    return render_template("login_form.html", form=form)


@app.route("/registro", methods=["GET", "POST"])
def muestra_registro():

    if current_user.is_authenticated:

        return redirect(url_for("inicio"))

    form = SignupForm()

    if form.validate_on_submit():

        nombre = form.name.data
        email = form.email.data
        password = form.password.data

        user = User(email=email, name=nombre)

        user.set_password(password)

        # login_user(user, remember=True)

        db.session.add(user)

        db.session.commit()

        return redirect(url_for("inicio"))

    return render_template("registro_form.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("inicio"))


if __name__ == "__main__":

    os.environ["FLASK_ENV"] = "development"
    app.run(debug=True)


