from aiogram.dispatcher.filters.state import StatesGroup, State


class Pay(StatesGroup):
    amount = State()
