import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from bot.buttons.reply_button import phone_number, main_menu_buttons
from bot.dispatcher import dp


@dp.message_handler(CommandStart())
async def start_handler(msg: types.Message, state: FSMContext):
    user_id = str(msg.from_user.id)
    users = requests.get(f"http://127.0.0.1:8000/telegram_users/")
    user_response = users.json()
    users_list = []
    for i in user_response:
        users_list.append(i.get('chat_id'))
    if user_id in users_list:
        await msg.answer(text=f"<b>Aktiv foydalanuvchi✅</b>", parse_mode="HTML", reply_markup=await main_menu_buttons())
    else:
        await msg.answer(
            f"Assalomu alaykum <i>{msg.from_user.first_name}</i>.Men <i>Best Food</i> yetkazib berish xizmati botiman!",
            parse_mode="HTML")
        await msg.answer("Familiya ismingizni kiriting")
        await state.set_state('fullname_set')


@dp.message_handler(state='fullname_set')
async def register_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["fullname"] = msg.text
    await state.set_state("username")
    await msg.answer('Ismingizni kiriting👇:')


@dp.message_handler(state='username')
async def register_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["username"] = msg.text
    await msg.answer('Telefon raqamingizni jonating 👇📱: ', reply_markup=await phone_number())
    await state.set_state("phone")


@dp.message_handler(state='phone', content_types=types.ContentTypes.CONTACT)
async def phone(msg: types.Message, state: FSMContext):
    number = msg.contact.phone_number
    async with state.proxy() as data:
        username = data['username']
        fullname = data['fullname']
    response = requests.post(
        url='http://127.0.0.1:8000/telegram_users/',
        data={'chat_id': msg.chat.id,
              'fullname': fullname,
              'username': username,
              'phone_number': msg.contact.phone_number})
    print(response.status_code, response.json())
    await msg.answer("Telefon raqam muvaffaqiyatli saqlandi!")
    await msg.answer("Quyidigilardan birini tanlang!", reply_markup=await main_menu_buttons())
    await state.set_state('buyurtma berish')
