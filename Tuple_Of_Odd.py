# Write a program to create a tuple of all odd numbers from 10 to 20.
t=(10,11,12,13,14,15,16,17,18,19,20)
l=list(t)
for i in l:
    if(i%2==0):
        l.remove(i)
print(tuple(l))