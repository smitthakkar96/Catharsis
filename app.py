from flask import Flask, request, redirect, jsonify, render_template
from twilio.twiml.voice_response import VoiceResponse, Dial
from twilio.rest import Client

account = 'AC5a8cd025e6a9a49c91a60d8b57fded16'
token = '409ee4348b706cfd238cdafc423943ae'


app = Flask(__name__)
client = Client(account, token)


available_numbers = [
    '917892443270',
    '919904511373',
]


@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
    """Handle key press from a user."""
    resp = VoiceResponse()
    # Dial (310) 555-1212 - connect that number to the incoming caller.
    resp.dial(available_numbers[-1])
    # If the dial fails:
    resp.say("The call failed, or the remote party hung up. Goodbye.")

    return str(resp)


@app.route('/connect-call', methods=['POST'])
def connect_call():
    phone_number = request.form.get('phone_number')
    client.calls.create(to='91'+phone_number, from_=available_numbers[-1],
                       url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
    client.calls.create(to=available_numbers[-2], from_=available_numbers[-2],
                       url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

    return jsonify({"response": "success"})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
