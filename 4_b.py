#find frequency
l=[]
n= int(input("Enter The Number"))
cnt=0
for i in range(0,n):
    a=int(input("Enter onr by one element"))
    l.append(a)
b=int(input("Enter The Variabele which you have to findd from the list"))
for i in range(0,n):
    if(l[i]==b):
        cnt+=1
print("The Number Is found In the list is ",cnt)