from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

category =


async def pubg_prices_buttons():
    design = []
    for i in pubg_mobile_prices:
        for i in i.items():
            key = f"{i[0]} -> {i[1]}"
            value = i[1]
        design.append([InlineKeyboardButton(text=key, callback_data=value)])
    return InlineKeyboardMarkup(inline_keyboard=design, resize_keyboard=True)