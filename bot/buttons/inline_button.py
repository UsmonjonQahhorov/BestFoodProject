from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests


async def category_buttons():
    response = []
    category = requests.get(f"http://127.0.0.1:8000/category_list/")
    user_response = category.json()
    for i in user_response:
        response.append(i.get('name'))

    for i in response:
        key = i
        response.append([InlineKeyboardButton(text=key, callback_data=key)])
    return InlineKeyboardMarkup(inline_keyboard=response, resize_keyboard=True)


async def food_buttons():
    response = []
    food = requests.get(f"http://127.0.0.1:8000/food_list")
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
