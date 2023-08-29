from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = '6295063109:AAGZsrbh6JP2iMuET8-z3717-jIRXP7z3N0'

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
