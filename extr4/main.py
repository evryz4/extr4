from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters

import loader, utils

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

app = Client(name=client_name, api_id=api_id, api_hash=api_hash, phone_number=phone_number)

@app.on_message(filters.me)
async def main(client: Client, msg: Message):
    modules = loader.get_modules()

    if msg.text[0] == prefix:
        cmd = ''.join(msg.text.split()[0][1:])
        for i in modules[1]:
            if cmd in modules[1][i]:
                try:
                    await modules[1][i][cmd](client, msg)
                except Exception as err:
                    await msg.edit(f'❌ Произошла ошибка:\n\n{err}')
    else:
        return

app.run()
