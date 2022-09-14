from aiogram.dispatcher.filters.state import StatesGroup, State


class state_contact_add(StatesGroup):
    add_contact = State()
    add_build = State()
    add_name_men = State()
    add_position = State()


class state_contact_drop(StatesGroup):
    drop_contact = State()
