from filters import IsPrivate
from loader import dp
from aiogram.types import CallbackQuery


@dp.callback_query_handler(text='c1_adres')
async def c1_adres(call: CallbackQuery):
    await call.message.answer('Адрес Корпуса №1:\n'
                              'ул. Гагарина, 42, Королёв')


@dp.callback_query_handler(text='c2_adres')
async def c1_adres(call: CallbackQuery):
    await call.message.answer('Адрес Корпуса №2:\n'
                              'Октябрьская ул., 10А, Королёв')


@dp.callback_query_handler(text='c3_adres')
async def c1_adres(call: CallbackQuery):
    await call.message.answer('Адрес Корпуса №3:\n'
                              'Пионерская ул., 19А, Королёв')
