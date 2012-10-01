#######################################
######## week 4 thesis time ###########
########################################

import os, datetime

from flask import Flask, request # Retrieve Flask, our framework
from flask import render_template

app = Flask(__name__)   # create our flask app

# thesis type category
categories = {}
#Let's make a dictionary
categories["Performance"] = {
	"image": "performance.gif",
	"title": "Performance",
	"inStock": True
}

categories["Installation"] = {
	"image": "installation.gif", 
	"title": "Installation",
	"inStock": True
}

categories["Web"] = {
	"image": "web.gif",
	"title": "Web",
	"inStock": True
}

categories["Mobile app"] = {
	"image": "mobile.gif",
	"title": "Mobile app",
	"inStock": True
}

categories ["Extra"] = {
	"image": "extra.gif",
	"title": "Extra",
	"inStock": True
}

# this is our main page
@app.route("/")
def index():
	# render the template, pass in the category dictionary to it as "categories"
	return render_template("main.html", categories=categories)


# this is the 2nd route - can be access with /choose
@app.route("/choose", methods=["POST"])
def choose():

	# Get the user submitted data
	chooseData = {
		# key has an underline. value doesn't.
		"name": request.form.get("name"),
		"category_name": request.form.get("category"),
		"start_time": request.form.get("start")
	}
	
	# get the category data by category_name
	chooseData["category"] = categories[chooseData.get("category_name")]
	
	# determine starting date
	
	if chooseData["start_time"] != "dunno":
		now = datetime.datetime.now()
		
		if chooseData["start_time"] == "already":
			future = datetime.timedelta(days = 90) # I'll change it later
			
		elif chooseData["start_time"] == "now":
			future = datetime.timedelta(days = 90) # I'll change it later
			
		elif chooseData["start_time"] =="midterm":
			future = datetime.timedelta(days = 45) #I'll change it later
			
		elif chooseData["start_time"] == "final":
			future = datetime.timedelta(days = 15) # I'll change it later
			
		chooseData["thesis_time"] = now + future
			
		
	else:
		chooseData["thesis_time"] = None	
		
	
	return render_template("thesis_time.html", **chooseData)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)



	