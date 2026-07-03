from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from texts import BUTTON_TEXTS

def main_keyboard() -> ReplyKeyboardMarkup:
    rows = [
        [KeyboardButton(text="🌍 موقعیت جغرافیایی 📍")],
        [KeyboardButton(text="🏙 معرفی شهر جاجرم"), KeyboardButton(text="👥 جمعیت")],
        [KeyboardButton(text="📜 تاریخچه 🏛")],
        [KeyboardButton(text="💼 اقتصاد 💰"), KeyboardButton(text="☀️ آب‌وهوا 🌦")],
        [KeyboardButton(text="🎭 فرهنگ و آداب و رسوم 🎉")],
        [KeyboardButton(text="🏰 جاذبه‌های گردشگری 📸"), KeyboardButton(text="🍲 غذاهای محلی 😋")],
        [KeyboardButton(text="🛣 راه‌های دسترسی 🚗")],
        [KeyboardButton(text="🗣 زبان و گویش"), KeyboardButton(text="🏥 امکانات شهر 🏫")],
        [KeyboardButton(text="🌸 جمع‌بندی 🌸")],
    ]
    return ReplyKeyboardMarkup(
        keyboard=rows,
        resize_keyboard=True,
        input_field_placeholder="یکی از گزینه‌ها را انتخاب کنید"
    )
