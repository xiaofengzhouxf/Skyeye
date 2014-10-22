from code import render

class index:
    def GET(self):
        name = "jason"
        age=30
        return render.index(name,age)