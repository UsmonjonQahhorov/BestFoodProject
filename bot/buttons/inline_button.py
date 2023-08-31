from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests


async def category_buttons():
    design = []
    category = requests.get(f"http://127.0.0.1:8000/category_list/")
    try:
        category_response = category.json()
    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return None
    for category_item in category_response:
        category_name = category_item.get('name')
        callback_data = f"category:{category_name}"
        button = InlineKeyboardButton(text=category_name, callback_data=callback_data)
        design.append([button])
    inline_markup = InlineKeyboardMarkup(inline_keyboard=design, resize_keyboard=True)
    return inline_markup

