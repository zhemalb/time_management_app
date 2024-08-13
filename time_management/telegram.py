from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.web_app_info import WebAppInfo

from .config import settings

bot = Bot(settings.BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message.handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Приложение', web_app=WebAppInfo(url='http://localhost:3000')))
    await message.answer('Нажми кнопку', reply_markup=markup)


executor.start_polling(dp)
