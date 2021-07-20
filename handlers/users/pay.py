from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message


from utils.db_api.transaction_controller import get_transaction
from keyboards.inline.user_balance import method_balance
from utils.format_message import show_pay
from states.add_pay import Pay
from utils.pay_send.qiwi_API import qiwiAPI
from utils.pay_send.utils_cryptonator import create_invoice
from data.config import QIWI_API_KEY, QIWI_NUMBER
from keyboards.inline.pay_keyboard import create_pay_link

from loader import dp, bot


@dp.callback_query_handler(text_contains='story', state='*')
async def get_history_pay(call: CallbackQuery, state: FSMContext):
    await state.finish()
    pays = await get_transaction(call.message.chat.id)
    if pays is None:
        await call.message.answer('Пополнений нету')
    else:
        message = ''
        for pay in pays[:10]:
            message += show_pay(pay)
        bot.send_message(call.message.chat.id, message)


@dp.callback_query_handler(text_contains='pay', state='*')
async def get_methods_pay(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>Выбери способ оплаты:</b>')
    await call.message.edit_reply_markup(reply_markup=await method_balance())


@dp.callback_query_handler(text_contains='qiwi', state='*')
@dp.callback_query_handler(text_contains='cryptonator', state='*')
async def get_amount(call: CallbackQuery, state: FSMContext):
    await Pay.amount.set()
    await state.update_data(type=call.data)
    await call.message.edit_text('Введи сумму пополнения:')
    await call.message.edit_reply_markup()


@dp.message_handler(state=Pay.amount)
async def create_url(message: Message, state: FSMContext):
    await state.update_data(amount=message.text)
    pay_data = await state.get_data()
    await state.finish()
    if pay_data['type'] == 'qiwi':
        qiwiSend = qiwiAPI(QIWI_API_KEY, QIWI_NUMBER)
        url_data = qiwiSend.create_qiwi_invoice(float(pay_data['amount']))
        await message.answer('Оплатите счет QIWI:', reply_markup=await create_pay_link(url_data))
    elif pay_data['type'] == 'cryptonator':
        url_data = create_invoice(pay_data['amount'])
        await message.answer('Оплатите счет Cryptonator:', reply_markup=await create_pay_link(url_data))



