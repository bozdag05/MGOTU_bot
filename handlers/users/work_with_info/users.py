from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from filters import IsPrivate
from utils.db_api import quick_commands as commands
from data.config import GENERAL_ID as ID
from loader import dp


@dp.message_handler(IsPrivate(), Command('get_users'))
async def get_users(message: Message):
    if message.from_user.id == ID:
        users = await commands.select_all_users()

        if users != None:
            for id, user in enumerate(users):
                await message.answer(f'Профиль №{id}\n\n'
                                     f'ID: {user.user_id}\n'
                                     f'имя: {user.first_name}\n'
                                     f'юзер: {user.username}\n'
                                     f'статус: {user.status}')
        else:
            await message.answer('В базе данных пока нет информаций')
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')


@dp.message_handler(IsPrivate(), Command('count_users'))
async def count_users(message: Message):
    if message.from_user.id == ID:
        users = await commands.count_users()
        await message.answer(text=f'Количество пользователей бота - {users}')
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')


@dp.message_handler(IsPrivate(), Command('get_user'))
async def get_users(message: Message):
    if message.from_user.id == ID:
        user = await commands.select_user(user_id=message.from_user.id)

        await message.answer(f'Профиль:\n\n'
                             f'ID: {user.user_id}\n'
                             f'имя: {user.first_name}\n'
                             f'юзер: {user.username}\n'
                             f'статус: {user.status}')
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')
