import loader, utils
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
        await msg.reply_to_message.download('modules/')
        new_modules = loader.get_modules()[0]
        for module in new_modules:
            if module not in old_modules:
                await msg.edit(f'✅ Модуль {module} успешно загружен!')
                return
        await msg.edit(f'✅ Модуль успешно обновлен!')