# Declare a class Person having name as member. Derive two classes
# a. Businessman - having income and number of people involved in his
# business as members.
# b. Employee - having income as a member.
# c. Create objects of both the classes and compare the income and print the name of 
# one having greater income.
from socket import getnameinfo


class person:
    name=""
    def setname(self,name):
        self.name=name
    def getname(self,name):
        return self.name
class businessman(person):
    income=0
    people=""
    def setincome(self,income):
        self.income=income
    def getincome(self,income):
        return self.income
    def setpeople(self,people):
        self.people=people
    def getpeople(self,people):
        return self.getpeople
    def __lt__(self,other):
        return self.income<other.income
class employee(person):
    income=0 
    def setincome(self,income):
        self.income=income
    def getincome(self,income):
        return self.income
b1=businessman()
b1.setincome(120000)
b2=businessman()
b2.setincome(155000) 
if b1<b2:
    print("B2 having Higher INCOME Than b1") 
else:
    print("B1 Having Higher Income Than b2")