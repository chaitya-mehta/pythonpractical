# Declare a class Person having name as member. Derive two classes
# a. Businessman - having income and number of people involved in his
# business as members.
# b. Employee - having income as a member.
# c. Create objects of both the classes and compare the income and print the name of
# one having greater income.

class Person:
    name = ""
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
class Businessman(Person):
    income = 0
    numOfPeople = 0
    def setIncome(self, income):
        self.income = income
    def getIncome(self):
        return self.income
    def __gt__(self, other):
        return self.income > other.income
class Employee(Person):
    income = 0
    def setIncome(self, income):
        self.income = income
    def getIncome(self):
        return self.income

b1 = Businessman()
b1.setIncome(120000)
e1 = Employee()
e1.setIncome(23000)
if b1>e1:
    print("The b1 has greater income")
else:
    print("The e1 has greater income.")