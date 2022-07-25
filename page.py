from flask import Flask, redirect, url_for, render_template, request
#from calc import robotnik

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():
	if request.method == "POST":

		theta1 = request.form.get("theta1")
		theta2 = request.form.get("theta2")

		
		

		#result_list = robotnik.forwardKinematics(int(site_inputs[0]), int(site_inputs[0]))

		return redirect(url_for("results", t1 = theta1, t2 = theta2))

	else:	
		return render_template("home.html")

@app.route("/results/<t1>/<t2>")
def results(t1, t2):
	return render_template("results.html", x = t1, y = t2)

if __name__ == "__main__":
	app.run(debug=True)

