from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text

from config import *
from keyboards import inline_kb_full

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def process_rm_command(message: types.Message):
    await message.reply('Выберите ваш любимый жанр фильмов', reply_markup=inline_kb_full)


@dp.callback_query_handler(text='123')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Ваш любимый жанр мелодрама')


@dp.callback_query_handler(text='btn2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Ваш любимый жанр комедия')


@dp.callback_query_handler(text='btn3')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Ваш любимый жанр Фантастика')


@dp.callback_query_handler(text='btn4')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Ваш любимый жанр Семейный')


@dp.callback_query_handler(text='btn5')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Ваш любимый жанр Ужасы')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
