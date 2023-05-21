l=[]
n= int(input("Enter The Number"))
cnt=0
for i in range(0,n):
    a=int(input("Enter onr by one element"))
    l.append(a)
l.sort()
print(l)