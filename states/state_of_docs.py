from aiogram.dispatcher.filters.state import StatesGroup, State


class state_doc_add(StatesGroup):
    add_name_file = State()
    add_file_url = State()
    add_build = State()


class state_doc_drop(StatesGroup):
    drop_doc = State()
