class CuentaCorriente:
    def __init__(self, numeroCuenta, titularCuenta, saldoCuenta):
        self.numeroCuenta = numeroCuenta
        self.titularCuenta = titularCuenta
        self.saldoCuenta = saldoCuenta

    def getDatos(self):
        return ("El titular de la cuenta es: "+ self.titularCuenta +". Su numero de cuenta es: "+
            self.numeroCuenta + \
            ". Y su saldo actual es:  " + str(self.saldoCuenta)
        )

    def deposit(self, toDepost):
        self.saldoCuenta = self.saldoCuenta + toDepost

    def extract(self, toExtract):
        self.saldoCuenta = self.saldoCuenta - toExtract


cuenta1 = CuentaCorriente("153846", "Pedro Longoria", 1500)
print(cuenta1.getDatos())
cuenta1.deposit(1500)
print(cuenta1.getDatos())
cuenta1.extract(1000)
print(cuenta1.getDatos())
