from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

corpuses_adres = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Корпус №1', callback_data='c1_adres'),
            InlineKeyboardButton(text='Корпус №2', callback_data='c2_adres'),
            InlineKeyboardButton(text='Корпус №3', callback_data='c3_adres'),
        ],
        [
            InlineKeyboardButton(text='назад', callback_data='end'),
        ]
    ]
)


corpuses_location = InlineKeyboardMarkup(row_width=3,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Корпус №1', callback_data='c1_location'),
            InlineKeyboardButton(text='Корпус №2', callback_data='c2_location'),
            InlineKeyboardButton(text='Корпус №3', callback_data='c3_location'),
        ],
        [
            InlineKeyboardButton(text='назад', callback_data='end'),
        ]
    ]
)
