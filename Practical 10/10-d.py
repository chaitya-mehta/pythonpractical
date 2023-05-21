# Create a table Course with id, name and student id. Display the details of students who are registered for a specific course

import pymysql

mydb = pymysql.Connect(host='localhost', user='root', passwd='', database='abhi')
cursor = mydb.cursor()
# cursor.execute("CREATE TABLE COURSE(C_ID INT(10), NAME VARCHAR(30), ID INT(10));")
# cursor.execute('INSERT INTO COURSE VALUES(1, "PYTHON", 1002);')
cursor.execute('SELECT ID FROM COURSE WHERE NAME = "PYTHON";')
id = list(cursor.fetchall())
id = list(id.pop()).pop()
q = f'SELECT * FROM STUDENT WHERE ID ={id};'
cursor.execute(q)
detail = list(cursor.fetchall())
for d in detail:
    print(d)