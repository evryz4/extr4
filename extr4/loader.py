import os
import json
import importlib.machinery

def strings(*, name: str = 'Module', version: str = '1.0'):
    return {
        'name': name,
        'version': version
    }

class Module:
    '''Sample class for module'''

    is_module = True
    strings = strings()

def command(name):
    '''Decorator for commands'''

    def decorator(func):
        async def wrapper(*args, **kwargs):
            ret = (await func(*args, **kwargs))
            return ret
        wrapper.__setattr__('is_command', True)
        wrapper.__setattr__('name', name)
        wrapper.__doc__ = func.__doc__
        return wrapper
    return decorator

def get_modules() -> tuple:
    '''Returns tuple (modules[name:class], commands[module:[name:command]]'''

    if os.path.dirname(__file__)[-7:] == 'modules':
        modulespath = os.path.dirname(__file__)
    else:
        modulespath = os.path.join(os.path.dirname(__file__), 'modules')

    modules = []
    for mod in os.listdir(modulespath):
        if mod[-3:] != '.py':
            continue

        name = os.path.basename(mod).rsplit(".py", maxsplit=1)[0]
        module = importlib.machinery.SourceFileLoader(name, os.path.join(modulespath, mod)).load_module()
        modules.append(module)

    cmodules = {}
    commands = {}
    for mod in modules:
        for attr in dir(mod):
            if isinstance(getattr(mod, attr), type) and hasattr(getattr(mod, attr), 'is_module'):
                cmodules[getattr(mod, attr).strings['name']] = getattr(mod, attr)
                commands[getattr(mod, attr).strings['name']] = {}
                for cattr in dir(getattr(mod, attr)):
                    if hasattr(getattr(getattr(mod, attr), cattr), 'is_command'):
                        commands[getattr(mod, attr).strings['name']][getattr(getattr(getattr(mod, attr), cattr), 'name')] = getattr(getattr(mod, attr), cattr)
    
    return (cmodules, commands)
