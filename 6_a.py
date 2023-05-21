class Chaitya:
    def __init__(self,username,balance):
        self.username=username
        self.balance=balance
    def getusername(self):
        return self.username
    def setusername(self,username):
        self.username=username
    def getbalance(self):
        return self.balance
    def setbalance(self,balance):
        self.balance=balance  
    def showBalance(self):
        print("Balance Is ",self.balance)
    def withdraw(self,amount):
        if amount>self.balance or(self.balance-amount)<1000:
            print("You dont withdraw the amount")        
        else:
            self.balance=self.balance-amount
            print("Your current Balance is",self.balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("self.balance")
    def transfer(self,amount,username):
        if amount>self.balance or (self.balance-amount<1000):
            print("You don't have sufficient amount to transfer the money")
            print(self.username)
        else:            
            self.balance=self.balance-amount
            print("Amount remaining is ",self.balance)
user1 = Chaitya("chaitya",2000)
user1.showBalance()
user1.setusername('Shyamal')
user1.transfer(1500,"Shyamal")
# user2 = Chaitya("Shyamal",1000)
# user2.trans+