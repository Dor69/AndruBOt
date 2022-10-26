import requests
from bs4 import BeautifulSoup
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import asyncio
from config import BOT_TOKEN

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Ща зарегаем")
    await message.answer("Введите имя")
           
if __name__ == '__main__':
    executor.start_polling(dp)