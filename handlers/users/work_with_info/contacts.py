from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from filters import IsPrivate
from states.state_of_contacts import state_contact_add, state_contact_drop
from utils.db_api import contacts_commands as commands
from data.config import GENERAL_ID as ID
from loader import dp


@dp.message_handler(IsPrivate(), Command('del_contact'))
async def del_contact(message: Message):
    if message.from_user.id == ID:
        await message.answer('Введите номер который вы хотите удалить:')
        await state_contact_drop.drop_contact.set()
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')


@dp.message_handler(state=state_contact_drop.drop_contact)
async def del_1(message: Message, state: FSMContext):
    answer = message.text
    contact = await commands.select_contact(answer)

    if contact == None:
        await message.answer('В базе данных нет такого контакта')
    else:
        await state.update_data(drop_contact=answer)
        data = await state.get_data()
        contact = data.get('contact')
        await commands.del_contact(contact)
        await message.answer('Запись успешно удалена')

    await state.finish()


@dp.message_handler(IsPrivate(), Command('add_contact'))
async def add_contact(message: Message):
    if message.from_user.id == ID:
        await message.answer('Введите контакт который вы хотите добавить')
        await state_contact_add.add_contact.set()

    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')


@dp.message_handler(state=state_contact_add.add_contact)
async def add_1(message: Message, state: FSMContext):
    answer = message.text
    try:
        contact = await commands.select_contact(answer)
        if contact.contact == answer:
            await message.answer('Этот контакт уже есть в базе данных\n'
                                 'вот информация по этому контакту:')
            await message.answer(f'{contact.build}\n'
                                 f'{contact.name_men}\n'
                                 f'{contact.position}\n'
                                 f'{contact.contact}')

    except Exception:
        await state.update_data(add_contact=answer)
        await message.answer('введите заведение:')
        await state_contact_add.add_build.set()


@dp.message_handler(state=state_contact_add.add_build)
async def add_2(message: Message, state: FSMContext):
    answer = message.text
    if len(answer) <= 4:
        answer.upper()
    else:
        answer.title()

    await state.update_data(add_build=answer)
    await message.answer('введите имя:')
    await state_contact_add.add_name_men.set()


@dp.message_handler(state=state_contact_add.add_name_men)
async def add_3(message: Message, state: FSMContext):
    answer = message.text

    await state.update_data(add_name_men=answer)
    await message.answer('введите должность:')
    await state_contact_add.add_position.set()


@dp.message_handler(state=state_contact_add.add_position)
async def add_3(message: Message, state: FSMContext):
    answer = message.text

    await state.update_data(add_position=answer)
    data = await state.get_data()
    build, name_men, position, contact = data.get('add_build'), data.get('add_name_men'), \
                                         data.get('add_position'), data.get('add_contact')
    await commands.add_contact(build=build,
                               name_men=name_men,
                               position=position,
                               contact=contact)
    await message.answer(f'контакт {contact} успешно добавлен\n'
                         f'вот информация по контакту:')

    contact = await commands.select_contact(contact)
    await message.answer(f'Заведение: {contact.build}\n'
                         f'Имя: {contact.name_men}\n'
                         f'Должность: {contact.position}\n'
                         f'Контакт: {contact.contact}')

    await state.finish()


@dp.message_handler(IsPrivate(), Command('all_contacts'))
async def all_contacts(message: Message):
    if message.from_user.id == ID:
        contacts = await commands.select_all_contacts()
        for contact in contacts:
            await message.answer(f'Заведение: {contact.build}\n'
                                 f'Имя: {contact.name_men}\n'
                                 f'Должность: {contact.position}\n'
                                 f'Контакт: {contact.contact}')
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')
