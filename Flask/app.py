from flask import Flask, render_template, url_for, request, redirect
import os

from forms import SignupForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "prueba"

empleados = ["Ana", "Maria", "Sandra", "Juan"]


@app.route("/")
@app.route("/inicio")
def inicio():

    return render_template("index.html", numero_empleados=len(empleados))


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


@app.route("/posts")
@app.route("/posts/<int:npost>")
def posts(npost=0):
    return "Este es el post nº {}".format(npost)


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    form = SignupForm()

    if form.validate_on_submit():
        nombre = form.name.data
        correo = form.email.data
        contra = form.password.data

        return redirect(url_for("inicio"))
    return render_template("contacto.html", form=form)


if __name__ == "__main__":

    os.environ["FLASK_ENV"] = "development"
    app.run(debug=True)
