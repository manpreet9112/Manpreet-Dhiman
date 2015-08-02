#!/usr/bin/python
import cgi

print "Content-type:text/html\r\n\r\n"



form= cgi.FieldStorage()
name_= form.getvalue("name")




print "<html>"
print "<head><title>user login form</title></head>"
print "<body>"
print "<h2>User login form</h2>"
print '<form name="form" method="get" action="/cgi-bin/form.py">'
print 'User Name<input type="text" size="18" name="name"/><br/>'
print 'password<input type="password" size="18" name="pwd"/><br/>'
print '<input type="submit" value="submit" name="btn"/>'
print '</form>'
print "<h2>Hello!!!" +name_+ "</h2>"
"""print "<h3> Hello dear! %s</h3>" %s (name_)"""      




print "</body>"
print "</html>"



"""// python statement print ("This is my login form")""" 

