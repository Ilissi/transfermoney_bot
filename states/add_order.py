from aiogram.dispatcher.filters.state import StatesGroup, State


class Order(StatesGroup):
    amount = State()
    currency = State()
    country = State()
