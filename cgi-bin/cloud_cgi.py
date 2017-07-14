#!/usr/bin/python
import cgi
print "content-type:text/html"
print "\r\n\r\n  "

d=cgi.FieldStorage()

user_name=d.getvalue('x')
user_password=d.getvalue('y')

if user_name=="cloud" and user_password=="redhat":
	print "<meta http-equiv='refresh' content='0;http://192.168.122.1/MainHtml/cloud/main_cloud.html'>"
else:
	print "User name or Password was incorrect <meta http-equiv='refresh' content='3;http://192.168.122.1/cloud.html'> "
