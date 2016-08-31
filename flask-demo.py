# Some cute flask app.
import requests
from requests.auth import HTTPBasicAuth
from twilio.rest import TwilioRestClient
from flask import Flask, render_template, request
from configobj import ConfigObj

app = Flask(__name__)
config = ConfigObj('config.ini')

TWILIO_SID = config['sid']
TWILIO_TOKEN = config['token']
TWILIO_NUMBER = config['number']

@app.route('/')
@app.route('/<name>')
def home(name=None):
    return render_template('home.html',name=name)
	
@app.route('/message', methods=['GET','POST'])
def message():
    if request.method == 'GET':
        return render_template('message.html', success=None)
    else:
        number = request.form['phoneNumber']
        message = request.form['message']

        client = TwilioRestClient(TWILIO_SID, TWILIO_TOKEN)

        message = client.messages.create(body=message,
            to="+1" + number,    # Replace with your phone number
            from_= TWILIO_NUMBER) # Replace with your Twilio number        
        return render_template('message.html', success="You sent a bloody message")

@app.route('/message/api', methods=['GET','POST'])
def message_api():
    if request.method == 'GET':
        return render_template('message.html', success=None)
    else:
        number = request.form['phoneNumber']
        message = request.form['message']
        account_sid = config['sid'] # Your Account SID from www.twilio.com/console
        auth_token  = config['token']  # Your Auth Token from www.twilio.com/console
        load = {'From':TWILIO_NUMBER, 'To':'+18722256140', 'Body': message}
        r = requests.post('https://api.twilio.com/2010-04-01/Accounts/' + TWILIO_SID + '/Messages', 
            data = load, auth=HTTPBasicAuth(TWILIO_SID,TWILIO_TOKEN))
        if r.status_code == 201:
            return render_template('message.html', success="You sent a bloody message")
        else:
            return "Failed"

if __name__ == '__main__':
    app.run()
