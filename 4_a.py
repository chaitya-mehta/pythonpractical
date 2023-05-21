#l=[1,2,3,1,6,3]
l=[]
n=int (input("Enter The Number"))
for i in range(0,n):
    a=int(input("Enter The Number TO List"))
    l.append(a) ;
s=set(l)
print(list(s))
