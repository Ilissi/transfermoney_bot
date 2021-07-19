from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.callback import currency_cb, country_cb
from utils.currency_dict import dict_currency_get, list_currency_get


async def create_currency_get(action, half):
    middle_index = len(list_currency_get) // 2
    if half == 'first':
        list_currency_half = list_currency_get[:middle_index]
        page = 'Следующая страница'
        action_currency_keyboard = 'second'
    else:
        list_currency_half = list_currency_get[middle_index:]
        page = 'Предыдущая страница'
        action_currency_keyboard = 'first'
    currency_keyboard = InlineKeyboardMarkup()
    for index in range(0, len(list_currency_half), 3):
        currency_keyboard.row(InlineKeyboardButton(list_currency_half[index], callback_data=country_cb.new(action=action,
                                                                                                          country=
                                                                                                          list_currency_half[
                                                                                                              index])),
                              InlineKeyboardButton(list_currency_half[index + 1],
                                                   callback_data=country_cb.new(action=action,
                                                                                country=
                                                                                list_currency_half[
                                                                                    index + 1])),
                              InlineKeyboardButton(list_currency_half[index + 2],
                                                   callback_data=country_cb.new(action=action,
                                                                                country=
                                                                                list_currency_half[
                                                                                    index + 2])))
    currency_keyboard.add(InlineKeyboardButton(page, callback_data=currency_cb.new(action=action_currency_keyboard,
                                                                                   currency=action_currency_keyboard)))
    currency_keyboard.add(InlineKeyboardButton('Отмена', callback_data='cancel'))
    return currency_keyboard


async def create_country_get(action, country):
    country_keyboard = InlineKeyboardMarkup()
    countries = dict_currency_get[country]
    if len(countries) == 5:
        country_keyboard.row(InlineKeyboardButton(countries[0], callback_data=country_cb.new(action=action,
                                                                                             country=countries[0])),

                             InlineKeyboardButton(countries[1], callback_data=country_cb.new(action=action,
                                                                                             country=countries[1])),
                             InlineKeyboardButton(countries[2], callback_data=country_cb.new(action=action,
                                                                                             country=countries[2]))),
        country_keyboard.row(InlineKeyboardButton(countries[3], callback_data=country_cb.new(action=action,
                                                                                             country=countries[3])),

                             InlineKeyboardButton(countries[4], callback_data=country_cb.new(action=action,
                                                                                             country=countries[4])))
    elif len(countries) >= 3:
        for index in range(0, len(countries), 3):
            country_keyboard.row(InlineKeyboardButton(countries[index], callback_data=country_cb.new(action=action,
                                                                                                     country=countries[
                                                                                                         index])),
                                 InlineKeyboardButton(countries[index + 1], callback_data=country_cb.new(action=action,
                                                                                                         country=
                                                                                                         countries[
                                                                                                             index + 1])),
                                 InlineKeyboardButton(countries[index + 2], callback_data=country_cb.new(action=action,
                                                                                                         country=
                                                                                                         countries[
                                                                                                             index + 2])))
    elif len(countries) >= 2:
        index = 0
        country_keyboard.row(InlineKeyboardButton(countries[index], callback_data=country_cb.new(action=action,
                                                                                                 country=countries[
                                                                                                     index])),
                             InlineKeyboardButton(countries[index + 1], callback_data=country_cb.new(action=action,
                                                                                                     country=countries[
                                                                                                         index + 1])))
    elif len(countries) == 1:
        country_keyboard.add(
            InlineKeyboardButton(countries[0], callback_data=country_cb.new(action=action, country=countries[0])))
    country_keyboard.add(InlineKeyboardButton('Отмена', callback_data='cancel'))
    return country_keyboard
