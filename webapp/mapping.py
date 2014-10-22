# Mapping for web browse path
#
# @auther jason.zhou
import web
from boot import *

urls = (
  '/error', 'mapping.errorpage',
  '/index', 'index.index',
  '/', 'index.index',
  '/cbforcsdn', 'cb4csdn.callback',
   '/getAccessCode', 'cb4csdn.getAccess',
  '/login','login.login'

  )

#errorpage
class errorpage:
    def GET(self):
        return render.errorpage()