# Write a Python Program to Find the Number Occurring Odd Number of Times using Lambda expression and reduce function
from functools import reduce
list=[1,2,3,4,5,6,7,8,91,1,54]
c=0
count=reduce(lambda x,y:c=c+1 if x%2==1 else 0,list)