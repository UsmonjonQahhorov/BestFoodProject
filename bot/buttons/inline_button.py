from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import requests



async def pubg_prices_buttons():
    design = []
    category = requests.get(f"http://127.0.0.1:8000/category_list/")
    user_response = category.json()
    for i in user_response:
        design.append(i.get('name'))

    for i in design:
        key = i
        design.append([InlineKeyboardButton(text=key, callback_data=key)])
    return InlineKeyboardMarkup(inline_keyboard=design, resize_keyboard=True)