class BankAccount:

    def __init__(self, name, number, money=0):
        self.name = name
        self.number = number
        self.money = money
    
    def __str__(self):
        return (f"{self.name}, {self.number}, amount: {self.money}")

    def __repr__(self):
        return f"BankAccount('{self.name}', '{self.number}', {self.money})"

    def deposit(self, money):
         self.money += money

    def withdraw(self, money):
        self.money -= money

    