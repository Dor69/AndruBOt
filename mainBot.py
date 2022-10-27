import requests
from bs4 import BeautifulSoup
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN
from StatesClassFile import StatesClass

storage = MemoryStorage()
bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)
state = None

data = []

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply(f"""Добрый ДЕНЬ
                        Это бот для регистрация
                        Введите свое имя:{message.text}""")
    await StatesClass.EnterName.set()
    
@dp.message_handler(state=StatesClass.EnterName)
async def enter_name(message: types.Message):
    print(message.text)
    data.append(message.text)
    await message.reply("""Имя принято
                        Введите вашу фамилию:""")
    await StatesClass.EnterSurename.set()
    

@dp.message_handler(state=StatesClass.EnterSurename)
async def enter_surename(message: types.Message):
    data.append(message.text)
    await message.reply("""Фамилия принята
                        Введите вашу отчество:""")
    await StatesClass.EnterPatronimyc.set()

@dp.message_handler(state=StatesClass.EnterPatronimyc)
async def enter_patronimyc(message: types.Message):
    data.append(message.text)
    await message.reply("""Отчество принято
                        Введите ВАШ номер:""")
    await StatesClass.EnterPhone.set()

@dp.message_handler(state=StatesClass.EnterPhone)
async def enter_patronimyc(message: types.Message):
    data.append(message.text)
    await message.reply(f"""Введенные вами данные:
                        {" ".join(data)}""")
    await StatesClass.Common.set()


if __name__ == '__main__':
    executor.start_polling(dp)
    