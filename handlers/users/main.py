from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import *
from keyboards.inline.test_part1_keyboard import *
from loader import dp, bot
from states.all_state import Answer
from utils.result_save import save_result
from utils.test_sender import send_test, sub_test_sender


@dp.callback_query_handler(variants_callback.filter())
async def bot_echo_all(call: types.CallbackQuery, callback_data: dict):
    answer = callback_data.get('variant')
    lang = users_data.data[str(call.from_user.id)]['language']
    n = users_data.data[str(call.from_user.id)]['n']
    message_id = call.message.message_id
    user_id = call.from_user.id

    if n == len(test_all[lang]) - 1:
        await bot.edit_message_text(
            text='Тест завершён, спасибо за уделённое время!',
            chat_id=user_id,
            message_id=message_id)
        save_result(user_id)
        return

    if temp_data[call.from_user.id]['sub_mode']:
        await sub_test_sender(user_id=user_id, message_id=message_id,
                              answer=answer, lang=lang, n=n)
    else:
        temp_data[call.from_user.id][n] = answer
        users_data.data[str(call.from_user.id)]['n'] += 1
        n += 1
        question = test_all[lang][n]

        await send_test(question=question, message_id=message_id,
                        user_id=user_id, n=n, lang=lang)


@dp.callback_query_handler(get_sub_number_callback.filter())
async def bot_echo_all(call: types.CallbackQuery, callback_data: dict):
    number = callback_data.get('number')
    lang = users_data.data[str(call.from_user.id)]['language']
    n = users_data.data[str(call.from_user.id)]['n']
    user_id = call.from_user.id

    temp_data[user_id][n] = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
    }

    temp_data[call.from_user.id]['sub_mode'] = True
    temp_data[user_id]['sub_n'] = 1  # номер текущего вопроса к приёму пищи
    temp_data[user_id]['num_sub'] = int(number)  # количество приёмов пищи
    temp_data[user_id]['cur_sub'] = 1  # номер текущего приёма пищи

    await bot.edit_message_text(
        text=f'Приём пищи 1. {sub_questions[lang][1][0]}',
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=question_111_creator(sub_questions[lang][1][1:],
                                          back=False))

    await Answer.openanswer.set()


@dp.callback_query_handler(skip_variants_callback.filter())
async def bot_echo_all(call: types.CallbackQuery, callback_data: dict):
    answer = callback_data.get('variant')
    lang = users_data.data[str(call.from_user.id)]['language']
    n = users_data.data[str(call.from_user.id)]['n']

    if temp_data[call.from_user.id]['sub_mode']:
        if answer == "2":
            cur_sub = temp_data[call.from_user.id]['cur_sub']
            temp_data[call.from_user.id]['sub_n'] += 1
            temp_data[call.from_user.id][n][int(cur_sub)].append('Нет')
        await sub_test_sender(user_id=call.from_user.id,
                              message_id=call.message.message_id, answer=answer,
                              lang=lang, n=n)
    else:
        temp_data[call.from_user.id][n] = answer
        n += 1
        if answer == '2':
            temp_data[call.from_user.id][n] = "Нет"
            n += 1

        question = test_all[lang][n]
        await send_test(question=question, message_id=call.message.message_id,
                        user_id=call.from_user.id, n=n, lang=lang)


@dp.message_handler(state=Answer.openanswer)
async def bot_echo_all(message: types.Message, state: FSMContext):
    await state.finish()
    answer = message.text + '.'
    lang = users_data.data[str(message.from_user.id)]['language']
    user_id = message.from_user.id
    message_id = message.message_id
    n = users_data.data[str(message.from_user.id)]['n']
    try:
        await bot.edit_message_reply_markup(chat_id=user_id,
                                            message_id=message_id - 1)
    except:
        pass
    await message.answer('Вопрос грузится')

    if temp_data[message.from_user.id]['sub_mode']:
        await sub_test_sender(user_id=user_id, message_id=message_id + 1,
                              answer=answer, lang=lang, n=n)
    else:

        temp_data[message.from_user.id][n] = answer
        users_data.data[str(user_id)]['n'] += 1
        n = users_data.data[str(user_id)]['n']
        question = test_all[lang][n]
        await send_test(question=question, message_id=message_id + 1,
                        user_id=user_id, n=n, lang=lang)


@dp.callback_query_handler(many_variants_callback.filter())
async def bot_echo_all(call: types.CallbackQuery, callback_data: dict):
    answer = callback_data.get('variant')
    lang = users_data.data[str(call.from_user.id)]['language']
    n = users_data.data[str(call.from_user.id)]['n']
    user_id = call.from_user.id

    if temp_data[call.from_user.id]['sub_mode']:
        sub_n = temp_data[user_id]['sub_n']
        question = sub_questions[lang][sub_n]
        if answer == 'complete':
            answer = temp_data[user_id].pop('choosed_vars')
            await sub_test_sender(user_id=user_id,
                                  message_id=call.message.message_id,
                                  answer=answer, lang=lang, n=n)
        else:
            if not temp_data[user_id].get('temp_vars', False):
                temp_data[user_id]['temp_vars'] = question[1:]
            temp_data[user_id]['choosed_vars'].append(
                temp_data[user_id]['temp_vars'].pop(int(answer)))
            await bot.edit_message_text(text=f'{sub_n}. {question[0][1:]}\n',
                                        chat_id=call.from_user.id,
                                        message_id=call.message.message_id,
                                        reply_markup=question_many_variants_creator(
                                            temp_data[user_id]['temp_vars'], lang=lang))

    else:
        question = test_all[lang][n]
        if answer == 'complete':
            n += 1
            question = test_all[lang][n]
            await send_test(question=question,
                            message_id=call.message.message_id,
                            user_id=call.from_user.id, n=n, lang=lang)

        else:
            temp_data[call.from_user.id][n].append(answer)
            ramaining_variants = question[1:] - temp_data[call.from_user.id][n]
            await bot.edit_message_text(text=f'{n}. {question[0][1:]}\n',
                                        chat_id=call.from_user.id,
                                        message_id=call.message.message_id,
                                        reply_markup=question_many_variants_creator(
                                            ramaining_variants, lang=lang))


@dp.callback_query_handler(variants_111_callback.filter())
async def bot_echo_all(call: types.CallbackQuery, callback_data: dict):
    answer = callback_data.get('answer')
    lang = users_data.data[str(call.from_user.id)]['language']
    n = users_data.data[str(call.from_user.id)]['n']
    sub_n = users_data.data[str(call.from_user.id)]['sub_n']
    cur_sub = temp_data[call.from_user.id]['cur_sub']
    temp_data[call.from_user.id][n][int(cur_sub)].append(answer)
    num_sub = temp_data[call.from_user.id]['num_sub']
    cur_sub = temp_data[call.from_user.id]['cur_sub']
    sub_n += 1

    if sub_n == len(sub_questions[lang]):
        cur_sub += 1
        sub_n = 1
    if cur_sub > num_sub:
        n += 1
        question = test_all[lang][n]
        await send_test(question=question, message_id=call.message.message_id,
                        user_id=call.from_user.id, n=n, lang=lang)
    else:
        question = sub_questions[lang][sub_n]
        await send_test(question=question, message_id=call.message.message_id,
                        user_id=call.from_user.id, n=n, lang=lang)


@dp.callback_query_handler(question_move_callback.filter(), state='*')
async def bot_echo_all(call: types.CallbackQuery, state: FSMContext):
    if users_data.data[str(call.from_user.id)]['n'] == 1:
        return

    lang = users_data.data[str(call.from_user.id)]['language']
    message_id = call.message.message_id
    user_id = call.from_user.id
    users_data.data[str(call.from_user.id)]['n'] -= 1
    n = users_data.data[str(call.from_user.id)]['n']
    question = test_all[lang][n]
    if question[0][0] == '6' or question[0][0] == '5':
        users_data.data[str(call.from_user.id)]['n'] += 1
        return
    if state:
        await state.finish()
    await send_test(question=question, message_id=message_id, user_id=user_id,
                    n=n, lang=lang)
