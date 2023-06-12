from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from login import token
import sqlite3
import logging

bot = Bot(token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

Keyboard_buttons = [
    KeyboardButton ('/backend'),
    KeyboardButton ('/frontend'),
    KeyboardButton ('/uxui'),
    KeyboardButton ('/android'),
    KeyboardButton ('/ios')
]
Keyboard_one = ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard=True).add(*Keyboard_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    
    await message.answer("Приветствую, чем я могу вам помочь", reply_markup=Keyboard_one)

@dp.message_handler(commands='backend')
async def beckend(message:types.Message):
    await message.answer("""Backend — это внутренняя часть продукта, которая находится на сервере и скрыта от пользователей.
Стоимость курса: 10.000 сомов в месяц.
Длительность обучения: 5 месяцев.""")

@dp.message_handler(commands='frontend')
async def frontend(messge:types.Message):
    await messge.answer("""Frontend разработчик -  Фронтенд — «лицо» системы; инструменты и компоненты, которые позволяют пользователю взаимодействовать с сайтом.
Стоимость курса: 10.000 сомов в месяц
Длитеоьность обучение: 5 месяцев""")

@dp.message_handler(commands='uxui')
async def uxui(messsage:types.Message):
    await messsage.answer("""Uxui разработчик - обучение длиться 4 месяцев, 2 дня в неделю
    оплата 40000 сом, знание гарантирована.""")

@dp.message_handler(commands='android')
async def android(messsage:types.Message):
    await messsage.answer("""Android разработчик - обучение длиться 5 месяцев, 2 дня в неделю
    оплата 70000 сом, знание гарантирована.""")

@dp.message_handler(commands='ios')
async def ios(messsage:types.Message):
    await messsage.answer("""Ios разработчик - обучение длиться 4 месяцев, 2 дня в неделю
    оплата 50000 сом, знание гарантирована""")

executor.start_polling(dp)