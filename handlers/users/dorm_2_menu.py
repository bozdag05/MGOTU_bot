from aiogram.types import CallbackQuery

from filters import IsPrivate
from utils.db_api.rooms_commands import select_rooms as build_rooms
from utils.db_api.docs_commands import select_docs as build_docs
from utils.db_api.contacts_commands import select_contacts as build_contacts

from loader import dp


@dp.callback_query_handler(text='dorm_2_adres')
async def dorm_2_adres(call: CallbackQuery):
    await call.message.answer('Общежитие МГОТУ №2:\n'
                              'Стадионная ул., 6, Королёв')


@dp.callback_query_handler(text='dorm_2_location')
async def dorm_2_location(call: CallbackQuery):
    await call.message.answer('https://yandex.ru/maps/-/CCURFLcGtD')


@dp.callback_query_handler(text='dorm_2_rooms')
async def dorm_2_rooms(call: CallbackQuery):
    rooms = await build_rooms('Общежитие №2')
    if rooms != []:
        for room in rooms:
            await call.message.answer(f'Заведение: {room.build}\n'
                                      f'номер кабинета: {room.number}\n'
                                      f'название кабинета: {room.title}\n'
                                      f'Описание: {room.comment}\n'
                                      f'Номер: {room.nomer}')
    else:
        await call.message.answer(f'Пока в базе данных нет информаций')


@dp.callback_query_handler(text='dorm_2_docs')
async def dorm_2_docs(call: CallbackQuery):
    docs = await build_docs('Общежитие №2')
    if docs != []:
        for doc in docs:
            await call.message.answer(f'{doc.build}\n'
                                 f'{doc.name_file}\n'
                                 f'{doc.file_url}')
    else:
        await call.message.answer(f'Пока в базе данных нет информаций')


@dp.callback_query_handler(text='dorm_2_contacts')
async def dorm_2_contacts(call: CallbackQuery):
    contacts = await build_contacts('Общежитие №2')
    if contacts != []:
        for contact in contacts:
            await call.message.answer(f'{contact.build}\n'
                                      f'{contact.name_men}\n'
                                      f'{contact.position}\n'
                                      f'{contact.contact}')
    else:
        await call.message.answer(f'Пока в базе данных нет информаций')