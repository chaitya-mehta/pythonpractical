def gcd(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    else:
        return gcd(b, a%b)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The gcd is ", gcd(a, b))