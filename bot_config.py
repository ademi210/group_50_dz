from dotenv import dotenv_values
from aiogram import Bot, Dispatcher


token = dotenv_values(".env")['TOKEN']
bot = Bot(token=token)
dp = Dispatcher(bot)