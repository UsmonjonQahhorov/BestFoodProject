import types

from bot.buttons.reply_button import phone_number
from bot.dispatcher import bot, dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Text
from bot.dispatcher import dp, bot
from aiogram import types
import requests


@dp.message_handler(CommandStart())
async def start_handler(msg: types.Message, state: FSMContext):
    user = requests.get(f"http://127.0.0.1:8000/telegram-user/{msg.from_user.id}")
    if user:
        await msg.answer(text=f"<b>Aktiv foydalanuvchi✅</b>", parse_mode="HTML", reply_markup=await main_menu_buttons())
    else:
        await state.set_state('phone-number')
        await msg.answer(text=f"<b>Ro'yhatdan o'tish uchun telefon raqamingizni kiriting</b>", parse_mode="HTML",
                         reply_markup=await phone_number())


@dp.message_handler(content_types='contact', state='phone-number')
async def register(msg: types.Message, state: FSMContext):
    requests.post(url="http://127.0.0.1:8000/telegram-users/",
                  data={"chat_id": str(msg.from_user.id), "phone_number": msg.contact.phone_number,
                        "full_name": msg.from_user.full_name,
                        "username": f"@{msg.from_user.username}"})
    await msg.answer(text=f"<b>Registratsiya qilindi✅</b>", parse_mode="HTML", reply_markup=await main_menu_buttons())
    await state.finish()
