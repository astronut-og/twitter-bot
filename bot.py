import tweepy
import json
import requests
import discord
from discord import Webhook, RequestsWebhookAdapter, File
import SMS

with open('secret.json') as json_file:
    data = json.load(json_file)
    consumer_key = data['consumer_key']
    consumer_token = data['consumer_token']
    access_token = data['access_token']
    access_token_secret = data['access_token_secret']
    discord_webhook_1 = data['discord_webhook_1']
    discord_webhook_2 = data['discord_webhook_2']
    json_file.close()
# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_token)
auth.set_access_token(access_token, access_token_secret)
webhook = Webhook.partial(discord_webhook_1,discord_webhook_2,\
 adapter=RequestsWebhookAdapter())

# Create API object
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        webhook.send(status.text)
        SMS.send(status.text)
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
# edit with the twitter IDs as needed
myStream.filter(follow=["2381285430","897873334632841217"],is_async=True)