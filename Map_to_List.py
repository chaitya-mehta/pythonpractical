# Consider a list of 1 to n (where n is user given number) and use map function to generate factorial of each numbers of list 
a=int(input("Enter The Number "))
def fact(n):
    if n>1:
        return n*fact (n-1)
    elif n==1:
        return 1
# print(fact(a))
num=range(1,a+1)
b=map(fact,num)
print(list(b))