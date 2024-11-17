import loader, utils
from bottypes import *

standarttext = '\ud83c\udf83 extr4\\\ud83d\udc7e owner - [owner]\\\\\ud83d\udd22 version - [version]\\\u2328 prefix - [prefix]'

class StdMod(loader.Module):
    '''Стандартный модуль'''

    strings = loader.strings(
        name='StdModule',
        version='1.1'
    )

    @loader.command('info')
    async def infocmd(client: Client, msg: Message):
        '''- показывает информацию о юзерботе'''

        config = utils.Config()
        cfg = config.get()
        if not 'infotext' in cfg:
            config.edit(infotext=standarttext)
        text = cfg['infotext']

        text = text.replace('[owner]', f'{(await client.get_me()).username and '@'+(await client.get_me()).username or (await client.get_me()).id}')\
                   .replace('[version]', cfg['version'])\
                   .replace('[prefix]', cfg['prefix'])\
                   .replace('\\', '\n')
        await msg.edit_text(text)

    @loader.command('infotext')
    async def infotextcmd(client: Client, msg: Message):
        '''[текст] - изменяет текст команды info. Можно использовать [owner], [version], [prefix], \\ для пробела. Напишите standart для стандартного текста'''

        config = utils.Config()

        if utils.is_args(msg):
            if utils.argslist(msg)[0] == 'standart':
                config.edit(infotext=standarttext)
                await msg.edit_text(f'✅ Текст успешно изменен на стандартный!')
            else:
                config.edit(infotext=utils.args(msg))
                await msg.edit_text(f'✅ Текст успешно изменен!')
        else:
            await msg.edit_text(f'❌ Синтаксис команды: {config.get()['prefix']}infotext [текст]')

    @loader.command('help')
    async def helpcmd(client: Client, msg: Message):
        '''- показывает все модули (название модуля для получения информации о нем)'''

        modules = loader.get_modules()

        config = utils.Config()
        cfg = config.get()

        if utils.is_args(msg):
            hmodule = utils.args(msg)
            for i in modules[0]:
                if hmodule.lower() == i.lower():
                    hmodule = i
            if hmodule not in modules[0]:
                text = f'📃 {len(modules[0])} модулей:\n\n'
                for module in modules[0]:
                    text += f'`{module}` - __{modules[0][module].__doc__}__ ( {' | '.join(modules[1][module].keys())} )\n'
            else:
                text = f'**{hmodule}** ({modules[0][hmodule].strings['version']})\n'
                text += f'__{modules[0][hmodule].__doc__}__\n\n'
                for command in modules[1][hmodule]:
                    text += f'`{cfg['prefix']}{command}` {modules[1][hmodule][command].__doc__}\n'
        else:
            text = f'📃 {len(modules[0])} модулей:\n\n'
            for module in modules[0]:
                text += f'`{module}` - __{modules[0][module].__doc__}__ ( {' | '.join(modules[1][module].keys())} )\n'

        await msg.edit_text(text)
