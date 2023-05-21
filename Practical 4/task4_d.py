#matrix addition and muliplication
m1 = [[1,1,1], [2,1,2], [1,2,1]]
m2 = [[1,1,1], [2,1,2], [1,2,1]]
sum = [[0,0,0], [0,0,0], [0,0,0]]
mult = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(0, len(m1)):
    for j in range(0, len(m1[i])):
        sum[i][j] = m1[i][j] + m2[i][j]
print("The matrix sum: ")
print(sum)
for i in range(0, len(m1)):
    for j in range(0, len(m1[i])):
        for k in range(0, len(m1[1])):
            mult[i][j] = m1[i][k] * m2[k][j]
print("Multiplication of list: ")
print(mult)