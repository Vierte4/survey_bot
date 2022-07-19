from aiogram import types

from data.config import *
from keyboards.inline.test_part2_keyboard import variants_extra_callback, \
    food_callback, food_creator, \
    question_yesno_callback, food_move_callback
from loader import dp, bot
from states.all_state import Answer
from utils.test_sender import send_test, sub_test_sender


@dp.callback_query_handler(food_move_callback.filter())
async def bot_echo_all(call: types.CallbackQuery, callback_data: dict):
    lang = users_data.data[str(call.from_user.id)]['language']
    message_id = call.message.message_id
    user_id = call.from_user.id
    temp_data[user_id]['food_n'] -= 1
    food_n = temp_data[user_id]['food_n']
    question = food[lang][food_n]
    await bot.edit_message_text(text=f'{food_n}. {question}',
                                chat_id=user_id,
                                message_id=message_id,
                                reply_markup=food_creator(food_questions[lang]))


@dp.callback_query_handler(variants_extra_callback.filter())
async def bot_echo_all(call: types.CallbackQuery, callback_data: dict):
    answer = callback_data.get('variant')
    lang = users_data.data[str(call.from_user.id)]['language']
    n = users_data.data[str(call.from_user.id)]['n']
    message_id = call.message.message_id
    user_id = call.from_user.id
    cur_sub = temp_data[user_id]['cur_sub']

    if answer == '2':
        temp_data[user_id]['sub_n'] = len(sub_questions[lang]) - 1
        temp_data[user_id][n][cur_sub] = ['Нет']
        await sub_test_sender(user_id, message_id, answer, lang, n)

    else:
        temp_data[user_id]['sub_n'] = 0
        temp_data[user_id][n][cur_sub] = []
        await sub_test_sender(user_id, message_id, answer, lang, n)


@dp.callback_query_handler(question_yesno_callback.filter())
async def bot_echo_all(call: types.CallbackQuery, callback_data: dict):
    user_id = call.from_user.id
    message_id = call.message.message_id
    answer = callback_data.get('variant')
    lang = users_data.data[str(user_id)]['language']
    n = users_data.data[str(user_id)]['n']
    msg_txt = '✏️Отправьте ответ сообщением' if lang == 'ru' else '✏️Жауапты хабарламамен жіберіңіз'
    if answer == '1':
        await bot.edit_message_text(text=msg_txt,
                                    chat_id=user_id,
                                    message_id=message_id)
        await Answer.openanswer.set()

    else:
        if temp_data[user_id]['sub_mode']:
            await sub_test_sender(user_id=user_id,
                                  message_id=message_id, answer=answer,
                                  lang=lang, n=n)
        else:
            temp_data[user_id][n] = answer
            users_data.data[str(user_id)]['n'] += 1
            n = users_data.data[str(user_id)]['n']
            question = test_all[lang][n]
            await send_test(question=question, message_id=message_id,
                            user_id=user_id, n=n, lang=lang)


@dp.callback_query_handler(food_callback.filter())
async def bot_echo_all(call: types.CallbackQuery, callback_data: dict):
    answer = callback_data.get('variant')
    lang = users_data.data[str(call.from_user.id)]['language']
    n = users_data.data[str(call.from_user.id)]['n']
    message_id = call.message.message_id
    user_id = call.from_user.id
    food_n = temp_data[user_id]['food_n']
    temp_data[user_id][n][food_n] = answer
    if food_n == len(food[lang]) - 1:
        users_data.data[str(call.from_user.id)]['n'] += 1
        n = users_data.data[str(call.from_user.id)]['n']
        question = test_all[lang][n]
        await send_test(question, message_id, user_id, n, lang, answer=None)

    else:
        temp_data[user_id]['food_n'] += 1
        food_n += 1
        question = food[lang][food_n]
        await bot.edit_message_text(text=f'{food_n}. {question}',
                                    chat_id=user_id,
                                    message_id=message_id,
                                    reply_markup=food_creator(
                                        food_questions[lang]))
