student = {"Abhi" : {"semester": 5, "age": 20, "cpi":8.65},
           "Dhaval": {"semester": 3, "age": 19, "cpi": 8.32},
           "Jyot": {"semester": 6, "age": 21, "cpi": 9.23}
           }
print("Student detail: ", student)
print("Name of the students: ", list(student.keys()))
max = 0
for n in student:
    if student[n]["cpi"] > max :
        max = student[n]["cpi"]
        key = n
    else:
        continue
print(key, " : ", max)
