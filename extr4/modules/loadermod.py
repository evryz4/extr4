import loader, utils.utils as utils, utils.argutils as argutils
from bottypes import *

class Loader(loader.Module):
    '''Загрузчик модулей'''

    strings = loader.strings(
        name='Loader',
        version='1.0'
    )

    @loader.command('load')
    async def loadcmd(client: Client, msg: Message):
        '''[ответ на файл] - загрузить модуль из файла'''

        old_modules = loader.get_modules()[0]
        path = await msg.reply_to_message.download('modules/')
        modules = loader.get_modules()
        for module in modules[0]:
            if module not in old_modules:
                config = utils.Config()
                cfg = config.get()

                text = f'Модуль **{module}** ({modules[0][module].strings['version']}) успешно загружен! Измените сообщение чтобы просмотреть код.\n'
                text += f'__{modules[0][module].__doc__}__\n\n'
                for command in modules[1][module]:
                    text += f'`{cfg['prefix']}{command}` {modules[1][module][command].__doc__}\n'
                await msg.edit(text)
                return
            with open(path, encoding='utf-8') as f:
                if module in f.read():
                    await msg.edit(f'✅ Модуль {module} успешно обновлен! Измените сообщение чтобы просмотреть код.')
            
            args = argutils.Args(client, msg)
            await args.handle()

            @args.after()
            async def _(client: Client, msg: Message, fargs):
                with open(path, encoding='utf-8') as file:
                    await msg.edit(f'```python\n{file.read()}```')