class BankAccount:
    def __init__(self, name, balance):
        self.holder_name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount} to your account")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insuficient Balance")
        else:
            self.balance = self.balance - amount
        print(f"{amount} withdrawn from your account")
    def __str__(self):
        return f"Account holder name: {self.holder_name} \nBalance = {self.balance}"
    
c1 = BankAccount("Naman" , 1000)
c1.deposit(200)
print(f"Balance ={c1.balance}")
c1.withdraw(500)
print(c1)


        