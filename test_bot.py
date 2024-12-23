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

@dp.message(Command("start"))
async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    button = [
        [types.KeyboardButton(text="Raqam jo'natish", request_contact=True)]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
    await message.answer("Assalomu alaykum! \n Les Ailes yetkazib berish xizmatiga xush kelibsiz:", reply_markup=keyboard)
    print(user_data)


async def send_code(message: types.Message):
    user_id = message.from_user.id
    i = '+1234567890'
    ok = True
    if message.contact is not None:
        phone_c = message.contact.phone_number
        user_data[user_id]['phone'] = phone_c
        verification_code = randint(100000, 999999)
        user_data[user_id]['verification_code'] = verification_code
        await message.answer(f"Nomerizga tasdiqlash ko'di yuborildi\n"
                         f"Iltimos kodni kiriting: {verification_code}")
    elif len(message.text) == 13 and message.text[0:4]  == '+998':
         for symbol in message.text:
             if symbol not in i:
                await message.answer('Hato nomer kiritildi')
                var = ok == False
                break

 if ok == True:
            phone = message.text
            user_data[user_id]['phone'] = phone
            verification_code = randint(100000, 999999)
            user_data[user_id]['verification_code'] = verification_code
            await message.answer(f"Nomerizga tasdiqlash ko'di yuborildi\n"
                                 f"Iltimos kodni kiriting: {verification_code}")

    else:
        await message.answer('Hato nomer kiritildi')
    print(user_data)

async def check_code(message: types.Message):
    user_id = message.from_user.id
    code = message.text
    verification_code = user_data[user_id]['verification_code']
    if str(verification_code) == code:
        user_data[user_id]['status'] = 'verified'
        await message.answer("Nomeringiz tasdiqlandi")
        await ask_location(message)
    else:
        await message.answer('Kod hato terildi. Yana urunib koring')
    print(user_data)


