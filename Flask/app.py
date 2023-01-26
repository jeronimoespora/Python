from flask import Flask, render_template, url_for, request, redirect
import os

from forms import SignupForm
from forms import PostForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "prueba"

empleados = ["Ana", "Maria", "Sandra", "Juan"]

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


if __name__ == "__main__":

    os.environ["FLASK_ENV"] = "development"
    app.run(debug=True)
