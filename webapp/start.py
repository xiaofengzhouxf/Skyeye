# start web app
#
# @auther jason.zhou
import web,os,sys

from mapping import urls


workpath=os.path.dirname(__file__)
sys.path.append(workpath)

app = web.application(urls, globals(), autoreload=False)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()