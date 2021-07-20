from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def create_pay_link(pay_url):
    pay_keyboard = InlineKeyboardMarkup()
    pay_keyboard.add(InlineKeyboardButton('Оплатить', url=pay_url))
    pay_keyboard.add(InlineKeyboardButton('Назад', callback_data='cancel'))
    return pay_keyboard

