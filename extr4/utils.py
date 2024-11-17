import json

from bottypes import *

def is_args(msg: Message, minq: int = 1):
    return len(msg.text.split()) > minq

def argslist(msg: Message, fromi: int = 1):
    return msg.text.split()[fromi:]

def args(msg: Message, fromi: int = 1):
    return ' '.join(msg.text.split()[fromi:])

class Config:
    '''Class for working with config'''

    def __init__(self, configfile='config.json'):
        self.file = configfile
        with open(configfile) as file:
            self.config = json.loads(file.read())

    def _save(self):
        with open(self.file, 'w') as file:
            file.write(json.dumps(self.config, indent=4))
    
    def edit(self, **vars):
        for var in vars:
            self.config[var] = vars[var]
        self._save()
    
    def get(self):
        return self.config
