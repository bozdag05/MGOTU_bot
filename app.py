async def bot_on_startup(dp):
    from utils.admins_comand import on_startup_admin
    from utils.db_api.db_mgotu import on_startup, db
    from utils.users_commands import set_default_commands, set_admins_commands

    import filters
    filters.setup(dp)




    '''print("Подключение к БД")
    await on_startup(dp)

    print("Удаляем таблицы в БД")
    await db.gino.drop_all()

    print("Создаём новые таблицы в БД")
    await db.gino.create_all()
    print("готово")'''

    await on_startup(dp)
    await on_startup_admin(dp)
    await set_default_commands(dp)

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=bot_on_startup)
