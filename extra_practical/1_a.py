a=input("Enter The String")
d=dict()
for i in a:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)