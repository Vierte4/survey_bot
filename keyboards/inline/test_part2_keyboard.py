from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

variants_extra_callback = CallbackData("variants_extra_callback", "variant")
question_yesno_callback = CallbackData("question_yesno_callback", "variant")
food_callback = CallbackData("food_callback", "variant")
question_move_callback = CallbackData("question_move_callback", "direction")
food_move_callback = CallbackData("food_move_callback", "direction")


def question_extra_creator(question, back=True):
    # Возвращает клавиатуру, построенную на основе файлов в директории, в которой находится программа
    variants = InlineKeyboardMarkup()
    for a in range(1, len(question)):
        variants.add(InlineKeyboardButton(text=f'{question[a]}',
                                          callback_data=variants_extra_callback.new(
                                              variant=f'{a}')))

    if back:
        variants.add(InlineKeyboardButton(text="⬅",
                                          callback_data=question_move_callback.new(
                                              direction=-1)))
    return variants


def question_yesno_creator(question, back=True):
    # Возвращает клавиатуру, построенную на основе файлов в директории, в которой находится программа
    variants = InlineKeyboardMarkup()
    for a in range(1, len(question)):
        variants.add(InlineKeyboardButton(text=f'{question[a]}',
                                          callback_data=question_yesno_callback.new(
                                              variant=f'{a}')))

    if back:
        variants.add(InlineKeyboardButton(text="⬅",
                                          callback_data=question_move_callback.new(
                                              direction=-1)))
    return variants


def food_creator(question, back=True):
    # Возвращает клавиатуру, построенную на основе файлов в директории, в которой находится программа
    variants = InlineKeyboardMarkup()
    for a in range(1, len(question)):
        variants.add(InlineKeyboardButton(text=f'{question[a]}',
                                          callback_data=food_callback.new(
                                              variant=f'{a}')))

    if back:
        variants.add(InlineKeyboardButton(text="⬅",
                                          callback_data=food_move_callback.new(
                                              direction=-1)))
    return variants
