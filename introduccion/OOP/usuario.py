class Usuario:
    
    nombre_banco = "Primer Dojo Nacional"
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount

    def hacer_retiro(self, amount):
        if amount > self.balance_cuenta:
            print("Ud esta sobregirado, no puede hacer retiro")
        else:
            self.balance_cuenta -= amount
    
    def mostrar_balance_usuario(self):
        print("USUARIO: ", self.name)
        print("Balance total:", self.balance_cuenta)

    def transfer_dinero(self,usuario_destino, amount):
        if amount > self.balance_cuenta:
            print("Ud esta sobregirado, no puede hacer retiro")
        else:
            self.balance_cuenta -= amount

        usuario_destino.balance_cuenta += amount

michael = Usuario("Michael", "michael@gmail.com")
michael.hacer_deposito(0)
michael.hacer_deposito(20)
michael.hacer_deposito(50)
michael.hacer_retiro(100)
michael.mostrar_balance_usuario()



juan = Usuario("Juan", "juan@gmail.com")
juan.hacer_deposito(50)
juan.mostrar_balance_usuario()

juan.transfer_dinero(michael, 30)

michael.mostrar_balance_usuario()
juan.mostrar_balance_usuario()

print("--"*20)
print(f"Sr. {michael.name} tiene deposito total: {michael.balance_cuenta} dolares")
print(f"Sr. {juan.name} tiene deposito total: {juan.balance_cuenta} dolares")
