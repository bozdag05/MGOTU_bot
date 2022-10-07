from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from filters import IsPrivate
from states.state_of_contacts import state_contact_add, state_contact_drop
from utils.db_api import quick_commands as users, contacts_commands as commands
from data.config import GENERAL_ID as ID, lis_build_1 as build_1, lis_build_2 as build_2
from loader import dp


@dp.message_handler(IsPrivate(), Command('del_contact'))
async def del_contact(message: Message):
    status = await users.select_user(message.from_user.id)
    if status == 'admin' or status == 'general_admin' or message.from_user.id == ID:
        await message.answer('Введите id номера который вы хотите удалить:')
        await state_contact_drop.drop_contact.set()
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')


@dp.message_handler(state=state_contact_drop.drop_contact)
async def del_1(message: Message, state: FSMContext):
    answer = message.text
    contact = await commands.select_contact_id(int(answer))

    if contact == None:
        await message.answer(f'В базе данных нет контакта с id - "{answer}"')
    else:
        await state.update_data(drop_contact=answer)
        data = await state.get_data()
        contact_id = data.get('drop_contact')
        await commands.delete_contact(int(contact_id))
        await message.answer('Запись успешно удалена')

    await state.finish()


@dp.message_handler(IsPrivate(), Command('add_contact'))
async def add_contact(message: Message):
    status = await users.select_user(message.from_user.id)
    if status == 'admin' or status == 'general_admin' or message.from_user.id == ID:
        await message.answer('Введите контакт который вы хотите добавить')
        await state_contact_add.add_contact.set()

    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')


@dp.message_handler(state=state_contact_add.add_contact)
async def add_1(message: Message, state: FSMContext):
    answer = message.text
    await state.update_data(add_contact=answer)
    await message.answer('введите заведение:')
    await state_contact_add.add_build.set()


@dp.message_handler(state=state_contact_add.add_build)
async def add_2(message: Message, state: FSMContext):
    inp = message.text
    if inp.upper() in build_1:
        answer = inp.upper()
        await state.update_data(add_build=answer)
        await message.answer('введите имя:')
        await state_contact_add.add_name_men.set()

    elif inp.title() in build_2:
        answer = inp.title()
        await state.update_data(add_build=answer)
        await message.answer('Введите имя:')
        await state_contact_add.add_name_men.set()
    else:
        await message.answer("Такого заведения не существует, ну или вы сделали ошибку вводе\n"
                             "введите одно из заведений - ККМТ, ТТД, МГОТУ, Общежитие №1, Общежитие №2\n"
                             "вызевите заново команду /add_contact")
        await state.finish()


@dp.message_handler(state=state_contact_add.add_name_men)
async def add_3(message: Message, state: FSMContext):
    answer = message.text

    await state.update_data(add_name_men=answer.title())
    await message.answer('Введите должность:')
    await state_contact_add.add_position.set()


@dp.message_handler(state=state_contact_add.add_position)
async def add_3(message: Message, state: FSMContext):
    answer = message.text
    lens = await commands.select_all_contacts()

    lis = []
    if lens == []:
        lis.append(0)

    for arg in lens:
        lis.append(arg.contact_id)

    lis.sort()
    id = lis[-1] + 1

    await state.update_data(add_position=answer.title())
    data = await state.get_data()
    build, name_men, position, contact = data.get('add_build'), data.get('add_name_men'), \
                                         data.get('add_position'), data.get('add_contact')
    await commands.add_contact(contact_id=id,
                               build=build,
                               name_men=name_men,
                               position=position,
                               contact=contact)
    await message.answer(f'контакт {contact} успешно добавлен\n'
                         f'вот информация по контакту:')

    contact = await commands.select_contact_id(id)
    await message.answer(f'ID: {contact.contact_id}\n\n'
                         f'Заведение: {contact.build}\n'
                         f'Имя: {contact.name_men}\n'
                         f'Должность: {contact.position}\n'
                         f'Контакт: {contact.contact}')

    await state.finish()


@dp.message_handler(IsPrivate(), Command('all_contacts'))
async def all_contacts(message: Message):
    status = await users.select_user(message.from_user.id)
    if status.status == 'admin' or status.status == 'general_admin' or message.from_user.id == ID:
        contacts = await commands.select_all_contacts()

        if contacts == []:
            await message.answer('База данных пуста')
        for contact in contacts:
            await message.answer(f'ID: {contact.contact_id}\n\n'
                                 f'Заведение: {contact.build}\n'
                                 f'Имя: {contact.name_men}\n'
                                 f'Должность: {contact.position}\n'
                                 f'Контакт: {contact.contact}')
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')
