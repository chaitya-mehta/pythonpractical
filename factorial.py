a=int(input("Enter The Number"))
fact=1
while(a>0):
    fact=fact*a
    a-=1
print("Factorial is ",fact)
# Recursion method 
a=int(input("Enter The Number"))
def factorial_recursive(a):
    if a<=1:
        return 1 
    else:
        return a*factorial_recursive(a-1)
print("The Factorial Of Given Number is",factorial_recursive(a))