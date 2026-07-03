from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from texts import BUTTON_TEXTS

def main_keyboard() -> ReplyKeyboardMarkup:
    buttons = list(BUTTON_TEXTS.keys())
    rows = []
    for i in range(0, len(buttons), 2):
        rows.append([KeyboardButton(text=b) for b in buttons[i:i+2]])
    return ReplyKeyboardMarkup(
        keyboard=rows,
        resize_keyboard=True,
        input_field_placeholder="یکی از گزینه‌ها را انتخاب کنید"
    )
