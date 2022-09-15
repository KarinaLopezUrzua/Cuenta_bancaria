from cuentayusuario1cuenta import CuentaBancaria

class Usuario:
    def __init__(self, nombre_usuario, email_usuario, numero_cuenta):
        self.nombre = nombre_usuario
        self. mail = email_usuario
        #self.cuenta = 100. enlazamos usuario con cuentabancaria a traves de la instancia cuenta
        self.cuenta = CuentaBancaria(monto_cuenta=0, tasa_interes=0.02)
        #los argumentos en cuenta bancaria seria monto_cuenta=0, tasa_interes=0.02
        #tambien se puede escribir asi, self.cuenta = CuentaBancaria(0,0.02)
        
        #se asocia con metodo deposito
        #se puede tener este metodo o bien eliminarlo 
        #y quedarse con el de cuenta bancaria
    def hacer_deposito(self, monto):
        self.cuenta.deposito(monto) 
        return self

    def mostrar_balance_usuario(self):        
        #para ocupar este metodo, asociamos con cuenta bancaria
        self.cuenta.mostrar_info_cuenta()
        # #print(f"El usuario {self.nombre} tiene una cuenta final de {self.cuenta}")
        return self

"""
    #forma como se asocia con metodo retiro, pero se puede eliminar
    def hacer_retiro(self, monto_retiro):
        self.cuenta.retiro()
    return self
"""