# Write a Python program to convert a list of tuples into a dictionary
t=('a','b','c','d')
l=list(t)
l1=[1,2,3,4]
d=dict(zip(l,l1))
print(d)