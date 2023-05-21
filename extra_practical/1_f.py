# Write a Program to calculate the sum and average of the digits present in a string.
a=input("Enter The String")
d=0
c=0
for i in a:
    if(i.isdigit()==True):
        z=int(i)
        d=d+z
        c=c+1
print(d/c)