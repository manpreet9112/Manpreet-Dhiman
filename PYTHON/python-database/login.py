#!/usr/bin/python
import cgi

print "Content-type:text/html\r\n\r\n"
print "<h1>welcome for login</h1>"

form= cgi.FieldStorage()
name_= form.getvalue("uname")
fname_= form.getvalue("fname")

month_=form.getvalue("month")




"""print "<html>"
print "<head><title>login form</title>"
print "<body>"
print '<form name="form" method="get" action="/cgi-bin/login.py">'
print '<input type="text" name="uname" size="20"/>'
print '<input type="submit" name="btn" value="submit"/>'
print '</form>'
print "<h2>hello!" +name_+ "</h2>"
print "</body>"
print "</html>" """ 

print "<html>"
print "<head><title>login form</title></head>"
print "<body>"
print '<form name="form" method="get" action="/cgi-bin/login.py">'
print 'Name:<input type="text" size="18" name="uname" /><br/>'
print 'Father name: <input type="text" size="18" name="fname"/><br/>'

print 'D.O.B:<select name="day">'
print '<option value="1">1</option>'
print '<option value="2">2</option>'
print '<option value="3">3</option>'
print '</select>'
print '<select month="month">'
print '<option value="jan">january</option>'
print '<option value ="feb">feburary</option>'
print '<option value ="march">march</option>'
print '</select>'
print '<select year="year">'
print '<option value="1991">1991</option>'
print '<option value ="1992">1992</option>'
print '<option value ="1993">1993</option>'
print '</select><br/>'
print 'photo<input type="file" name="photoname"><br/>'
print '<input type="submit" value="upload"/><br/>' 
print '<input type="submit" name="btn" value="submit"/>'
print '</form>'

print "<h2>hello !" +name_+ "</h2>" 
print "<h2>hlo " +fname_+ "</h2>"  

print "<h2>month" +month_+ "</h2>"

print "</body>"
print "</html>"

