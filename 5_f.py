student={'chaitya':{'semester':4 ,'age':19 ,'cpi':8.02},
         'abhi':{'semester':4 ,'age':19 ,'cpi':8.8},
         'smit':{'semester':4 ,'age':19 ,'cpi':8.0}
         }
print('students',student)
print('Students Name',list(student.keys()))
max=0
a=''
for i in student:
    for j in student[i]:
        if j=='cpi':
            if(student[i][j]>max):
                max=student[i][j]
                a=i
print(max)
print(a)