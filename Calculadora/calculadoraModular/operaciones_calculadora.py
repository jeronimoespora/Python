from tkinter import *

from resultados_pantalla import *


def pulsaciones_teclas(self, valor, mostrar):

    if mostrar:
        self.operacion += str(valor)
        mostrar_pantalla(self, valor)
    elif not mostrar and valor == "=":
        # self.operacion = re.sub("\u00D7", "*", self.operacion) problema con el "re"
        borrar_pantalla(self)
        mostrar_pantalla(self, str(eval(self.operacion)))
    else:
        pass
