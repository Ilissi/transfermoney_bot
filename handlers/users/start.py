from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.main_keyboards import create_main_menu

from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def main_menu(message: Message, state: FSMContext):
    await state.finish()
    await message.answer(text='Главное меню:', reply_markup=await create_main_menu())


