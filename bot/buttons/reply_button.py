from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.buttons.text import back, order, menu, orders, savat, about


async def main_menu_buttons():
    design = [
        [menu, orders],
        [savat],
        [about]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def phone_number():
    design = [[KeyboardButton(text="Telefon raqamni yuborish📲", request_contact=True)]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def location():
    design = [[KeyboardButton(text="Joylashuvni yuborish📍", request_location=True)], [back]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
