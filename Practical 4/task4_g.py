t = (1, 2, 23, 34, 91, 100)
n = int(input("Enter number you want to delete: "))
l = list(t)
if n in l:
    l.remove(23)
    print(tuple(l))
else:
    print("Value is not in list")
