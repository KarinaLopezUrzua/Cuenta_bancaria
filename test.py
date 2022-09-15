from usuario1cuenta import Usuario
from cuentayusuario1cuenta import CuentaBancaria

cuenta1 = CuentaBancaria(0, 0.05)
cuenta2 = CuentaBancaria (100,0.01)
cuenta3 = CuentaBancaria (0,0.01)
"""
cuenta1.deposito(100).retiro(50).generar_interes().mostrar_info_cuenta()
usuario1.cuenta.mostrar_info_cuenta()
"""

usuario1 = Usuario("Karina Lopez", "kari.lopez@gmail.com", 100)
usuario2 = Usuario("Andrea Urzua", "andrea.urzua@gmail.com", 200)
usuario3 = Usuario("Constanza Daniels", "constanza.daniels@gmail.com", 50)

#me muestra la informacion del usuario1
print(usuario1.__dict__)

#cuenta de usuario se asocia y hace deposito con el metodo cuentabancaria
usuario2.cuenta.deposito(200).retiro(50).mostrar_info_cuenta()

#deposito desde metodo usuario
usuario3.hacer_deposito(50).mostrar_balance_usuario()