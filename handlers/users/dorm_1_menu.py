from aiogram.types import CallbackQuery

from filters import IsPrivate
from utils.db_api.rooms_commands import select_rooms as build_rooms

from loader import dp


@dp.callback_query_handler(IsPrivate(), text='dorm_1_adres')
async def dorm_1_adres(call: CallbackQuery):
    await call.message.answer('dorm_1_adres')


@dp.callback_query_handler(IsPrivate(), text='dorm_1_location')
async def dorm_1_location(call: CallbackQuery):
    await call.message.answer('https://yandex.ru/maps/-/CCURFLcGtD')


@dp.callback_query_handler(IsPrivate(), text='dorm_1_rooms')
async def dorm_1_rooms(call: CallbackQuery):

    rooms = await build_rooms('Общежитие №1')
    if rooms != []:
        for room in rooms:
            await call.message.answer(f'Заведение: {room.build}\n'
                                      f'номер кабинета: {room.number}\n'
                                      f'название кабинета: {room.title}\n'
                                      f'Описание: {room.comment}\n'
                                      f'Номер: {room.nomer}')
    else:
        await call.message.answer(f'Пока в базе данных нет информаций')


@dp.callback_query_handler(IsPrivate(), text='dorm_1_docs')
async def dorm_1_docs(call: CallbackQuery):
    await call.message.answer('dorm_1_docs')
