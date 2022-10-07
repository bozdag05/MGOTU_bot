from aiogram import Dispatcher


from data.config import GENERAL_ID, admins


async def on_startup_admin(dp: Dispatcher):
    text = 'Bot MGOTU started'
    print(text)
    for admin in admins:
        await dp.bot.send_message(chat_id=admin, text=text)
