# Entrance for web browse
#
# @auther jason.zhou
import web
from boot import render
#from db import mysqlcli


class login:
    def GET(self):
    	print 'login........'
    	##raise web.redirect('http://api.csdn.net/oauth2/authorize?client_id=YOUR_API_KEY&redirect_uri=http%3a%2f%2flocalhost%3a8080%2fcb4csdn&response_type=code')
    	raise web.seeother('http://api.csdn.net/oauth2/authorize?client_id=YOUR_API_KEY&redirect_uri=http%3a%2f%2flocalhost%3a8080%2fcb4csdn&response_type=code')



    