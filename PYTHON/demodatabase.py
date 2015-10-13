#! /usr/lib/python
import MYSQLdb
import cgi

db= MYSQLdb.connect(host ="localhost" ,
                   user="root",
                  passwd="manpreet",
                  dbname="MYdatabase")

cur=db.cursor()

cur.execute("SELECT VERSION()")
vv=cur.fetchone()

#for row in cur.fetchall():
#       print row[0]
#db.close()"""

print "content-Type:text/html"
print "database version is: %s" %vv

db.close();
                                                              1,1           Top

