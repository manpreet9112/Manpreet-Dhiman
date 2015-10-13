#!/usr/bin/python

import cgi
import MySQLdb
print "content-type:text/html\r\n\r"

db=MySQLdb.connect("localhost", "root", "manpreet", "mydatabase")
cursor=db.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql="""CREATE TABLE EMPLOYEE(
    FIRST_NAME CHAR(10) NOT NULL,
    LAST_NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT)"""


cursor.execute(sql)

db.close() 

print "table created"
