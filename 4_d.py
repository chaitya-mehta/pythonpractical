#Matrix Addition using list
m1=[[1,2,3],
    [4,5,6],
    [7,8,9]]
m2=[[1,2,3],
    [4,5,6],
    [7,8,9]]
r=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        r[i][j]=m1[i][j]+m2[i][j]
print(r)
#Matrix multiplicaton
mat=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m1)):
            mat[i][j]=m1[i][k]*m2[k][j]
            
print(mat)