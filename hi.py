from flask import Flask, render_template


#create a flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')

#def index():
#	return "<h2>Hello world!</h2>"

###FILTERS!!!!
#safe
#capitalize
#lower
#upper
#title
#trim
#striptags
#reverse

def index():
	first_name = "jon"
	stuff1 = "this is <strong>Bold</strong> Text"
	stuff2 = "This is bold text "

	fav_pizza = ["peporeni","mushroom",41]
	return render_template("index.html",first_name=first_name,
		stuff1=stuff1,
		stuff2=stuff2,
		fav_pizza=fav_pizza)




#localhost:5000/user/yahyaa
@app.route('/user/<name>')

def user(name):
	return render_template("user1.html",user_name=name)

#create custom error pages

#INvalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal server error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500