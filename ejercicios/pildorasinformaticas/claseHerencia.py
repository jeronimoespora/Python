class CuentaCorriente:
    def __init__(self, numero, titular, saldo):

        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def getDatos(self):
        return (
            "El titular de la cuenta nº "
            + self.numero
            + " es "
            + self.titular
            + " y tiene un saldo en cuenta de "
            + str(self.saldo)
        )

    def ingresar(self, cantidad):
        self.saldo = self.saldo + cantidad

    def retirar(self, cantidad):

        self.saldo = self.saldo - cantidad

        def getBonus(self):
            return self.bonus_promocion

    def getDatos(self):
        return super().getDatos() + " Bonus: " + str(self.bonus_promocion)

    def ingresar(self, cantidad):
        super().ingresar(cantidad)

    def retirar(self, cantidad):
        super().retirar(cantidad)


class CuentaJoven(CuentaCorriente):
    def __init__(self, numeroCuenta, titularCuenta, saldoCuenta):
        super().__init__(numeroCuenta, titularCuenta, saldoCuenta)
