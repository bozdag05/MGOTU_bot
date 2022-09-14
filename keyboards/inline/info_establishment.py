from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_mgotu = InlineKeyboardMarkup(row_width=3,
            inline_keyboard=[
                        [
                            InlineKeyboardButton(text='Адреса корпусов', callback_data='mgotu_adreses'),
                            InlineKeyboardButton(text='Локаций корпусов в яндексе', callback_data='mgotu_locations'),

                        ],
                        [
                            InlineKeyboardButton(text='Особые комнаты', callback_data='mgotu_rooms'),
                            InlineKeyboardButton(text='Документы', callback_data='mgotu_docs'),
                            InlineKeyboardButton(text='Контакты', callback_data='mgotu_contacts'),

                        ],
                        [
                            InlineKeyboardButton(text='закрыть', callback_data='close')
                        ],
            ])

ikb_kkmt = InlineKeyboardMarkup(row_width=3,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text='Адрес', callback_data='kkmt_adres'),
                                         InlineKeyboardButton(text='Локация в яндексе', callback_data='kkmt_location'),

                                     ],
                                     [
                                         InlineKeyboardButton(text='Особые комнаты', callback_data='kkmt_rooms'),
                                         InlineKeyboardButton(text='Документы', callback_data='kkmt_docs'),
                                         InlineKeyboardButton(text='Контакты', callback_data='kkmt_contacts'),

                                     ],
                                     [
                                         InlineKeyboardButton(text='закрыть', callback_data='close')
                                     ],
                                 ])

ikb_ttd = InlineKeyboardMarkup(row_width=3,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text='Адрес', callback_data='ttd_adres'),
                                         InlineKeyboardButton(text='Локация в яндексе', callback_data='ttd_location'),

                                     ],
                                     [
                                         InlineKeyboardButton(text='Особые комнаты', callback_data='ttd_rooms'),
                                         InlineKeyboardButton(text='Документы', callback_data='ttd_docs'),
                                         InlineKeyboardButton(text='Контакты', callback_data='ttd_contacts'),

                                     ],
                                     [
                                         InlineKeyboardButton(text='закрыть', callback_data='close')
                                     ],
                                 ])

ikb_dorm_1 = InlineKeyboardMarkup(row_width=3,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text='Адрес', callback_data='dorm_1_adres'),
                                         InlineKeyboardButton(text='Локация в яндексе', callback_data='dorm_1_location'),

                                     ],
                                     [
                                         InlineKeyboardButton(text='Особые комнаты', callback_data='dorm_1_rooms'),
                                         InlineKeyboardButton(text='Документы', callback_data='dorm_1_docs'),
                                         InlineKeyboardButton(text='Контакты', callback_data='dorm_1_contacts'),

                                     ],
                                     [
                                         InlineKeyboardButton(text='закрыть', callback_data='close')
                                     ],
                                 ])

ikb_dorm_2 = InlineKeyboardMarkup(row_width=3,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text='Адрес', callback_data='dorm_2_adres'),
                                         InlineKeyboardButton(text='Локация в яндексе', callback_data='dorm_2_location'),

                                     ],
                                     [
                                         InlineKeyboardButton(text='Особые комнаты', callback_data='dorm_2_rooms'),
                                         InlineKeyboardButton(text='Документы', callback_data='dorm_2_docs'),
                                         InlineKeyboardButton(text='Контакты', callback_data='dorm_2_contacts'),

                                     ],
                                     [
                                         InlineKeyboardButton(text='закрыть', callback_data='close')
                                     ],
                                 ])

ikb_remove = InlineKeyboardMarkup(inline_keyboard=[[]])


