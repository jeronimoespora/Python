class CuentaCorriente:
    def __init__(self, numero, titular, saldo):

        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def getDatos(self):

        return "El titular de la cuenta nº " + self.numero + " es " + self.titular + \
        " y tiene un saldo en cuenta de " + str(self.saldo)
        

    def ingresar(self, cantidad):
        self.saldo = self.saldo + cantidad

    def retirar(self, cantidad):

        self.saldo = self.saldo - cantidad


class CuentaJoven(CuentaCorriente):
    def __init__(self, numero, titular, saldo, bonus_promocion=0):
        super().__init__(numero, titular, saldo)
        self.bonus_promocion = bonus_promocion
        self.saldo += bonus_promocion

    def getBonus(self):

        return self.bonus_promocion

    def getDatos(self):
        return super().getDatos() + " Bonus: " + str(self.bonus_promocion)

    def ingresar(self, cantidad):
        super().ingresar(cantidad)

    def retirar(self, cantidad):
        super().retirar(cantidad)


