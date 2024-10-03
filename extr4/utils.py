from bottypes import *

def is_args(msg: Message, minq: int = 1):
    return len(msg.text.split()) > minq

def argslist(msg: Message, fromi: int = 1):
    return msg.text.split()[fromi:]

def args(msg: Message, fromi: int = 1):
    return ' '.join(msg.text.split()[fromi:])