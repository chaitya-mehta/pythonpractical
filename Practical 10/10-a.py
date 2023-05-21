# Write a Python program to create a table named student with id, name and spi data.

import pymysql

mydb = pymysql.Connect(host='localhost', user='root', passwd='', database='abhi')
cursor = mydb.cursor()
cursor.execute('CREATE TABLE STUDENT(ID INT(10), NAME VARCHAR(30), SPI INT(3));')
mydb.close()