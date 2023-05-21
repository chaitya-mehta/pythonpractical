class A:
    def call(self):
        print("Class A Calling")
class B(A):
    def call(self):
        print("Class B Calling")
        return super().call()
class C(A):
    def call(self):
        print("Class C Calling")
        return super().call()
class D(C,B):
    def call(self):
        print("Class D calling")
        return super().call()
d=D()
d.call()               