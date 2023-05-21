l = []
length = int(input("Enter the length: "))
for i in range(0, length):
    a = int(input("Enter the number: "))
    l.append(a)
d = dict()
for n in l:
    if n in d.keys():
        d[n] = d[n] + 1
    else:
        d[n] = 1
print("The frequency of elements: ")
for n in d.keys():
    print(n, " : ", d[n])