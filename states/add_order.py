from aiogram.dispatcher.filters.state import StatesGroup, State


class Order(StatesGroup):
    get_currency = State()
    get_country = State()
    amount_order = State()
    card_number = State()
    FIO = State()


