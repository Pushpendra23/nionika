#!/usr/bin/python
import cgi,os
print "content-type:text/html"
print "\r\n\r\n  "

d=cgi.FieldStorage()

user_name=d.getvalue('x')
user_password=d.getvalue('y')

if user_name=="root" and user_password=="redhat":
	print "<meta http-equiv='refresh' content='0;http://192.168.122.1/MainHtml/bigdata/big_main.html'>"
else:
	print "User name or Password was incorrect <meta http-equiv='refresh' content='3;http://192.168.122.1/bigdata.html'> "

