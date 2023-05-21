sign = input("Enter the sign: ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second nunber: "))
if sign=="+":
    print(a, " + ", b, " = ", a+b)
elif sign=="-":
    print(a, " - ", b, " = ", a-b)
elif sign=="*":
    print(a, " * ", b, " = ", a*b)
elif sign=="/":
    print(a, " / ", b, " = ", a/b)
else:
    print("The sign is wrong")
