import os
import importlib.machinery
import inspect

from pyrogram.handlers.message_handler import MessageHandler

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

def handler(event, filter=None):
    '''Decorator for handlers'''

    def decorator(func):
        async def wrapper(*args, **kwargs):
            ret = (await func(*args, **kwargs))
            return ret
        
        wrapper.__setattr__('is_handler', True)
        wrapper.__setattr__('event', event)
        wrapper.__setattr__('filter', filter)
        wrapper.__doc__ = func.__doc__
        return wrapper
    return decorator

def load_modules():
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
    
    return modules

def get_modules() -> tuple:
    '''Returns tuple (modules[name:class], commands[module:[name:command]])'''

    modules = load_modules()

    cmodules = {}
    commands = {}
    handlers = {}
    for mod in modules:
        for name, cls in inspect.getmembers(mod, inspect.isclass):
            if getattr(cls, 'is_module', False):
                module_name = cls.strings['name']
                cmodules[module_name] = cls
                commands[module_name] = {}
                handlers[module_name] = {}

                for func_name, method in inspect.getmembers(cls, inspect.isfunction):
                    if getattr(method, 'is_command', False):
                        command_name = method.name
                        commands[module_name][command_name] = method
                    
                    if getattr(method, 'is_handler', False):
                        event = method.event
                        handlers[module_name][event] = method
    
    return (cmodules, commands, handlers)

def handler_groups() -> dict:
    groups = {
        MessageHandler: 1
    }

    modules = get_modules()
    for module in modules[2]:
        for event in modules[2][module]:
            if event in groups:
                groups[event] += 1
            else:
                groups[event] = 1
    
    return groups