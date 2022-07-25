from flask import Flask, redirect, url_for, render_template, request, flash



app = Flask(__name__)


app.config['SECRET_KEY'] = 'a1ba82a9c0673d28b00c9520f4963a95'


@app.route("/", methods = ["POST", "GET"])
def home():
	
	if request.method == "POST":

		row1 = request.form.get("row1")
		col1 = request.form.get("col1")
		row2 = request.form.get("row2")
		col2 = request.form.get("col2")

		if row1 == col1:

			return redirect(url_for("multiplication", r1 = row1, c1 = col1, r2 = row2, c2 = col2))


		else:
			flash(f'asda', 'error')
			return render_template('home.html')


	return render_template('home.html')

@app.route("/multiplication/<r1>/<c1>/<r2>/<c2>/")
def multiplication(r1, c1, r2, c2):
	return render_template("multiplication.html", r1 = r1, c1 = c1, r2 = r2, c2 = c2)

@app.route("/results/<t1>/<t2>")
def results(t1, t2):
	return render_template("results.html", x = t1, y = t2)

if __name__ == "__main__":
	app.run(debug=True)

