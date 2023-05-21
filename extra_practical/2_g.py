#  Write a Python program to find the index of an item of a tuple
t=('a','b','c','d','e','f')
z=input("Enter The Element you Want To find In The tuple")
flag=0
for i in t:
    if i==z:
        flag=1
        print(i)
if flag==1:
    print(i)
else:
    print("Element Not Found")