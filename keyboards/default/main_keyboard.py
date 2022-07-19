from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

organizators_main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Начать тест')
        ],
    ],
    resize_keyboard=True
)
