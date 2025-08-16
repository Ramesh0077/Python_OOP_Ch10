# 5. Accessing Instance Variables from Another Method
# Create a BankAccount class.
# In __init__, store account holder name and balance.
# Create a method deposit(amount) that updates balance.
# Create a method show_balance() to print the balance.

class BankAccount:
    
    def __init__(self,name,balance):
        self.name=name 
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def show_balance(self):
        print(f"Balance:{self.balance}")

account=BankAccount("Ramesh",1500000)
account.deposit(120000)
account.show_balance()
print(account.balance)
        