#!/usr/bin/python
import cgi
print "content-type:text/html"
print "\r\n\r\n  "

d=cgi.FieldStorage()

user_choice_of_service=d.getvalue('opt')


if user_choice_of_service == 'IAAS':
	print "<meta http-equiv='refresh' content='0;http://192.168.122.1/MainHtml/cloud/iaas.html'>"	
elif user_choice_of_service == 'PAAS':
	print "<meta http-equiv='refresh' content='0;http://192.168.122.1/MainHtml/cloud/paas.html'>"
elif user_choice_of_service == 'STAAS':
	print "<meta http-equiv='refresh' content='0;http://192.168.122.1/MainHtml/cloud/staas.html'>"
elif user_choice_of_service == 'SAAS':
	print "<meta http-equiv='refresh' content='0;http://192.168.122.1/MainHtml/cloud/saas.html'>"

