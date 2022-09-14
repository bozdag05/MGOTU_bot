from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from filters import IsPrivate

from utils.db_api import quick_commands as commands
from utils.users_commands import set_admins_commands
from data.config import admins

from loader import dp, bot


@dp.message_handler(IsPrivate(), Command('start'))
async def start(message: Message):
    text = f'Добропожаловать на бот поддержки МГОТУ им.А.А.Леонова\n\n' \
           f'Функций бота:\n' \
           f'-- Полученеие адрессов корпусов мготу\n' \
           f'-- Получение локаций нахождения корпусов в яндексе\n' \
           f'-- Получение контактов должнастных лиц мготу\n' \
           f'-- Получение расположение особых комнат и информаций о них\n' \
           f'-- Получение документов\n' \
           f'-- Получение всей перечисленной информаций по отдельно взятим заведениям\n' \
           f'(ТТД/ККМТ/МГОТУ)\n\n'\
           f'нажмите команду /menu чтобы начать работать с ботом'
    await message.answer(text=text)

    await commands.add_user(user_id=message.from_user.id,
                            first_name=message.from_user.first_name,
                            last_name=message.from_user.last_name,
                            username=message.from_user.username,
                            status='active')


@dp.message_handler(IsPrivate(), Command('get_admins_commands'))
async def get_commands(message: Message):
    id = message.from_user.id
    if id in admins:
        await set_admins_commands(dp, id)
        await message.answer('Вы получили доступ к командам\n'
                             'перезапустите бота')
    else:
        await message.answer('Вы не админ\n'
                             'вам эти команды не доступны')


@dp.message_handler(IsPrivate())
async def all_message(message: Message):
       await message.answer('Вы походу допустили какую-то ошибку\n'
                            'лучше обратитесь к меню чтобы не было проблем\n'
                            '- /menu')


@dp.message_handler()
async def all_message(message: Message):
       await bot.send_message(message.from_user.id, 'С ботом можно работать только приватно')
