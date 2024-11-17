import json
import os

from pyrogram import Client


configfile = 'config.json'

custom = input('Custom api id and api hash (Y/n): ')
if custom.lower() == 'y':
    print('You can get your api id and hash at the https://my.telegram.org/')
    api_id = input('Enter your api id: ')
    api_hash = input('Enter your api hash: ')
else:
    api_id = '23634288'
    api_hash = '982c5f9989cbd719ad0b5b766f81d09e'
phone_number = input('Enter your phone number: ')
client_name = input('Enter the client name: ')

with open(configfile) as file:
    config = json.loads(file.read())

config['configured'] = True
config['api_id'] = api_id
config['api_hash'] = api_hash
config['phone_number'] = phone_number
config['client_name'] = client_name

with open(configfile, 'w') as file:
    file.write(json.dumps(config, indent=4))

os.system('start python main.py')
quit()
