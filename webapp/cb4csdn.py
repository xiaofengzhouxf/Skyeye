# Entrance for web browse
#
# @auther jason.zhou
import web
from boot import render
import urllib2
#from db import mysqlcli



#{
#    "access_token": "0dd49b2a5afa45bba6765ba4fdd1b3c9",
#    "expires_in": 86400,
#    "username": "zhuyi"
#}
class getAccess:
    def GET(self): 
		i = web.input()
		print 'input: ',i

class callback:
    def GET(self): 
		i = web.input()
		print 'callback input: ',i
		print urllib2.urlopen('http://api.csdn.net/oauth2/access_token?client_id=YOUR_API_KEY&client_secret=YOUR_API_SECRET&grant_type=authorization_code&redirect_uri=http%3a%2f%2flocalhost%3a8080%2fgetAccessCode&code=THE_CODE_FROM_ABOVE').read()