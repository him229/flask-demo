# Some cute flask app.
from twilio.rest import TwilioRestClient
from flask import Flask, render_template, request
from configobj import ConfigObj
app = Flask(__name__)
config = ConfigObj('config.ini')

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

        account_sid = config['sid'] # Your Account SID from www.twilio.com/console
        auth_token  = config['token']  # Your Auth Token from www.twilio.com/console

        client = TwilioRestClient(account_sid, auth_token)

        message = client.messages.create(body=message,
            to="+1" + number,    # Replace with your phone number
            from_="+17135978334") # Replace with your Twilio number        
        return render_template('message.html', success="You sent a bloody message")
if __name__ == '__main__':
    app.run()
