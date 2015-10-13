#!/usr/bin/python
import MySQLdb
import sys
print "content-type:text/html\r\n\r\n"
   
# Open database connection
db = MySQLdb.connect("localhost","root","manpreet","mydatabase")
  
# prepare a cursor object using cursor() method
cursor = db.cursor()
  
# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")
  
# Fetch a single row using fetchone() method.
data = cursor.fetchone()
  
print "Database Version : %s " % data
  
# disconnect from server
db.close()     
