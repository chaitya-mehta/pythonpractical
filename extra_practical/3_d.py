# Consider a list consisting the marks of Physics subject of 10 students. Use reduce function to calculate the average of marks from the list. 
from functools import reduce
list=[45,35,46,47,48,49,19,25,39,41]
sum=reduce(lambda x,y:x+y,list)
avg=sum/len(list)
print(avg)
print(sum)
