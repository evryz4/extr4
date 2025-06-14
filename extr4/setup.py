import json
import os
import shutil

import asyncio

from pyrogram import Client
from pyrogram.errors import SessionPasswordNeeded

if not os.path.exists("config.json"):
    shutil.copy("config.example.json", "config.json")

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

app = Client(client_name, api_id=api_id, api_hash=api_hash)

async def login():
    await app.connect()

    sent_code = await app.send_code(phone_number)
    code = input('Enter the confirmation code: ')
    try:
        await app.sign_in(phone_number, sent_code.phone_code_hash, code)
    except SessionPasswordNeeded:
        password = input('Enter the 2FA password: ')
        await app.check_password(password)

asyncio.run(login())

os.system('python3 main.py')
exit()