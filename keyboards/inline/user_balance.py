from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def user_balance():
    balance = InlineKeyboardMarkup(row_width=3)
    balance.add(InlineKeyboardButton('Пополнить', callback_data='pay'))
    balance.add(InlineKeyboardButton('История пополнений', callback_data='story'))
    balance.add(InlineKeyboardButton('Назад', callback_data='cancel'))
    return balance


async def method_balance():
    method = InlineKeyboardMarkup(row_width=3)
    method.row(InlineKeyboardButton('QIWI', callback_data='qiwi'), InlineKeyboardButton('Криптовалюта', callback_data='cryptonator'))
    method.add(InlineKeyboardButton('Назад', callback_data='cancel'))
    return method



