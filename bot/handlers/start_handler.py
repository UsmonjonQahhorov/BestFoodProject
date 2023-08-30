import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from bot.buttons.reply_button import phone_number, main_menu_buttons
from bot.dispatcher import dp


@dp.message_handler(CommandStart())
async def start_handler(msg: types.Message, state: FSMContext):
    user_response = requests.get(f"http://127.0.0.1:8000/tgusers/{msg.from_user.id}/detail/")

    if user_response.status_code == 200:
        user_data = user_response.json()  # Assuming the server returns JSON data
        await msg.answer(text=f"<b>Aktiv foydalanuvchi✅</b>", parse_mode="HTML", reply_markup=await main_menu_buttons())
    else:
        await state.set_state('phone-number')
        await msg.answer(text=f"<b>Ro'yhatdan o'tish uchun telefon raqamingizni kiriting</b>", parse_mode="HTML",
                         reply_markup=await phone_number())


@dp.message_handler(content_types='contact', state='phone-number')
async def register(msg: types.Message, state: FSMContext):
    print("Hello")
    response = requests.post(url="http://127.0.0.1:8000/telegram_users/",
                             data={"chat_id": str(msg.from_user.id), "phone_number": msg.contact.phone_number,
                                   "full_name": msg.from_user.full_name,
                                   "username": f"@{msg.from_user.username}"})
    print(response)
    if response.status_code == 201:
        await msg.answer(text=f"<b>Registratsiya qilindi✅</b>", parse_mode="HTML",
                         reply_markup=await main_menu_buttons())
    await state.finish()
