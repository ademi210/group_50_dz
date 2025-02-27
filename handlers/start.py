from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


async def start_handler(message: types.Message):
    user = message.from_user
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="наш сайт", url="https://dodopizza.kg"),
            InlineKeyboardButton(text="инстаграм профиль", url="https://www.instagram.com/dodopizza.kg/"),
            InlineKeyboardButton(text="вакансии", url="https://dodopizza.ru/")
        ],

        [
            InlineKeyboardButton(text="о нас", callback_data="abouts"),
            InlineKeyboardButton(text="контакты", callback_data="contacts"),
            InlineKeyboardButton(text="оставить отзыв", callback_data="review"),
        ],

    ])
    await message.answer(
        f'Привет,{user.first_name}! Вас приветствует официальный бот сети пиццерий "Додо пицца", выберите интересующий ваш сервис', reply_markup=kb)

async def about_us_handler(callback: CallbackQuery):
    await callback.message.answer(f"Додо Пицца — российская сеть пиццерий, основанная в 2011 году. Компания специализируется на быстром и качественном обслуживании, а также предлагает пиццу на любой вкус с возможностью индивидуальной настройки заказа.")


async def contact_handler(callback: CallbackQuery):
    await callback.message.answer(f"наш адрес:\nчуйский переулок 32Б\nномер телефона: 0709550550 ")



def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
    dp.register_callback_query_handler(about_us_handler, lambda c: c.data == "abouts")
    dp.register_callback_query_handler(contact_handler,lambda c: c.data == "contacts")
