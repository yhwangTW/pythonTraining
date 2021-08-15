class Account():
    def __init__(self, number, name):
        self.number = number
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("must be positive")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("amount not enough")


a = Account("123", "45545")
a.deposit(-1000)
a.withdraw(98)
print(a.balance)
