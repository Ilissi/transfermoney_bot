from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

import typing

from keyboards.inline.currency import create_currency_get, create_country_get
from keyboards.inline.main_keyboards import accept_order
from states.add_order import Order
from utils.callback import currency_cb, country_cb
from utils.format_message import accept_message, get_balance, get_balance_value
from utils.get_currency import calculate_sum
from utils.db_api.order_controller import add_order
from utils.db_api.user_controller import update_balance

from loader import dp


@dp.callback_query_handler(text_contains='transfer', state='*')
@dp.callback_query_handler(currency_cb.filter(action='first'), state=Order.get_currency)
async def balance_menu(call: CallbackQuery, state: FSMContext):
    await Order.get_currency.set()
    balance = await get_balance(call.message.chat.id)
    await call.message.edit_text(f'{balance}\n<b>Выбери валюту,</b> которую хочешь получить:')
    await call.message.edit_reply_markup(reply_markup=await create_currency_get('get_currency', 'first'))


@dp.callback_query_handler(currency_cb.filter(action='second'), state=Order.get_currency)
async def balance_menu(call: CallbackQuery, state: FSMContext):
    balance = await get_balance(call.message.chat.id)
    await call.message.edit_text(f'{balance}\n<b>Выбери валюту,</b> которую хочешь получить:')
    await call.message.edit_reply_markup(reply_markup=await create_currency_get('get_currency', 'second'))


@dp.callback_query_handler(currency_cb.filter(action='get_currency'), state=Order.get_currency)
async def post_country(call: CallbackQuery, callback_data: typing.Dict[str, str], state: FSMContext):
    await state.update_data(get_currency=callback_data['currency'])
    await Order.next()
    await call.message.edit_text('<b>Выбери страну валюты,</b> которую хочешь обменять:')
    await call.message.edit_reply_markup(reply_markup=await create_country_get('get_country', callback_data['currency']))


@dp.callback_query_handler(country_cb.filter(action='get_country'), state=Order.get_country)
async def post_amount(call: CallbackQuery, callback_data: typing.Dict[str, str], state: FSMContext):
    await state.update_data(get_country=callback_data['country'])
    await Order.next()
    await call.message.delete()
    await call.message.answer('Введите сумму для обмена:')


@dp.message_handler(lambda message: message.text.isdigit(), state=Order.amount_order)
async def get_amount(message: Message, state: FSMContext):
    await state.update_data(amount_order=float(message.text))
    await Order.next()
    await message.answer('Введите номер карты получателя:')


@dp.message_handler(lambda message: not message.text.isdigit(), state=Order.amount_order)
async def get_amount(message: Message, state: FSMContext):
    await message.answer('Неправильно указана сумма обмена, попробуй еще раз!')


@dp.message_handler(state=Order.card_number)
async def get_card_number(message: Message, state: FSMContext):
    await Order.next()
    await state.update_data(card_number=message.text)
    await message.answer('Введите ФИО получателя:')


@dp.message_handler(state=Order.FIO)
async def get_FIO(message: Message, state: FSMContext):
    await state.update_data(FIO=message.text)
    user_data = await state.get_data()
    await message.answer(text=accept_message(user_data), reply_markup=await accept_order())


@dp.callback_query_handler(text_contains='OK', state='*')
async def create_accept(call: CallbackQuery, state: FSMContext):
    balance = await get_balance_value(call.message.chat.id)
    user_data = await state.get_data()
    amount = calculate_sum(user_data)
    if amount < 10:
        await call.message.edit_text('Минимальная сумма обмена 10 USD')
    elif balance < amount:
        await call.message.edit_text('На балансе недостаточно USD для обмена!')
    elif balance >= amount:
        await call.message.edit_text('Заявка на обмен отправлена!')
        await add_order(user_id=call.message.chat.id, amount_get=user_data['amount_order'], accepted=False,
                        currency_get=user_data['get_currency'], country_get=user_data['get_country'],
                        card_number=user_data['card_number'], FIO=user_data['FIO'], amount_spend=amount,
                        status='Не подтверждена администратором')
        new_balance = round(balance-amount, 2)
        await update_balance(call.message.chat.id, new_balance)
    await state.finish()


