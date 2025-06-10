import json
from pyrogram.filters import create

from bottypes import *

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