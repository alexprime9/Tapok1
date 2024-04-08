from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text

from config import *
from keybreads import inline_kb_top

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def process_rm_command(message: types.Message):
    await message.reply('Хотите узнать курс рубля по отношению к юаню, тогда кликай на ссылку',
                        reply_markup=inline_kb_top)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
