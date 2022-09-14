from aiogram.types import CallbackQuery

from filters import IsPrivate
from loader import dp


@dp.callback_query_handler(text='c1_location')
async def c1_location(call: CallbackQuery):
    await call.message.answer('https://yandex.ru/maps/-/CCURJDAcgA')


@dp.callback_query_handler(text='c2_location')
async def c1_location(call: CallbackQuery):
    await call.message.answer('https://yandex.ru/maps/-/CCURJDUpCC')


@dp.callback_query_handler(text='c3_location')
async def c1_location(call: CallbackQuery):
    await call.message.answer('https://yandex.ru/maps/-/CCURJDey1B')
