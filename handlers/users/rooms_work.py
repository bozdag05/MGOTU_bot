from aiogram.types import Message

from loader import dp

from utils.db_api import docs_commands as commands


@dp.message_handler(text='0000')
async def add_rooms(message: Message):

    try:
        room = await commands.select_room(message.text)
        if room.number == message.text:
            await message.answer(f'room {message.text} have')

    except Exception:
        await commands.add_room(build='ККМТ',
                                number=message.text,
                                title='Доп. обучение',
                                comment='Можно узнать и купить дополнительные курсы',
                                nomer=89322471784)

        room = await commands.select_room(message.text)
        await message.answer(f'Заведение: {room.build}\n'
                             f'номер кабинета: {room.number}\n'
                             f'название кабинета: {room.title}\n'
                             f'Номер: {room.nomer}')


