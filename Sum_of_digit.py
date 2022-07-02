a=int(input("Enter The Number"))
sum=0
while(a>0):
    r=a%10
    sum=sum+r
    a=a//10
print("Sum Of Digit is", sum)