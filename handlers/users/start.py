from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import *
from keyboards.inline.test_part1_keyboard import choose_language_kb, \
    choose_language_callback, agreement_kb, agreement_callback, question_creator
from loader import dp, bot
from states.all_state import Answer
from utils.test_creator import file_reader


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!\n"
                         f"Выберите язык для прохождения анкетирования и взаимодействия с ботом",
                         reply_markup=choose_language_kb())
    users_data.data[str(message.from_user.id)] = {}
    users_data.data[str(message.from_user.id)]['n'] = 1
    if state:
        await state.finish()


@dp.callback_query_handler(choose_language_callback.filter())
async def bot_echo_all(call: types.CallbackQuery, callback_data: dict):
    answer = callback_data.get('language')
    users_data.data[str(call.from_user.id)]['language'] = answer
    users_data.update_data()
    text = file_reader(agreement_ru_path) if answer == 'ru' else file_reader(
        agreement_kz_path)
    await bot.edit_message_text(chat_id=call.from_user.id,
                                message_id=call.message.message_id,
                                text=text,
                                reply_markup=agreement_kb(answer))


@dp.callback_query_handler(agreement_callback.filter())
async def bot_echo_all(call: types.CallbackQuery, callback_data: dict):
    answer = callback_data.get('answer')
    lang = users_data.data[str(call.from_user.id)]['language']
    msg_txt = '✏️Отправьте ответ сообщением' if lang == 'ru' else '✏️Жауапты хабарламамен жіберіңіз'
    if answer == 'no':
        msg_text = 'Всего доброго!' if lang == 'ru' else 'Барлығы жақсы!'
        await call.message.answer(msg_text)
    else:
        temp_data[call.from_user.id] = {'extra_n': False, 'sub_mode': False}
        test = test_all[lang]

        await call.message.answer(f'1. {test[1][0]}\n' + msg_txt,
                                  reply_markup=question_creator(test[1][1:],
                                                                back=False))
        await Answer.openanswer.set()

