import web
import index

render = web.template.render('templates/')

urls = (
  '/', 'index.index'
)

app = web.application(urls, globals(), autoreload=False)


if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()