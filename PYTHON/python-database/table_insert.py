#!/usr/bin/python

import MySQLdb

print "Content-type:text/html\r\n\r"

# Open database connection
db = MySQLdb.connect("localhost","root","manpreet","mydatabase" )

# prepare a cursor object using cursor() method
cursor = db.cursor()


# Create table as per requirement
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

     
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
   
  
# disconnect from server
db.close()

print "hello"
