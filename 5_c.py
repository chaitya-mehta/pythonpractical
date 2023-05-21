#5_c: frequency of given string
s = input("Enter the string: ")
d = dict()
for i in s:
    if i in d.keys():
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)
