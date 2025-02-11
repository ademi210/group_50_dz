from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


reviewed_users = set()

class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    text = State()
    rate = State()


async def start_dialog(callback: CallbackQuery):
    user_id = callback.from_user.id
    if user_id in reviewed_users:
        await callback.message.answer('нельзя оставлять отзыв больше одного раза')
        return

    reviewed_users.add(user_id)
    await RestourantReview.name.set()
    await callback.message.answer('как вас зовут?')

async def process_name(message: Message, state: FSMContext):
    name = message.text
    async with state.proxy() as data:
        data['name'] = name
    await RestourantReview.next()
    await message.answer('какой у вас номер телефона?')

async def process_phone_number(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text
    await RestourantReview.next()
    await message.answer('какая у вас жалоба?')

async def process_text(message: Message, state:FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
    await RestourantReview.next()
    await message.answer('поставьте оценку от 1 до 5')

async def process_rate(message: Message, state:FSMContext):
    async with state.proxy() as data:
        data['rate'] = message.text
    await state.finish()
    await message.answer('спасибо за отзыв')




def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_dialog, lambda c: c.data == 'review')
    dp.register_message_handler(process_name, state=RestourantReview.name)
    dp.register_message_handler(process_phone_number, state=RestourantReview.phone_number)
    dp.register_message_handler(process_text, state=RestourantReview.text)
    dp.register_message_handler(process_rate, state=RestourantReview.rate)

