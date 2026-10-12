from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.main_keyboards import main_menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer_photo(caption=f"Assalomu alaykum\n<b>{message.from_user.full_name}</b>",
                            photo="https://i.pinimg.com/originals/7e/0f/64/7e0f64e278cabce4752abac1d8432389.jpg",
                            reply_markup=main_menu)