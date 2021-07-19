from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message

from states.add_pay import Pay
from utils.db_api.transaction_controller import get_transaction
from keyboards.inline.user_balance import method_balance
from utils.format_message import show_pay

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

