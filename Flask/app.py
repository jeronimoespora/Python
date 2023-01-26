from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

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


@app.route("/contacto")
def contacto():
    return render_template("Contacto.html")


if __name__ == "__main__":

    os.environ["FLASK_ENV"] = "development"
    app.run(debug=True)
