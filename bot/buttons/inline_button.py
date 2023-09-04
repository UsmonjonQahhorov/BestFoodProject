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
        button = InlineKeyboardButton(text=category_name, callback_data=category_name)
        design.append([button])
    inline_markup = InlineKeyboardMarkup(inline_keyboard=design, resize_keyboard=True)
    return inline_markup


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests


async def food_buttons():
    response = []
    food = requests.get("http://127.0.0.1:8000/food_list/")

    try:
        food_response = food.json()
    except requests.exceptions.RequestException as e:
        print("Error requesting food data:", e)
        return None
    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return None
    for food_item in food_response:
        food_name = food_item.get('name')
        food_category = food_item.get('category')
        button = InlineKeyboardButton(text=food_name, callback_data=f"food:{food_name}")
        response.append([button])

    inline_markup = InlineKeyboardMarkup(inline_keyboard=response, resize_keyboard=True)
    return inline_markup


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
