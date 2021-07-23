from utils.get_currency import calculate_sum
from utils.db_api.user_controller import get_user
import asyncio

def accept_message(data_dict):
    summary = calculate_sum(data_dict)
    str_data = '<b>Подтвердите действие:</b>\n<b>Валюта перевода:</b> {get_currency}\n<b>Страна перевода:</b> {get_country}\n<b>Сумма перевода:</b> {amount_get}\n<b>Номер карты получателя:</b> {card_number}\n<b>ФИО получателя:</b> {FIO}\n<b>Сумма списания со счета:</b> {summary}$'.format(
        get_currency=data_dict['get_currency'], get_country=data_dict['get_country'], amount_get=data_dict['amount_order'],
        card_number=data_dict['card_number'], FIO=data_dict['FIO'], summary=summary)
    return str_data


async def get_balance(telegram_id):
    user = await get_user(telegram_id)
    return f'<b>Текущий баланс:</b> {user.balance}$'


async def get_balance_value(telegram_id):
    user = await get_user(telegram_id)
    return user.balance


def show_message(data_dict):
    str_data = '<b>ID заказа:</b> {id}\n<b>Валюта перевода:</b> {get_currency}\n<b>Страна перевода:</b> {get_country}\n<b>Сумма перевода:</b> {amount_get}\n<b>Номер карты получателя:</b> {card_number}\n<b>ФИО получателя:</b> {FIO}\n<b>Сумма списания со счета:</b> {summary}$ \n<b>Статус:</b> {status}'.format(
        id=data_dict.id, get_currency=data_dict.currency_get, get_country=data_dict.country_get, amount_get=data_dict.amount_get,
        card_number=data_dict.card_number, FIO=data_dict.FIO, summary=data_dict.amount_spend, status=data_dict.status)
    return str_data


def show_pay(data_dict):
    str_data = '<b>ID транзакции: </b>{id_trans}\n<b>Сумма:</b> {amount} \n<b>Платежная система:</b> {type_transaction}\n<b>Статус: </b>{status}'.format(
        id_trans=data_dict.id, amount=data_dict.amount,
        type_transaction=data_dict.type_transaction, status=data_dict.status)
    return str_data


async def admin_pay(data_dict):
    user = await get_user(data_dict.user_id)
    str_data = '<b>ID транзакции: </b>{id_trans}\n<b>username пользователя: </b>{username}\n<b>id_telegram: </b>{id_telegram}\n<b>Платежная система: </b>{type_transaction}\n<b>Сумма: </b>{amount}'.format(
        id_trans=data_dict.id, username=user.username, id_telegram=data_dict.user_id,
        type_transaction=data_dict.type_transaction, amount=data_dict.amount)
    return str_data


async def admin_order(data_dict):
    str_data = '<b>ID заказа:</b> {id}\n<b>Валюта перевода:</b> {get_currency}\n<b>Страна перевода:</b> {get_country}\n<b>Сумма перевода:</b> {amount_get}\n<b>Номер карты получателя:</b> {card_number}\n<b>ФИО получателя:</b> {FIO}\n<b>Сумма списания со счета:</b> {summary}$'.format(
        id=data_dict.id, get_currency=data_dict.currency_get, get_country=data_dict.country_get,
        amount_get=data_dict.amount_get, card_number=data_dict.card_number, FIO=data_dict.FIO, summary=data_dict.amount_spend)
    return str_data


