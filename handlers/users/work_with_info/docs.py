from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from filters import IsPrivate
from states.state_of_docs import state_doc_add, state_doc_drop
from utils.db_api import docs_commands as commands, quick_commands as users
from data.config import GENERAL_ID as ID, lis_build_2 as build_2, lis_build_1 as build_1

from loader import dp, bot


@dp.message_handler(IsPrivate(), Command('del_doc'))
async def del_room(message: Message):
    status = await users.select_user(message.from_user.id)
    if status == 'admin' or status == 'general_admin' or message.from_user.id == ID:
        await message.answer(f'Введите id файла который вы хотите удалить:')
        await state_doc_drop.drop_doc.set()
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')


@dp.message_handler(state=state_doc_drop.drop_doc)
async def del_room(message: Message, state: FSMContext):
    answer = message.text

    doc = await commands.select_doc_id(int(answer))

    if doc == None:
        await message.answer(f'В базе данных нету документа с id - "{answer}"')
    else:
        await state.update_data(drop_doc=answer)
        data = await state.get_data()
        doc_id = data.get('drop_doc')
        await commands.delete_doc(int(doc_id))
        await message.answer(f'Запись успешно удалена')

    await state.finish()


@dp.message_handler(IsPrivate(), Command('add_doc'))
async def add_room(message: Message):
    status = await users.select_user(message.from_user.id)
    if status == 'admin' or status == 'general_admin' or message.from_user.id == ID:
        await message.answer(f'Введите название файла который вы хотите добавить:')
        await state_doc_add.add_name_file.set()
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')


@dp.message_handler(state=state_doc_add.add_name_file)
async def add_1(message: Message, state: FSMContext):
    answer = message.text

    await state.update_data(add_name_file=answer.title())
    await message.answer(f'Введите заведение:')
    await state_doc_add.add_build.set()


@dp.message_handler(state=state_doc_add.add_build)
async def add_2(message: Message, state: FSMContext):
    inp = message.text
    if inp.upper() in build_1:
        answer = inp.upper()
        await state.update_data(add_build=answer)
        await message.answer('Введите ссылку документа:')
        await state_doc_add.add_file_url.set()

    elif inp.title() in build_2:
        answer = inp.title()
        await state.update_data(add_build=answer)
        await message.answer('Введите ссылку документа:')
        await state_doc_add.add_file_url.set()

    else:
        await message.answer("Такого заведения не существует, ну или вы сделали ошибку вводе\n"
                             "введите одно из заведений - ККМТ, ТТД, МГОТУ, Общежитие №1, Общежитие №2\n"
                             "вызевите заново команду /add_doc")
        await state.finish()


@dp.message_handler(state=state_doc_add.add_file_url)
async def add_5(message: Message, state: FSMContext):
    answer = message.text
    lens = await commands.select_all_docs()

    lis = []
    if lens == []:
        lis.append(0)

    for arg in lens:
        lis.append(arg.doc_id)
    lis.sort()
    id = lis[-1] + 1

    await state.update_data(add_file_url=answer)
    data = await state.get_data()
    name_file, build, file_url = data.get('add_name_file'), data.get('add_build'), \
                                 data.get('add_file_url')

    await commands.add_doc(doc_id=id,
                           name_file=name_file,
                           build=build,
                           file_url=file_url)

    await message.answer(f' Вы успешно добавили документ\n'
                         f'Проверте правильно ли вы вели информацию:')
    doc = await commands.select_doc_id(doc_id=id)
    await message.answer(f'ID: {doc.doc_id}\n\n'
                         f'Заведение: {doc.build}\n'
                         f'Документ: {doc.name_file}\n'
                         f'Ссылка: {doc.file_url}\n')

    await state.finish()


@dp.message_handler(IsPrivate(), Command('all_docs'))
async def get_all_rooms(message: Message):
    status = await users.select_user(message.from_user.id)
    if status == 'admin' or status == 'general_admin' or message.from_user.id == ID:
        docs = await commands.select_all_docs()

        if docs == []:
            await message.answer('База данных пуста')
        for doc in docs:
            await message.answer(f'ID: {doc.doc_id}\n\n'
                                 f'Заведение: {doc.build}\n'
                                 f'Документ: {doc.name_file}\n'
                                 f'Ссылка: {doc.file_url}\n')
    else:
        await message.answer(f'{message.from_user.first_name}, Вы не имеете доступа к этой информаций')
        await bot.send_message(ID, f'пользователь - {message.from_user.first_name} что-то мутит')
