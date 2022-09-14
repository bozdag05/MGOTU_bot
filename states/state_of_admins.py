from aiogram.dispatcher.filters.state import StatesGroup, State


class state__admin_add(StatesGroup):
    add_admin = State()


class state_admin_drop(StatesGroup):
    drop_admin = State()