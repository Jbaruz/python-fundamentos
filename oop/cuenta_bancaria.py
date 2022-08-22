class CuentaBancaria:
# ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    def __init__(self, name,email):
        self.name = name
        self.email = email
        self.tasa_interes = 0.01
        self.balance = 0
# tu código aquí (recuerda, los atributos de instancia van aquí)
# no te preocupes por la información del usuario aquí; pronto involucraremos la clase de usuario
    def deposito(self, amount):
        self.balance += amount
        return self
# tu código aquí
    def retiro(self, amount):
        if amount > self.balance:
            print("Fondos insuficiente: cobrando una tarifa de $5")
        else:
            self.balance -= amount
        return self
# mostrar _info _cuenta (self) imprime en la consola: por ejemplo, "Balance: $100"
    def mostrar_info_cuenta(self):
        print("Usuario: ", self.name)
        print("Balance:", self.balance)
        return self
        
# generar_interés(self): aumenta el balance de la cuenta por el balance actual * la tasa
#de interés (siempre que el balance sea positivo)
    def generar_interes(self):
        print("Generar interes")
        self.nuevo_interes = self.balance * self.tasa_interes
        print(f"Interese adquirido: {self.nuevo_interes}")
        self.balance = self.balance + self.tasa_interes
        return self

# BONUS NINJA: utiliza un método de clase para imprimir todas las instancias de la
#información de una cuenta bancaria

juan = CuentaBancaria("Juan", "juan@gmail.com")
aisha = CuentaBancaria("Aisha", "aisha@gmail.com")

juan.deposito(100).deposito(10).deposito(10)
juan.mostrar_info_cuenta()
juan.retiro(1050)
juan.mostrar_info_cuenta()
juan.generar_interes()
juan.mostrar_info_cuenta()
print(f"Sr. {juan.name} tiene deposito total: {juan.balance}")
print("--"*20)

aisha.deposito(6660).deposito(7700)
aisha.mostrar_info_cuenta()
aisha.retiro(5).retiro(10).retiro(22).retiro(10)
aisha.mostrar_info_cuenta()
