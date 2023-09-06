from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ContentType
from geopy import Nominatim
import requests

from bot.buttons.inline_button import category_buttons, food_buttons
from bot.buttons.reply_button import location
from bot.buttons.text import order, menu
from bot.dispatcher import dp

geolocator = Nominatim(user_agent="myGeocoder")


@dp.message_handler(Text(menu))
async def category_create(msg: types.Message, state: FSMContext):
    await msg.answer(text="<i>Buyurtmani davom ettirish uchun iltimos categoryalardan birini tanlang👇</i>",
                     parse_mode="HTML",
                     reply_markup=await category_buttons())
    await state.set_state("category")


@dp.callback_query_handler(Text("🥘Ovqatlar"), state="category")
async def what_delete_handler(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(f"<b>Ovqatlar royhati🥘\n"
                              "Ovqatlardan birini tanlang👇</b>", parse_mode="HTML",
                              reply_markup=await food_buttons())



# @dp.message_handler(Text(order))
# async def order_create(msg: types.Message, state: FSMContext):
#     await state.set_state('location')
#     await msg.answer(text="<b>Buyurtmani davom ettirish uchun iltimos lokatsiyangizni yuboring</b>", parse_mode="HTML",
#                      reply_markup=await location())
#
#
# @dp.message_handler(state='location', content_types=ContentType.LOCATION)
# async def location_handler(msg: types.Message, state: FSMContext):
#     lat = msg.location.latitude
#     lon = msg.location.longitude
#     location = geolocator.reverse((lat, lon), exactly_one=True)
#
#     if location:
#         address = location.raw.get('display_name', 'Unknown Address')
#         await msg.answer(text=f"<b>Sizning manzilingiz: {address}</b>", parse_mode="HTML")
#     else:
#         await msg.answer(text="<b>Manzil topilmadi</b>", parse_mode="HTML")
