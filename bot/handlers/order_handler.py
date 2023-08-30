from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ContentType
from geopy import Nominatim

from bot.buttons.reply_button import location
from bot.buttons.text import order
from bot.dispatcher import dp

geolocator = Nominatim(user_agent="myGeocoder")


@dp.message_handler(Text(order))
async def order_create(msg: types.Message, state: FSMContext):
    await state.set_state('location')
    await msg.answer(text="<b>Buyurtmani davom ettirish uchun iltimos lokatsiyangizni yuboring</b>", parse_mode="HTML",
                     reply_markup=await location())


@dp.message_handler(state='location', content_types=ContentType.LOCATION)
async def location_handler(msg: types.Message, state: FSMContext):
    lat = msg.location.latitude
    lon = msg.location.longitude
    location = geolocator.reverse((lat, lon), exactly_one=True)

    if location:
        address = location.raw.get('display_name', 'Unknown Address')
        await msg.answer(text=f"<b>Sizning manzilingiz: {address}</b>", parse_mode="HTML")
    else:
        await msg.answer(text="<b>Manzil topilmadi</b>", parse_mode="HTML")
