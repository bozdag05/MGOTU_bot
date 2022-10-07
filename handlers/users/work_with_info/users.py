from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from filters import IsPrivate
from states import state_update_status
from utils.db_api import quick_commands as commands
from data.config import GENERAL_ID as ID
from loader import dp, bot


@dp.message_handler(IsPrivate(), Command('get_users'))
async def get_users(message: Message):
    if message.from_user.id == ID:
        users = await commands.select_all_users()

        if users != None:
            for id, user in enumerate(users):
                await message.answer(f'Профиль №{id + 1}\n\n'
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

        user = await commands.select_user(user_id=message.from_user.id)

        await message.answer(f'ID: {user.user_id}\n'
                             f'имя: {user.first_name}\n'
                             f'юзер: {user.username}\n'
                             f'статус: {user.status}')


@dp.message_handler(IsPrivate(), Command('update_status'))
async def update_status(message: Message):
    answer = message.from_user.id

    admin = await commands.select_user(answer)
    if admin.status == 'admin' or admin.status == 'general_admin' or answer == ID:
        await message.answer('Введите id статус которого вы хотите изменть')
        await state_update_status.update_status.set()
    else:
        await message.answer('Your not admin')


@dp.message_handler(IsPrivate(), state=state_update_status.update_status)
async def update(message: Message, state: FSMContext):
    answer = int(message.text)

    if answer == ID and message.from_user.id == ID:
        await message.answer('Введите новый статус этому админу')
        await state.update_data(update_status=answer)
        await state_update_status.new_status.set()

    elif answer != ID:
        await message.answer('Введите новый статус этому админу')
        await state.update_data(update_status=answer)
        await state_update_status.new_status.set()

    elif answer == ID and message.from_user.id != ID:
        await message.answer('этому админу нельзя ничего сделать :)')
        await bot.send_message(ID, f'Тебе пытаются изменить статус, админ {message.from_user.id}')
        await state.finish()
    else:
        await message.answer('произошла ошибка')
        await state.finish()


@dp.message_handler(IsPrivate(), state=state_update_status.new_status)
async def new_status(message: Message, state: FSMContext):
    answer = message.text
    await state.update_data(new_status=answer)
    data = await state.get_data()
    new = data.get('new_status')
    id = data.get('update_status')
    await commands.update_status(user_id=int(id), new_status=new)
    await message.answer("Статус успешно обнавлён")
    user = await commands.select_user(id)
    await message.answer(f'Профиль:\n\n'
                         f'ID: {user.user_id}\n'
                         f'имя: {user.first_name}\n'
                         f'юзер: {user.username}\n'
                         f'статус: {user.status}')

    await state.finish()
