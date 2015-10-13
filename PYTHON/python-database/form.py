#!/usr/bin/python
import cgi
import cgitb	
import MySQLdb
print "Content-type:text/html\r\n\r\n"

db=MySQLdb.connect("localhost", "root", "manpreet", "mydatabase")

form= cgi.FieldStorage()
cgitb.enable()

print "<html>"
print "<head><title>user login form</title></head>"
print "<body>"
print "<center>"
print "<h2>User login form</h2>"
print '<form name="form" method="post" action="/cgi-bin/form.py">'
print 'First Name:<input type="text" size="18" name="fname"/><br/>'
print 'Last Name<input type="text" size="18" name="lname"/><br/>'
print 'Age<input type="text" size="18" name="age"/><br/>'
print 'Gender<input type="text" size="18" name="gender"/><br/>'
print 'Income<input type="text" size="18" name="income"/><br/>'
print '<input type="submit" value="submit" name="btn"/>'
print '</form>'
print "</center>"
print "</body>"
print "</html>"

fname= form.getvalue('fname')
lname=form.getvalue('lname')
age=form.getvalue('age')
gender=form.getvalue('gender')
income=form.getvalue('income')

print "<h2>Hello!!!</h2>"
print "<h2>Your name  is:"+fname+ "</h2>"
print "<h2>Your lastname  is:"+lname+"</h2>"
print "<h2>Your age is:"+age+"</h2>"
print "<h2>Your gender is:"+gender+"</h2>"
print "<h2>Your income  is:"+income+"</h2>"


cursor=db.cursor()
sql ="INSERT INTO new(FN, LN, AGE, INCOME,GENDER) VALUES (%s, %s, %s, %s, %s)" 

cursor.execute(sql,(fname,lname,age,income,gender))

#cur.execute("SELECT VERSION()")
#data=cur.fetchone()
#print "database version is:%s" % data

db.commit()
db.close()
