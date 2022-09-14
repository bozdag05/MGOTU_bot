from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from filters import IsPrivate
from states.state_of_rooms import state_room_add, state_room_drop
from utils.db_api import rooms_commands as commands
from data.config import GENERAL_ID as ID

from loader import dp


@dp.message_handler(IsPrivate(), Command('del_room'))
async def del_room(message: Message):
    if message.from_user.id == ID:
        await message.answer(f'Введите номер кобинтеа который вы хотите удалить:')
        await state_room_drop.drop_room.set()
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')


@dp.message_handler(state=state_room_drop.drop_room)
async def del_room(message: Message, state: FSMContext):
    answer = message.text

    room = await commands.select_room(answer)
    if room == None:
        await message.answer(f'комнаты {answer} нету в базе данных')
    else:
        await state.update_data(drop_room=answer)
        data = await state.get_data()
        number = data.get('drop_room')
        await commands.delete_room(number)
        await message.answer(f'Запись успешно удалена')

    await state.finish()


@dp.message_handler(IsPrivate(), Command('add_room'))
async def add_room(message: Message):
    if message.from_user.id == ID:
        await message.answer(f'Введите номер кобинтеа который вы хотите добавить:')
        await state_room_add.add_number.set()
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')


@dp.message_handler(state=state_room_add.add_number)
async def add_1(message: Message, state: FSMContext):
    answer = message.text
    try:
        room = await commands.select_room(answer)
        if room.number == answer:
            await message.answer(f'Такой кабинет уже существует\n'
                                 f'вот информация по этому кабинету')

            room = await commands.select_room(message.text)
            await message.answer(f'Заведение: {room.build}\n'
                                 f'номер кабинета: {room.number}\n'
                                 f'название кабинета: {room.title}\n'
                                 f'Номер: {room.nomer}')

    except Exception:
        await state.update_data(add_number=answer)
        await message.answer(f'Введите заведение:')
        await state_room_add.add_build.set()


@dp.message_handler(state=state_room_add.add_build)
async def add_2(message: Message, state: FSMContext):
    answer = message.text
    if len(answer) <= 4:
        answer.upper()
    else:
        answer.title()

    await state.update_data(add_build=answer)
    await message.answer(f'Введите название кабинета:')
    await state_room_add.add_title.set()


@dp.message_handler(state=state_room_add.add_title)
async def add_3(message: Message, state: FSMContext):
    answer = message.text

    await state.update_data(add_title=answer)
    await message.answer(f'Введите описание')
    await state_room_add.add_comment.set()


@dp.message_handler(state=state_room_add.add_comment)
async def add_4(message: Message, state: FSMContext):
    answer = message.text

    await state.update_data(add_comment=answer)
    await message.answer(f'Введите телефонный номер:')
    await state_room_add.add_nomer.set()


@dp.message_handler(state=state_room_add.add_nomer)
async def add_5(message: Message, state: FSMContext):
    answer = message.text

    await state.update_data(add_nomer=answer)
    data = await state.get_data()
    number, build, title, comment, nomer = data.get('add_number'), data.get('add_build'), \
                                           data.get('add_title'), data.get('add_comment'), data.get('add_nomer')

    await commands.add_room(number=number,
                            build=build,
                            title=title,
                            comment=comment,
                            nomer=int(nomer))

    await message.answer(f' Вы успешно добавили кабинет\n'
                         f'Проверте правильно ли вы вели информацию:')

    room = await commands.select_room(number)
    await message.answer(f'Заведение: {room.build}\n'
                         f'номер кабинета: {room.number}\n'
                         f'название кабинета: {room.title}\n'
                         f'Описание: {room.comment}\n'
                         f'Номер: {room.nomer}')

    await state.finish()


@dp.message_handler(IsPrivate(), Command('all_rooms'))
async def get_all_rooms(message: Message):
    if message.from_user.id == ID:
        rooms = await commands.select_all_rooms()
        for room in rooms:
            await message.answer(f'Заведение: {room.build}\n\n'
                                 f'номер кабинета: {room.number}\n\n'
                                 f'название кабинета: {room.title}\n\n'
                                 f'Описание: {room.comment}\n\n'
                                 f'Номер: {room.nomer}')
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')
