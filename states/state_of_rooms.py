from aiogram.dispatcher.filters.state import StatesGroup, State


class state_room_add(StatesGroup):
    add_number = State()
    add_build = State()
    add_title = State()
    add_comment = State()
    add_nomer = State()


class state_room_drop(StatesGroup):
    drop_room = State()
