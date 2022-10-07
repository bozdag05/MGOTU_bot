from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from filters import IsPrivate
from states.state_of_rooms import state_room_add, state_room_drop
from utils.db_api import rooms_commands as commands, quick_commands as users
from data.config import GENERAL_ID as ID, lis_build_2 as build_2, lis_build_1 as build_1

from loader import dp


@dp.message_handler(IsPrivate(), Command('del_room'))
async def del_room(message: Message):
    status = await users.select_user(message.from_user.id)
    if status == 'admin' or status == 'general_admin' or message.from_user.id == ID:
        await message.answer(f'Введите id кабинтеа который вы хотите удалить:')
        await state_room_drop.drop_room.set()
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')


@dp.message_handler(state=state_room_drop.drop_room)
async def del_room(message: Message, state: FSMContext):
    answer = message.text

    room = await commands.select_room_id(int(answer))
    if room == None:
        await message.answer(f'В базе данных нету комнаты с id - "{answer}"')
    else:
        await state.update_data(drop_room=answer)
        data = await state.get_data()
        number = data.get('drop_room')
        await commands.delete_room(int(number))
        await message.answer(f'Запись успешно удалена')

    await state.finish()


@dp.message_handler(IsPrivate(), Command('add_room'))
async def add_room(message: Message):
    status = await users.select_user(message.from_user.id)
    if status == 'admin' or status == 'general_admin' or message.from_user.id == ID:
        await message.answer(f'Введите номер кабинтеа который вы хотите добавить:')
        await state_room_add.add_number.set()
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')


@dp.message_handler(state=state_room_add.add_number)
async def add_1(message: Message, state: FSMContext):
    answer = message.text

    await state.update_data(add_number=answer)
    await message.answer(f'Введите заведение:')
    await state_room_add.add_build.set()


@dp.message_handler(state=state_room_add.add_build)
async def add_2(message: Message, state: FSMContext):
    inp = message.text
    if inp.upper() in build_1:
        answer = inp.upper()
        await state.update_data(add_build=answer)
        await message.answer(f'Введите название кабинета:')
        await state_room_add.add_title.set()
    elif inp.title() in build_2:
        answer = inp.title()
        await state.update_data(add_build=answer)
        await message.answer(f'Введите название кабинета:')
        await state_room_add.add_title.set()
    else:
        await message.answer("Такого заведения не существует, ну или вы сделали ошибку вводе"
                             "введите одно из заведений - ККМТ, ТТД, МГОТУ, Общежитие №1, Общежитие №2\n"
                             "вызевите заново команду /add_room")
        await state.finish()


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
    lens = await commands.select_all_rooms()

    lis = []
    if lens == []:
        lis.append(0)

    for arg in lens:
        lis.append(arg.room_id)
    lis.sort()
    id = lis[-1] + 1

    await state.update_data(add_nomer=answer)
    data = await state.get_data()

    number, build, title, comment, nomer = data.get('add_number'), data.get('add_build'), \
                                           data.get('add_title'), data.get('add_comment'), data.get('add_nomer')

    await commands.add_room(room_id=id,
                            number=number.title(),
                            build=build,
                            title=title.title(),
                            comment=comment,
                            nomer=nomer)

    await message.answer(f' Вы успешно добавили кабинет\n'
                         f'Проверте правильно ли вы вели информацию:')

    room = await commands.select_room_id(id)
    await message.answer(f'ID: {room.room_id}\n\n'
                         f'Заведение: {room.build}\n'
                         f'Номер кабинета: {room.number}\n'
                         f'Название кабинета: {room.title}\n'
                         f'Описание: {room.comment}\n'
                         f'Номер: {room.nomer}')

    await state.finish()


@dp.message_handler(IsPrivate(), Command('all_rooms'))
async def get_all_rooms(message: Message):
    status = await users.select_user(message.from_user.id)
    if status == 'admin' or status == 'general_admin' or message.from_user.id == ID:
        rooms = await commands.select_all_rooms()

        if rooms == []:
            await message.answer('База данных пуста')

        for room in rooms:
            await message.answer(f'ID: {room.room_id}\n\n'
                                 f'Заведение: {room.build}\n'
                                 f'Номер кабинета: {room.number}\n'
                                 f'Название кабинета: {room.title}\n'
                                 f'Описание: {room.comment}\n'
                                 f'Номер: {room.nomer}')
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')
