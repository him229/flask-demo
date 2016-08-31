# Some cute flask app.

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def home(name=None):
    return render_template('home.html',name=name)

	
@app.route('/message')
def message():
    return render_template('message.html')