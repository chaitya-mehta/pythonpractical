# Write a Python program to find maximum of two user given numbers using lambda function
a=int(input("Enter The Number"))
b=int(input("Enter The Number"))
c=lambda a,b:a if a>b else b
print(c(a,b),"is a maximum number")