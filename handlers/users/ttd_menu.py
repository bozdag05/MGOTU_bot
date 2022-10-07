from aiogram.types import CallbackQuery

from filters import IsPrivate
from utils.db_api.rooms_commands import select_rooms as build_rooms
from utils.db_api.docs_commands import select_docs as build_docs
from utils.db_api.contacts_commands import select_contacts as build_contacts

from loader import dp


@dp.callback_query_handler(text='ttd_adres')
async def ttd_adres(call: CallbackQuery):
    await call.message.answer('Адрес ТТД:\n'
                              'Стадионная ул., 1, Королёв')


@dp.callback_query_handler(text='ttd_location')
async def ttd_location(call: CallbackQuery):
    await call.message.answer('https://yandex.ru/maps/-/CCURFLaADD')


@dp.callback_query_handler(text='ttd_rooms')
async def ttd_rooms(call: CallbackQuery):

    rooms = await build_rooms('ТТД')
    if rooms != []:
        for room in rooms:
            await call.message.answer(f'Заведение: {room.build}\n'
                                 f'номер кабинета: {room.number}\n'
                                 f'название кабинета: {room.title}\n'
                                 f'Описание: {room.comment}\n'
                                 f'Номер: {room.nomer}')
    else:
        await call.message.answer(f'Пока в базе данных нет информаций')


@dp.callback_query_handler(text='ttd_docs')
async def ttd_docs(call: CallbackQuery):
    docs = await build_docs('ТТД')
    if docs != []:
        for doc in docs:
            await call.message.answer(f'Заведение: {doc.build}\n'
                                      f'документ: {doc.name_file}\n'
                                      f'ссылка: {doc.file_url}')
    else:
        await call.message.answer(f'Пока в базе данных нет информаций')


@dp.callback_query_handler(text='ttd_contacts')
async def ttd_contacts(call: CallbackQuery):
    contacts = await build_contacts('ТТД')
    if contacts != []:
        for contact in contacts:
            await call.message.answer(f'Заведение: {contact.build}\n'
                                      f'имя: {contact.name_men}\n'
                                      f'должность: {contact.position}\n'
                                      f'контакт: {contact.contact}')
    else:
        await call.message.answer(f'Пока в базе данных нет информаций')