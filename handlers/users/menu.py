from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.user_balance import user_balance
from utils.db_api.order_controller import get_orders
from utils.format_message import get_balance, show_message
from loader import dp, bot


@dp.callback_query_handler(text_contains='balance', state='*')
async def balance_menu(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text(await get_balance(call.message.chat.id))
    await call.message.edit_reply_markup(reply_markup=await user_balance())


@dp.callback_query_handler(text_contains='history', state='*')
async def get_history(call: CallbackQuery, state: FSMContext):
    await state.finish()
    orders = await get_orders(int(call.message.chat.id))
    if orders is None:
        await call.answer('Истории транзакций не найдено')
    else:
        for order in orders[:10]:
            await bot.send_message(call.message.chat.id, show_message(order))
