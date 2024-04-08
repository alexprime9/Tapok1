from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from config import TOKEN

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Games(StatesGroup):
    game = State()
    delivery = State()
    accept = State()
    phone = State()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.delete()
    keyboard = InlineKeyboardMarkup(row_width=3).add(
        InlineKeyboardButton('Action', callback_data='Action'),
        InlineKeyboardButton('MMO', callback_data='MMO'),
        InlineKeyboardButton('RPG', callback_data='RPG')
    )
    await message.answer('Здравствуйте!\nВы находитесь в магазине игр\nВыберите жанр игры:', reply_markup=keyboard)
    await Games.game.set()


@dp.callback_query_handler(state=Games.game)
async def get_games(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['game'] = call.data
    keyboard = InlineKeyboardMarkup(row_width=2).add(
        InlineKeyboardButton('Доставка курьером', callback_data='courier'),
        InlineKeyboardButton('Самовывоз', callback_data='pickup')
    )
    await call.message.edit_text(text='Выберите вариант доставки:', reply_markup=keyboard)
    await Games.next()


@dp.callback_query_handler(state=Games.delivery)
async def process_delivery(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['delivery'] = 'Доставка курьером' if call.data == 'courier' else 'Самовывоз'
    keyboard = InlineKeyboardMarkup(row_width=2).add(
        InlineKeyboardButton('Оплатить', callback_data='pay'),
        InlineKeyboardButton('Отмена', callback_data='cancel')
    )
    await call.message.edit_text(text='Теперь вы можете перейти к <u>Оплате</u> или <u>Отменить заказ</u>', parse_mode='HTML', reply_markup=keyboard)
    await Games.next()


@dp.callback_query_handler(state=Games.accept)
async def process_accept(call: types.CallbackQuery, state: FSMContext):
    if call.data == 'pay':
        await call.message.edit_text(text='Оплата через QIWI.\nВведите номер телефона для оплаты:')
        await Games.next()
    else:
        await call.message.edit_text(text='Вы отменили оплату')
        await state.finish()


@dp.message_handler(state=Games.phone)
async def process_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    # Здесь пишите валидацию номера телефона и логику для оплаты через Qiwi.
    # Для проверки выведем полученные ранее данные от пользователя.
    await message.answer(text=f'Жанр: {data["game"]}\nСпособ доставки: {data["delivery"]}\nНомер телефона: {data["phone"]}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp)