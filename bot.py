import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import BOT_TOKEN
from keyboards import main_keyboard
from texts import WELCOME_TEXT, BUTTON_TEXTS

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(WELCOME_TEXT, reply_markup=main_keyboard())

@dp.message(F.text.in_(BUTTON_TEXTS.keys()))
async def menu_handler(message: Message):
    await message.answer(BUTTON_TEXTS[message.text], reply_markup=main_keyboard())

@dp.message()
async def unknown_handler(message: Message):
    await message.answer("لطفاً یکی از دکمه‌های منو را انتخاب کنید.", reply_markup=main_keyboard())

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
