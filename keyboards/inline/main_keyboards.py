from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def create_main_menu():
    main_keyboard = InlineKeyboardMarkup()
    main_keyboard.add(InlineKeyboardButton('Перевести', callback_data='transfer'))
    main_keyboard.add(InlineKeyboardButton('Баланс', callback_data='balance'))
    main_keyboard.add(InlineKeyboardButton('История операций', callback_data='history'))
    main_keyboard.add(InlineKeyboardButton('Пополнить', callback_data='pay'))
    return main_keyboard
