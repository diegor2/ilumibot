import json
import random

from atproto import Client

MAX_LENGHT = 300
ELLIPSIS = " (...)"

with open('database.json') as f:
    quotes = json.load(f)

author, quote = random.choice(quotes['database']).values()

footer = f'\n\n    -- {author}'
quote_lenght = MAX_LENGHT - len(footer)

if(len(quote) > quote_lenght):
    quote_lenght -= len(ELLIPSIS)
    quote = quote[:quote_lenght] + ELLIPSIS

message = f'{quote}{footer}'

with open('secrets.json') as f:
    credentials = json.load(f)

user, password = credentials.values() 

client = Client()
client.login(user, password)
post = client.send_post(message)
