from aiogram import Dispatcher


from data.config import GENERAL_ID


async def on_startup_admin(dp: Dispatcher):
    text = 'Bot MGOTU started'
    print(text)
    await dp.bot.send_message(chat_id=GENERAL_ID, text=text)
