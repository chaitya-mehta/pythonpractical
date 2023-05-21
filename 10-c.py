# Display the list of students having spi greater than 8

import pymysql

mydb = pymysql.Connect(host='localhost', user='root', passwd='', database='abhi')
cursor = mydb.cursor()
cursor.execute("SELECT NAME FROM STUDENT WHERE SPI > 8;")
result = cursor.fetchall()
for name in result:
    name = list(name)
    print(name.pop())