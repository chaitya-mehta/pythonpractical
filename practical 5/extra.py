d = {}
dm = {}
l1 = []
l3 = ["semester", "age", "cpi"]
l2 = []
n = int(input("Enter the length: "))
for i in range(0, n):
    l1 = []
    l2 = []
    a = input("Enter the name: ")
    l1.append(a)
    b = input("Enter the semester: ")
    l2.append(b)
    b = input("age: ")
    l2.append(b)
    b = input("cpi: ")
    l2.append(b)
    print(l2)
    if d == {}:
        d = dict(zip(l3, l2))
    else:
        d.update(dict(zip(l3,l2)))
    print(list(d.items()))
    if dm == {}:
        dm = dict(zip(l1, list(d)))
    else:
        dm.update(dict(zip(l1, list(d.items()))))
print(dm)
        
        
