from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

choose_language_callback = CallbackData("choose_language_callback", "language")
agreement_callback = CallbackData("agreement_callback", "answer")
variants_callback = CallbackData("variants_callback", "variant")
variants_111_callback = CallbackData("variants_111_callback", "variant")
skip_variants_callback = CallbackData("skip_variants_callback", "variant")
many_variants_callback = CallbackData("many_variants_callback", "variant")
question_move_callback = CallbackData("question_move_callback", "direction")
get_sub_number_callback = CallbackData("get_sub_number_callback", "number")


def choose_language_kb():
    variants = InlineKeyboardMarkup()
    variants.add(InlineKeyboardButton(text='Орысша/русский',
                                      callback_data=choose_language_callback.new(
                                          language='ru')))
    variants.add(InlineKeyboardButton(text='Қазақша/казахский',
                                      callback_data=choose_language_callback.new(
                                          language='kz')))
    return variants


def back_create():
    variants = InlineKeyboardMarkup()
    variants.add(InlineKeyboardButton(text="⬅",
                                      callback_data=question_move_callback.new(
                                          direction=-1)))
    return variants


def agreement_kb(language):
    if language == 'ru':
        variants = InlineKeyboardMarkup()
        variants.add(InlineKeyboardButton(text='Соглашаюсь',
                                          callback_data=agreement_callback.new(
                                              answer='yes')))
        variants.add(InlineKeyboardButton(text='Не соглашаюсь',
                                          callback_data=agreement_callback.new(
                                              answer='no')))
    else:
        variants = InlineKeyboardMarkup()
        variants.add(InlineKeyboardButton(text='келісемін',
                                          callback_data=agreement_callback.new(
                                              answer='yes')))
        variants.add(InlineKeyboardButton(text='келіспеймін',
                                          callback_data=agreement_callback.new(
                                              answer='no')))
    return variants


def question_creator(question, back=True):
    # Возвращает клавиатуру, построенную на основе файлов в директории, в которой находится программа
    variants = InlineKeyboardMarkup()

    for a in range(1, len(question)):
        variants.add(InlineKeyboardButton(text=f'{question[a]}',
                                          callback_data=variants_callback.new(
                                              variant=f'{a}')))

    if back:
        variants.add(InlineKeyboardButton(text="⬅",
                                          callback_data=question_move_callback.new(
                                              direction=-1)))
    return variants


def get_sub_number(question, back=True):
    # Возвращает клавиатуру, построенную на основе файлов в директории, в которой находится программа
    variants = InlineKeyboardMarkup()

    for a in range(1, len(question)):
        variants.add(InlineKeyboardButton(text=f'{question[a]}',
                                          callback_data=get_sub_number_callback.new(
                                              number=f'{a}')))

    if back:
        variants.add(InlineKeyboardButton(text="⬅",
                                          callback_data=question_move_callback.new(
                                              direction=-1)))

    return variants


def question_111_creator(question, back=True):
    # Возвращает клавиатуру, построенную на основе файлов в директории, в которой находится программа
    variants = InlineKeyboardMarkup()

    for a in range(1, len(question)):
        variants.add(InlineKeyboardButton(text=f'{question[a]}',
                                          callback_data=variants_111_callback.new(
                                              variant=f'{a}')))

    if back:
        variants.add(InlineKeyboardButton(text="⬅",
                                          callback_data=question_move_callback.new(
                                              direction=-1)))
    return variants


def skip_question_creator(question, back=True):
    # Возвращает клавиатуру, построенную на основе файлов в директории, в которой находится программа
    variants = InlineKeyboardMarkup()
    for a in range(1, len(question)):
        variants.add(InlineKeyboardButton(text=f'{question[a]}',
                                          callback_data=skip_variants_callback.new(
                                              variant=f'{a}')))

    if back:
        variants.add(InlineKeyboardButton(text="⬅",
                                          callback_data=question_move_callback.new(
                                              direction=-1)))
    return variants


def question_many_variants_creator(question, lang):
    # Возвращает клавиатуру, построенную на основе файлов в директории, в которой находится программа
    variants = InlineKeyboardMarkup()
    for a in range(1, len(question)):
        variants.add(InlineKeyboardButton(text=f'{question[a]}',
                                          callback_data=many_variants_callback.new(
                                              variant=f'{a}')))
    compleete_but = 'Завершить' if lang == 'ru' else "Аяқтау"
    variants.add(InlineKeyboardButton(text=compleete_but,
                                      callback_data=many_variants_callback.new(
                                          variant='complete')))
    return variants
