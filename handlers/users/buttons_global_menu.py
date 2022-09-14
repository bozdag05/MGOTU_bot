from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from filters import IsPrivate
from keyboards.default.global_menu import global_menu
from keyboards.inline.info_establishment import *
from utils.db_api.rooms_commands import select_all_rooms as all_rooms
from utils.db_api.contacts_commands import select_all_contacts as all_contacts

from loader import dp


@dp.message_handler(IsPrivate(), commands=['menu'])
async def close_global_menu(message: Message):
    await message.answer('Выберите заведение о которй хотите получить информацию',
                         reply_markup=global_menu)


@dp.message_handler(IsPrivate(), text=['Университет', 'университет'])
async def close_global_menu(message: Message):
    await message.answer(f'<b>{message.text.upper()}</b>',
                        parse_mode='HTML',
                        reply_markup=ikb_mgotu)


@dp.message_handler(IsPrivate(), text=['ККМТ', 'ккмт'])
async def close_global_menu(message: Message):
    await message.answer(f'<b>{message.text.upper()}</b>',
                        parse_mode='HTML',
                        reply_markup=ikb_kkmt)


@dp.message_handler(IsPrivate(), text='ТТД')
async def close_global_menu(message: Message):
    await message.answer(f'<b>{message.text.upper()}</b>',
                        parse_mode='HTML',
                        reply_markup=ikb_ttd)


@dp.message_handler(IsPrivate(), text='общежитие №1')
async def close_global_menu(message: Message):
    text = 'времменно не функционирует'
    await message.answer(f'<b>{message.text.upper()} {text.upper()}</b>',
                        parse_mode='HTML')


@dp.message_handler(IsPrivate(), text='обшежитие №2')
async def close_global_menu(message: Message):
    await message.answer(f'<b>{message.text.upper()}</b>',
                        parse_mode='HTML',
                        reply_markup=ikb_dorm_2)


@dp.message_handler(IsPrivate(), text='Все особые кабинеты')
async def all_roomes(message: Message):


    try:
        rooms = await all_rooms()
        for room in rooms:
            await message.answer(f'Заведение: {room.build}\n'
                                f'номер кабинета: {room.number}\n'
                                f'название кабинета: {room.title}\n'
                                f'Описание: {room.comment}\n'
                                f'Номер: {room.nomer}')
    except Exception:
        await message.answer(f'Пока в базе данных нет информаций')


@dp.message_handler(IsPrivate(), text='Все контакты')
async def all_contacts(message: Message):
    try:
        contacts = await all_contacts()
        for contact in contacts:
            await message.answer(f'{contact.build}\n'
                                f'{contact.name_men}\n'
                                f'{contact.position}\n'
                                f'{contact.contact}\n')
    except Exception:
        await message.answer(f'Пока в базе данных нет ни каких контактов')


@dp.message_handler(IsPrivate(), text='закрыть')
async def close_global_menu(message: Message):
    await message.answer('Вы закрыли меню, чтобы открыть его снова нажмите /menu', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(IsPrivate(), text='назад')
async def close_global_menu(message: Message):
    await message.answer(f'Вы перешли на главное меню', reply_markup=global_menu)


@dp.callback_query_handler(text='close')
async def close_global_menu(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_remove)


@dp.callback_query_handler(text='end')
async def end_global_menu(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_mgotu)

