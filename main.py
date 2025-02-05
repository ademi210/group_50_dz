import asyncio
from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
import random

token = dotenv_values(".env")['TOKEN']
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_handler(message):
    user = message.from_user
    await message.answer(f"Привет,{user.first_name}!\n Мои команды:\n /start - начать работу с ботом\n"
                         f"/myinfo - информация о пользователе \n /random - случайное имя")


@dp.message_handler(commands=["myinfo"])
async def info_handler(message):
    user = message.from_user
    await message.answer(f'Ваше имя : {user.first_name}\nВаш ID: {user.id}\n'
                         f'Ваш ник: {user.username}\n')

@dp.message_handler(commands=["random"])
async def random_handler(message):
      my_tuple = ('Вова', 'Карина', 'Эля', 'Мила','Алексей', 'Александра, Арина, Виктория, Анна, Максим, Eва, Юлия, Кирилл, Никита, Илья, Мария')
      random_element = random.choice(my_tuple)
      await message.answer(f'Случайное имя: {random_element}')


@dp.message_handler()
async def echo_handler(message):
    text = message.text
    await message.answer(text)

async def main():
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())


