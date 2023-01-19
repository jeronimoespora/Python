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


if __name__ == "__main__":

    os.environ["FLASK_ENV"] = "development"
    app.run(debug=True)
