import logging

from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters

from pyrogram.handlers import MessageHandler

import loader, utils.utils as utils

config = utils.Config()
cfg = config.get()

if not cfg["configured"]:
    print('Run setup.py first!')
    exit()

client_name = cfg['client_name']
api_id = cfg['api_id']
api_hash = cfg['api_hash']
phone_number = cfg['phone_number']
prefix = cfg['prefix']

modules = loader.get_modules()

app = Client(name=client_name, api_id=api_id, api_hash=api_hash, phone_number=phone_number)

groups = {
    MessageHandler: 1
}

async def on_command(client: Client, msg: Message):
    if msg.text[0] == prefix:
        modules = loader.get_modules()
        cmd = ''.join(msg.text.split()[0][1:])
        for i in modules[1]:
            if cmd in modules[1][i]:
                try:
                    await modules[1][i][cmd](client, msg)
                except Exception as err:
                    await msg.edit(f'❌ Произошла ошибка:\n\n{err}')
    else:
        return

app.add_handler(MessageHandler(callback=on_command, filters=filters.me and filters.text))

for module in modules[2]:
    for event in modules[2][module]:
        for method in modules[2][module][event]:
            if event in groups:
                groups[event] += 1
            else:
                groups[event] = 1

            app.add_handler(event(method, filters=method.filter), group=groups[event])

print('Бот запущен!')
app.run()
