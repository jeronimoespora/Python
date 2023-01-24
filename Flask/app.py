from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

empleados = ["Ana", "Maria", "Sandra", "Juan"]


@app.route("/")
def hola_mundo():

    return render_template("index.html", numero_empleados=len(empleados))


@app.route("/quienes")
def quienes():
    return "Esta es la pagina de quienes somos"


""" @app.route("/usuarios/<string:nombreusuario>")
def usuarios(nombreusuario):
    return "Bienvenido a la web " + nombreusuario """


@app.route("/usuarios/<int:numusuario>")
def usuarios(numusuario):
    return "Bienvenido a la web. Usuario nº {} ".format(numusuario)


@app.route("/datosusuario/<int:id>/<string:nombreusuario>")
def datosusuario(id, nombreusuario):
    return "Estos son los datos del usuario. Id: {}. Nombre de usuario: {}".format(
        id, nombreusuario
    )


@app.route("/posts")
@app.route("/posts/<int:npost>")
def posts(npost=0):
    return "Este es el post nº {}".format(npost)


if __name__ == "__main__":

    os.environ["FLASK_ENV"] = "development"
    app.run(debug=True)
