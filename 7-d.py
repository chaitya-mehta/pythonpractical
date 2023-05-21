#  Handle possible exceptions in the practical 6_a.

class NoBalance(Exception):
    """You don't have enought balance in your account."""
    pass

class Account:
    def __init__(self, username, balance):
        self.balance = balance
        self.username = username
    def getUserName(self):
        return self.username
    def setUserNmane(self, username):
        self.username = username
    def getBlance(self):
        return self.balance
    def setBalance(self, balance):
        self.balance = balance
    def showBalance(self):
        print("The balance is ", self.balance)
    def withdraw(self, amount):
        try:
            if amount > self.balance or ((self.balance - amount) < 1000):
                raise NoBalance
            else:
                self.balance = self.balance - amount
                print("Your current balance is ", self.balance)
        except NoBalance as e:
            print(e)
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Your current balance is ", self.balance)
    def transfer(self, amount, username):
        try:
            if amount > self.balance or ((self.balance - amount) < 1000):
                raise NoBalance
            else:
                self.balance = self.balance - amount
        except NoBalance:
            print("You don't have enought balance in your account.")
user1 = Account("Abhi", 2000)
user2 = Account("Dhaval", 22000)
user1.transfer(30000, "ajihbwd")
user2.showBalance()