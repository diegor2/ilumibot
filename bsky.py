import json

from atproto import Client

with open('secrets.json') as f:
    credentials = json.load(f)

user, password = credentials.values() 

client = Client()
client.login(user, password)
post = client.send_post('Hello world! I posted this via the Python SDK.')
