from flask import Flask, request
from twilio import twiml
from twilio.twiml.messaging_response import Message, MessagingResponse
from tinder_api_sms import *;
from features import *;
import pprint
import datetime
import string
import dialogflow
import os   
from google.api_core.exceptions import InvalidArgument
from twilio.rest import Client

account_sid = '#'
auth_token = '#'
client = Client(account_sid, auth_token)

app = Flask(__name__)


@app.route('/sms', methods=['POST'])

def sms():
    number = request.form['From']
    message_body = request.form['Body']
    send_msg(message_body, "my bad sorry, i can't hangout. i hope you have a terrific day tho <3");

    resp = MessagingResponse()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    return str(message_body)

if __name__ == '__main__':
    app.run()

