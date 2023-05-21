# Insert data in student table.

import pymysql

mydb = pymysql.Connect(host='localhost', user='root', passwd='', database='abhi')
cursor = mydb.cursor()
cursor.execute('INSERT INTO STUDENT VALUES(1002, "ABHI", 9);')
cursor.close()
mydb.close()