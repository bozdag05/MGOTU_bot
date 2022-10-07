from aiogram.types import CallbackQuery

from filters import IsPrivate
from loader import dp, bot
from keyboards.inline.info_corpuses import corpuses_adres, corpuses_location
from utils.db_api.rooms_commands import select_rooms as build_rooms
from utils.db_api.docs_commands import select_docs as build_docs
from utils.db_api.contacts_commands import select_contacts as build_contacts


@dp.callback_query_handler(text='mgotu_adreses')
async def mgotu_adres(call: CallbackQuery):
    await call.message.edit_reply_markup(corpuses_adres)


@dp.callback_query_handler(text='mgotu_locations')
async def mgotu_adres(call: CallbackQuery):
    await call.message.edit_reply_markup(corpuses_location)


@dp.callback_query_handler(text='mgotu_rooms')
async def mgotu_rooms(call: CallbackQuery):
    rooms = await build_rooms('МГОТУ')
    if rooms != []:
        for room in rooms:
            await call.message.answer(f'Заведение: {room.build}\n'
                                      f'номер кабинета: {room.number}\n'
                                      f'название кабинета: {room.title}\n'
                                      f'Описание: {room.comment}\n'
                                      f'Номер: {room.nomer}')
    else:
        await call.message.answer(f'Пока в базе данных нет информаций')


@dp.callback_query_handler(text='mgotu_docs')
async def mgotu_docs(call: CallbackQuery):
    docs = await build_docs('МГОТУ')
    if docs != []:
        for doc in docs:
            await call.message.answer(f'Заведение: {doc.build}\n'
                                      f'документ: {doc.name_file}\n'
                                      f'ссылка: {doc.file_url}')
    else:
        await call.message.answer(f'Пока в базе данных нет информаций')


@dp.callback_query_handler(text='mgotu_contacts')
async def mgotu_contcts(call: CallbackQuery):
    contacts = await build_contacts('МГОТУ')
    if contacts != []:
        for contact in contacts:
            await call.message.answer(f'Заведение: {contact.build}\n'
                                      f'имя: {contact.name_men}\n'
                                      f'должность: {contact.position}\n'
                                      f'контакт: {contact.contact}')
    else:
        await call.message.answer(f'Пока в базе данных нет информаций')
