# Entrance for web browse
#
# @auther jason.zhou
import web
from boot import render
#from db import mysqlcli


class index:
    def GET(self): 
		
		return render.index()