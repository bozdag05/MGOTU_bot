from aiogram.dispatcher.filters.state import StatesGroup, State


class state_admin_add(StatesGroup):
    add_admin = State()


class state_admin_drop(StatesGroup):
    drop_admin = State()


class state_update_status(StatesGroup):
    update_status = State()
    new_status = State()
