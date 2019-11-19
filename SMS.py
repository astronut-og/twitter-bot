# import the Twilio client from the dependency
from twilio.rest import Client
import json


with open('secret.json') as json_file:
    data = json.load(json_file)
    account_sid = data["twilio_sid"]
    auth_token = data["twilio_token"]
    from_number = data["twilio_from"]
    to_number = data["twilio_to"]
    json_file.close()

client = Client(account_sid, auth_token)

def send(message,from_number,to_number):
    message = client.messages.create(
        from_ = from_number,
        body = message,
        to = to_number
    )