from aiogram import Dispatcher, types


async def info_handler(message: types.Message):
    user = message.from_user
    await message.answer(f'Ваше имя : {user.first_name}\nВаш ID: {user.id}\n'
                         f'Ваш ник: {user.username}\n')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(info_handler, commands=["myinfo"])