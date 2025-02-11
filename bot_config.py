from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import dotenv_values
from aiogram import Bot, Dispatcher


token = dotenv_values(".env")['TOKEN']
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)