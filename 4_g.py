#remove from tuple
from typing import Tuple


t=(10,54,84,4,5,2,3,9)
a=int(input("Enter The  Numver which you have to delete from tuple"))
l=list(t)
l.remove(a)
print(tuple(l))
