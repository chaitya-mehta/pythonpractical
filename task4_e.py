ans = [[1]]
n = int(input("Enter the length: "))
for i in range(0, n):
    t = [1]
    for j in range(0, i):
        t.append(ans[i][j] + ans[i][j+1])
    t.append(1)
    ans.append(t)
print(ans)