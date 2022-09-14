from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

global_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Университет')
        ],
        [
            KeyboardButton(text='ТТД'),
            KeyboardButton(text='ККМТ'),
        ],
        [
            KeyboardButton(text='общежитие №1'),
            KeyboardButton(text='обшежитие №2'),
        ],
        [
            KeyboardButton(text='Все особые кабинеты'),
            KeyboardButton(text='закрыть'),
            KeyboardButton(text='Все контакты'),
        ]
    ],
    resize_keyboard=True
)

close_global_menu = ReplyKeyboardRemove(selective=False)
