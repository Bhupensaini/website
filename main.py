from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/tabs')
def tabs():
	return render_template("tab.html")

@app.route('/evangalion')
def evangalion():
	return render_template("evangalion.html")

if __name__ == '__main__':
	app.debug = True
	app.run()