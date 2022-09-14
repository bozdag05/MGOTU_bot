from aiogram.types import Message, CallbackQuery

from loader import dp


@dp.message_handler(commands=['test'])
async def test_bot(message: Message):
    await message.answer('Bot_test_OK')


@dp.callback_query_handler(text='mgotu')
async def mgotu(call: CallbackQuery):
    await call.message.answer('MGOTU')


@dp.callback_query_handler(text='kkmt')
async def kkmt(call: CallbackQuery):
    await call.message.answer('KKMT')