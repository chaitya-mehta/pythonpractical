l = []
n = int(input("Enter the length: "))
for i in range(0, n):
    a = int(input("Enter the number: "))
    l.append(a)
print("Max: ", max(l), ", Min: ", min(l))