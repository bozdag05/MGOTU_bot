from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Старт бота'),
        types.BotCommand('menu', 'Главное меню'),
        types.BotCommand('get_admins_commands', 'Получение команд админа'),
    ])


async def set_admins_commands(dp, chat_id: int):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Старт бота'),
        types.BotCommand('menu', 'Главное меню'),
        types.BotCommand('add_doc', 'Добавление документа'),
        types.BotCommand('add_room', 'добавление кабинета'),
        types.BotCommand('add_contact', 'добавление контакта'),
        types.BotCommand('del_doc', 'удаление документа'),
        types.BotCommand('del_room', 'удаление кабинета'),
        types.BotCommand('del_contact', 'удаление контакта'),
        types.BotCommand('all_docs', 'получить все документы'),
        types.BotCommand('all_rooms', 'получить все кабинеты'),
        types.BotCommand('all_contacts', 'получить все контакты'),
        types.BotCommand('get_users', 'получить всех пользователей'),
        types.BotCommand('get_user', 'получить свой профиль'),
        types.BotCommand('count_users', 'получить количество пользователей бота'),
        #types.BotCommand('drop_general_admin', 'Удалить генерального админа'),
        #types.BotCommand('drop_admin', 'удалить амина'),
        #types.BotCommand('add_admin', 'добавить админа'),
        #types.BotCommand('add_general_admin', 'добавить генерального админа'),
        types.BotCommand('update_status', 'Изменение статуса админу')
    ])


