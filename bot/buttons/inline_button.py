from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
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



async def food_buttons():
    response = []
    food = requests.get(f"http://127.0.0.1:8000/food_list/")
    food_response = food.json()
    for i in food_response:
        response.append(i.get('name'))

    for i in response:
        key = i
        response.append([InlineKeyboardButton(text=key, callback_data=key)])
    return InlineKeyboardMarkup(inline_keyboard=response, resize_keyboard=True)


async def order_buttons():
    response = []
    order = requests.get(f"http://127.0.0.1:8000/order_list/")
    order_response = order.json()
    for i in order_response:
        response.append(i.get('name'))

    for i in response:
        key = i
        response.append([InlineKeyboardButton(text=key, callback_data=key)])
    return InlineKeyboardMarkup(inline_keyboard=response, resize_keyboard=True)
