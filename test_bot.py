import asyncio

from aiogram import types, Bot, Dispatcher
from aiogram.filters import Command
from random import *


TOKEN = "7391043820:AAF7_1bKC-K_LekoBM4PGdJVEExraR588vc"
channel_name = "@"

bot = Bot(token=TOKEN)
dp = Dispatcher()

user_data = {}

@dp.message()
async def handle_text(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_data or message.text == '/start':
        await start(message)
    elif 'phone' not in user_data[user_id]:
        await send_code(message)
    elif 'status' not in user_data[user_id]:
        await check_code(message)
    elif 'location' not in user_data[user_id]:
        await info_location(message)
    elif 'kategoriyalar' in user_data[user_id]['holat']:
        await show_menu(message)
    elif 'tovarlar' in user_data[user_id]['holat']:
        await check_menu(message)
    elif 'tovar' in user_data[user_id]['holat']:
        await check_items(message)
