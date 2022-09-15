class CuentaBancaria:
    todas_lascuentas = []

    def __init__(self, monto_cuenta, tasa_interes):
        self.cuenta = monto_cuenta
        self.tasa_int = tasa_interes
        CuentaBancaria.todas_lascuentas.append(self)

    @classmethod
    def todas_las_cuentas(cls):
        for cuenta in cls.todas_lascuentas:
            print(f"El balance total de la cuenta es {cuenta.__dict__['cuenta']}")

    def generar_interes (self):
        if self.cuenta > 0:
           self.cuenta = self.cuenta + (self.cuenta * self.tasa_int)
        return self         

    def deposito(self, monto_deposito):
        self.cuenta += monto_deposito
        return self

    def retiro(self,monto_retiro):
        self.cuenta -= monto_retiro
        return self

    def mostrar_info_cuenta(self):
        print(f"El monto total de tu cuenta es de {self.cuenta}")
        return self