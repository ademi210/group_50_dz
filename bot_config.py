from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from database import Database
from decouple import config



token = config('TOKEN')
bot = Bot(token=token)
storage = MemoryStorage()
database = Database("database.sqlite3")
dp = Dispatcher(bot, storage=storage)
ADMINS = [6469468347, ]
