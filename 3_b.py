str=input("Enter The string ")
u=0
l=0
d=0
s=0
print("The Length Of String is ",len(str))
for i in range (len(str)):
    if(str[i]>='a' and str[i]<='z'):
        l=l+1
    elif(str[i]>='A' and str[i]<='Z'):
        u=u+1
    elif(str[i]==' '):
        s=s+1
    elif(str[i]>='0' and str[i]<='9'):
        d+=1
print("The Length Of String is and Calculate The Number Of digit is ",len(str))
print("Number Of Upper case Letter Is",u)
print("Number Of Lower case Letter Is",l)
print("Number Of space Is",s)
print("The NUmber Of Digit is ",d) 