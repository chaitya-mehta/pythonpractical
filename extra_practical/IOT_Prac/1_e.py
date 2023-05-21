l=[1,2,54,1,118,5]

flag=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            flag=1
            
if(flag==1):
    print("Duplicate")
    
else:
    print("Unique")