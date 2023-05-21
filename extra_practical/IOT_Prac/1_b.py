import random
s=0
min=99999999999
max=-1
l=[]
i=int(input("Enter The Number "))
for j in range(0,i): 
    l.append(random.randint(0,51))
    s=s+l[j]
    if(l[j]<min):
        min=l[j]
    if(l[j]>max):
        max=l[j]
avg=s/i
print(l)
print(avg)
print(min)
print(max)