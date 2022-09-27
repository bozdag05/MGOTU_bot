from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from filters import IsPrivate
from states.state_of_docs import state_doc_add, state_doc_drop
from utils.db_api import docs_commands as commands
from data.config import GENERAL_ID as ID

from loader import dp


@dp.message_handler(IsPrivate(), Command('del_doc'))
async def del_room(message: Message):
    if message.from_user.id == ID:
        await message.answer(f'Введите название файла который вы хотите удалить:')
        await state_doc_drop.drop_doc.set()
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')


@dp.message_handler(state=state_doc_drop.drop_doc)
async def del_room(message: Message, state: FSMContext):
    answer = message.text

    doc = await commands.select_doc(answer)
    if doc == None:
        await message.answer(f'документа "{answer}" нету в базе данных')
    else:
        await state.update_data(drop_doc=answer)
        data = await state.get_data()
        name_file = data.get('drop_doc')
        await commands.delete_doc(name_file)
        await message.answer(f'Запись успешно удалена')

    await state.finish()


@dp.message_handler(IsPrivate(), Command('add_doc'))
async def add_room(message: Message):
    if message.from_user.id == ID:
        await message.answer(f'Введите название файла который вы хотите добавить:')
        await state_doc_add.add_name_file.set()
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')


@dp.message_handler(state=state_doc_add.add_name_file)
async def add_1(message: Message, state: FSMContext):
    answer = message.text
    try:
        doc = await commands.select_doc(answer)
        if doc.name_file.lower() == answer.lower():
            await message.answer(f'Такой документ уже существует\n'
                                 f'вот информация по этому документу')

            doc = await commands.select_doc(answer)
            await message.answer(f'Заведение: {doc.build}\n'
                                 f'документ: {doc.name_file}\n'
                                 f'ссылка: {doc.file_url}\n')

    except Exception:

        await state.update_data(add_name_file=answer)
        await message.answer(f'Введите заведение:')
        await state_doc_add.add_build.set()


@dp.message_handler(state=state_doc_add.add_build)
async def add_2(message: Message, state: FSMContext):
    inp = message.text
    if inp.upper() in ['ККМТ', 'ТТД', 'МГОТУ']:
        answer = inp.upper()
    elif inp.title() in ["Общежитие №1", "Общежитие №1"]:
        answer = inp.title()
    else:
        await message.answer("Такого заведения не существует, ну или вы сделали ошибку в воде")
        await state.finish()

    await state.update_data(add_build=answer)
    await message.answer('Введите ссылку документа:')
    await state_doc_add.add_file_url.set()


@dp.message_handler(state=state_doc_add.add_file_url)
async def add_5(message: Message, state: FSMContext):
    answer = message.text

    await state.update_data(add_file_url=answer)
    data = await state.get_data()
    name_file, build, file_url = data.get('add_name_file'), data.get('add_build'), \
                                 data.get('add_file_url')

    await commands.add_doc(name_file=name_file,
                           build=build,
                           file_url=file_url)

    await message.answer(f' Вы успешно добавили документ\n'
                         f'Проверте правильно ли вы вели информацию:')
    doc = await commands.select_doc(name_file)
    await message.answer(f'Заведение: {doc.build}\n'
                         f'документ: {doc.name_file}\n'
                         f'ссылка: {doc.file_url}\n')

    await state.finish()


@dp.message_handler(IsPrivate(), Command('all_docs'))
async def get_all_rooms(message: Message):
    if message.from_user.id == ID:
        docs = await commands.select_all_docs()
        for doc in docs:
            await message.answer(f'Заведение: {doc.build}\n'
                                 f'документ: {doc.name_file}\n'
                                 f'ссылка: {doc.file_url}\n')
    else:
        await message.answer(f'{message.from_user.first_name}, you not admin')
