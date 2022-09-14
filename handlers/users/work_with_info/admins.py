from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from filters import IsPrivate
from utils.db_api import admins_commands as commands
from data.config import GENERAL_ID as ID
from states.state_of_admins import state_admin_drop, state__admin_add
from loader import dp, bot


@dp.message_handler(IsPrivate(), Command('add_general_admin'))
async def add_admin(message: Message):
    id = message.from_user.id
    username = message.from_user.username

    if id == ID and username == 'ottoman_02':
        admin = await commands.select_admin(id)
        if admin == None or admin.status != 'general_admin':
            await commands.add_admin(admin_id=message.from_user.id,
                                     first_name=message.from_user.first_name,
                                     last_name=message.from_user.last_name,
                                     username=message.from_user.username,
                                     status='general_admin')
            await message.answer('Super')
        else:
            await message.answer('Your in db')

    else:
        await message.answer('admin in db')


@dp.message_handler(IsPrivate(), Command('drop_general_admin'))
async def drop_general_admin(message: Message):
    id = message.from_user.id
    admin = await commands.select_admin(id)

    if admin != None and admin.admin_id == ID:
        await commands.delete_admin(id)
        await message.answer('Super')

    else:
        await message.answer('Admin not in db')


@dp.message_handler(IsPrivate(), Command('drop_admin'))
async def drop_admin(message: Message):
    admin = await commands.select_admin(message.from_user.id)

    if admin != None and admin.status == 'admin' or admin.status == 'general_admin':
        await message.answer('Введите ID админа которого хотите удалить')
        await state_admin_drop.drop_admin.set()
    else:
        await message.answer('You not admin')


@dp.message_handler(IsPrivate(), state=state_admin_drop.drop_admin)
async def drop_admin(message: Message, state: FSMContext):
    answer = int(message.text)

    admin = await commands.select_admin(answer)
    if admin != None and admin.admin_id != ID:
        await state.update_data(drop_admin=answer)
        data = await state.get_data()
        admin = data.get('drop_admin')
        await commands.delete_admin(admin)
        await message.answer('Запись успешно удалена')

    elif admin.admin_id == ID:
        await message.answer('Этого админа нельзя удалить :)')
        await bot.send_message(ID, f'Тебя пытается удалить админ {message.from_user.id}')
        admin = await commands.select_admin(admin_id=message.from_user.id)
        await bot.send_message(ID,
                               f'Профиль:\n\n'
                               f'ID: {admin.admin_id}\n'
                               f'имя: {admin.first_name}\n'
                               f'юзер: {admin.username}\n'
                               f'статус: {admin.status}')

    else:
        await message.answer('admin not in db')

    await state.finish()


@dp.message_handler(IsPrivate(), Command('add_admin'))
async def add_admin(message: Message):
    admin = await commands.select_admin(message.from_user.id)

    if admin != None and admin.status == 'admin' or admin.status == 'general_admin':
        await message.answer('Введите ID админа которог хотите добавить')
        await state__admin_add.add_admin.set()
    else:
        await message.answer('You not admin')


@dp.message_handler(IsPrivate(), state=state__admin_add.add_admin)
async def add_admin(message: Message, state: FSMContext):
    answer = message.text
    admin = await commands.select_admin(int(answer))
    admins = await commands.select_all_admins()
    lens = len(admins)

    if admin == None:
        await state.update_data(add_admin=answer)
        data = await state.get_data()
        admin = data.get('add_admin')
        await commands.add_admin(admin_id=int(admin),
                                 first_name=f'Admin {lens + 1}',
                                 last_name=f'Admin {lens + 1}',
                                 username=f'admin {lens + 1}',
                                 status='admin')

    else:
        await message.answer('admin in db')

    await state.finish()


@dp.message_handler(IsPrivate(), Command('update_status'))
async def update_status(message: Message):
    pass
