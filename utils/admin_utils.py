from data.config import ADMINS
from utils.format_message import admin_pay, admin_order
from keyboards.inline.admin_keyboard import accept_pay, accept_oder
from loader import bot_admin


async def send_admin_pay_message(transaction_object):
    for admin in ADMINS:
        message = await admin_pay(transaction_object)
        await bot_admin.send_message(admin, message, reply_markup=await accept_pay(transaction_object))


async def send_admin_order_message(order_object):
    for admin in ADMINS:
        message = await admin_order(order_object)
        await bot_admin.send_message(admin, message, reply_markup=await accept_oder(order_object))