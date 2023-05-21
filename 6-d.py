# d) Create a base class A with 2 children B and C. class D having 2 parents B and C.
# Create a method named “Call” in every class. Use super in a way that a single call
# to method of class D execute “Call” method of every class.

class A:
    def call(self):
        print("Class A called..")

class B(A):
    def call(self):
        print("Class B called..")
        super().call()

class C(A):
    def call(self):
        print("Class C called..")
        super().call()

class D(B, C):
    def call( self) :
        print("Class D called..")
        super().call()

d = D()
d.call()