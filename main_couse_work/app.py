from flask import Flask, render_template, request

from map_foursquare import point
#Flask
app = Flask(__name__, template_folder="template")
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def my_form_post():
	"""
	Return hml page
	"""
	return render_template('result.html')


@app.route('/map', methods=["POST"])
def my_form():
	"""
	Create forms in the web app
	Return the map, based on the information, written in forms
	"""
	text = request.form['text']
	place = request.form['place']
	point(text, place)
	return render_template('map.html')


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=80)
	"http://127.0.0.1:80"
