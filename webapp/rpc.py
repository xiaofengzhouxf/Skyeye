# Receive data and deal
#
# @auther jason.zhou
import web
from boot import *

class receive:
    def GET(self):
    	success = True
    	if success:
    		return render.success()
    	else:
    		errCode=1
    		errMsg="xx"
    		return render.fail(errCode,errMsg)
