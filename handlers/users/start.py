from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Text, Command
from aiogram.types import CallbackQuery

from keyboards.inline.main_keyboards import create_main_menu
from utils.db_api.user_controller import add_user
from utils.db_api.database import db

from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def main_menu(message: Message, state: FSMContext):
    await state.finish()
    await message.answer(f'Привет, {message.from_user.full_name}!\nЖми /menu')
    user = message.from_user
    try:
        await add_user(id_telegram=user.id, username=user.username, balance=0)
        await message.answer(f'Вы зарегестрированны!')
    except Exception as e:
        pass


@dp.message_handler(Command('menu'), state='*')
async def main_menu(message: Message, state: FSMContext):
    await state.finish()
    await message.answer(text='<b>Главное меню:</b>', reply_markup=await create_main_menu())


@dp.callback_query_handler(text_contains='cancel', state='*')
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def back_main_menu(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text('<b>Главное меню:</b>')
    await call.message.edit_reply_markup(reply_markup=await create_main_menu())









