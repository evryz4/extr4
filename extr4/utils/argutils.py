import loader

from pyrogram.client import Client
from pyrogram.types import Message
from pyrogram.handlers.edited_message_handler import EditedMessageHandler
from pyrogram.handlers.message_handler import MessageHandler
from pyrogram.filters import create, me, chat

def is_args(msg: Message, minq: int = 1):
    return len(msg.text.split()) > minq

def argslist(msg: Message, fromi: int = 1):
    return msg.text.split()[fromi:]

def args(msg: Message, fromi: int = 1):
    return ' '.join(msg.text.split()[fromi:])

def message_id_filter(target_id: int):
    return create(lambda _, __, message: message.id == target_id)
                  
class Args:
    def __init__(self, client: Client, message: Message, *args: str, skipfirstarg: bool = False):
        self.args = args
        self.step = 0
        self.client = client
        self.message = message
        self.skipfirstarg = skipfirstarg
        self.fargs = []
    
    def after(self):
        def decorator(func):
            self.afterfunc = func
            return func
        return decorator
    
    async def handle(self):
        if self.step == 0 and not (self.skipfirstarg or not self.args):
                await self.message.edit(self.args[self.step])
        async def editor(client: Client, message: Message):
            self.step += 1
            self.fargs.append(message.text)
            if self.step >= len(self.args):
                await self.afterfunc(self.client, self.message, self.fargs)
                self.client.remove_handler(self.handler)
                return
            await message.edit(self.args[self.step])
        
        self.handler = EditedMessageHandler(editor, filters=message_id_filter(self.message.id))
        self.client.add_handler(self.handler)