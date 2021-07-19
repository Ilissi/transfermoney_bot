from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def create_main_menu():
    main_keyboard = InlineKeyboardMarkup(row_width=3)
    main_keyboard.add(InlineKeyboardButton('Перевести', callback_data='transfer'))
    main_keyboard.add(InlineKeyboardButton('Баланс', callback_data='balance'))
    main_keyboard.add(InlineKeyboardButton('История операций', callback_data='history'))
    return main_keyboard


async def accept_order():
    accept_keyboard = InlineKeyboardMarkup()
    accept_keyboard.row(InlineKeyboardButton('OK', callback_data='OK'),
                        InlineKeyboardButton('ОТМЕНА', callback_data='cancel'))
    return accept_keyboard
