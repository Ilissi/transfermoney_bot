from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.callback import pay_cb, order_cb


async def accept_pay(data_dict):
    accept_pay_keyboard = InlineKeyboardMarkup()
    accept_pay_keyboard.add(InlineKeyboardButton('Подтвердить', callback_data=pay_cb.new(data_dict.id, accept=True)),
                            InlineKeyboardButton('Отменить', callback_data=pay_cb.new(data_dict.id, accept=False)))
    return accept_pay_keyboard


async def accept_oder(data_dict):
    accept_order_keyboard = InlineKeyboardMarkup()
    accept_order_keyboard.add(
        InlineKeyboardButton('Подтвердить', callback_data=order_cb.new(data_dict.id, accept=True)),
        InlineKeyboardButton('Отменить', callback_data=order_cb.new(data_dict.id, accept=False)))
    return accept_order_keyboard
