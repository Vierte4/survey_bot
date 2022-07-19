from data.config import *
from keyboards.inline.test_part1_keyboard import *
from keyboards.inline.test_part2_keyboard import *
from loader import bot
from states.all_state import Answer


async def send_test(question, message_id, user_id, n, lang, answer=None):
    msg_txt = '✏️Отправьте ответ сообщением' if lang == 'ru' else '✏️Жауапты хабарламамен жіберіңіз'
    if temp_data[user_id]['sub_mode']:
        back = False
    else:
        back = True
    if question[0][0] == '5':
        try:
            await bot.edit_message_text(text=f'{n}. {question[0][1:]}',
                                        chat_id=user_id,
                                        message_id=message_id)
        except:
            await bot.send_message(text=f'{n}. {question[0][1:]}',
                                   chat_id=user_id)
        temp_data[user_id]['cur_sub'] = 11
        question = extra_food[lang][1]
        temp_data[user_id]['extra_n'] = 1
        temp_data[user_id]['num_sub'] = 9 + len(extra_food[lang])
        temp_data[user_id]['sub_mode'] = True
        temp_data[user_id][n] = {}

        await bot.send_message(text=f'{question[0]}',
                               chat_id=user_id,
                               reply_markup=question_extra_creator(question,
                                                                   back=False))
    elif question[0][0] == '6':
        try:
            await bot.edit_message_text(text=f'{n}. {question[0][1:]}',
                                        chat_id=user_id,
                                        message_id=message_id)
        except:
            await bot.send_message(text=f'{n}. {question[0][1:]}',
                                   chat_id=user_id)
        temp_data[user_id]['food_mod'] = True
        temp_data[user_id]['food_n'] = 1
        temp_data[user_id][n] = {}
        question = food[lang][1]

        await bot.send_message(text=f'1. {question}',
                               chat_id=user_id,
                               reply_markup=food_creator(food_questions[lang],
                                                         back=back))


    elif len(question) == 1:
        await Answer.openanswer.set()
        if back:
            try:
                await bot.edit_message_text(
                    text=f'{n}. {question[0]}\n' + msg_txt,
                    chat_id=user_id,
                    message_id=message_id,
                    reply_markup=back_create())
            except:
                await bot.send_message(text=f'{n}. {question[0]}\n' + msg_txt,
                                       chat_id=user_id,
                                       reply_markup=back_create())
            return
        try:
            await bot.edit_message_text(text=f'{n}. {question[0]}\n' + msg_txt,
                                        chat_id=user_id,
                                        message_id=message_id)
        except:
            await bot.send_message(text=f'{n}. {question[0]}\n' + msg_txt,
                                   chat_id=user_id)
    elif question[0][0] == '1':
        try:
            await bot.edit_message_text(text=f'{n}. {question[0][1:]}\n',
                                        chat_id=user_id,
                                        message_id=message_id,
                                        reply_markup=question_yesno_creator(
                                            question, back=back))
        except:
            await bot.send_message(text=f'{n}. {question[0][1:]}\n',
                                   chat_id=user_id,
                                   reply_markup=question_yesno_creator(
                                       question, back=back))
    elif question[0][0] == '2':
        try:
            await bot.edit_message_text(text=f'{n}. {question[0][1:]}\n',
                                        chat_id=user_id,
                                        message_id=message_id,
                                        reply_markup=question_many_variants_creator(
                                            question[1:], lang=lang))
        except:
            await bot.send_message(text=f'{n}. {question[0][1:]}\n',
                                   chat_id=user_id,
                                   reply_markup=question_many_variants_creator(
                                       question[1:], lang=lang))
        temp_data[user_id]['temp_vars'] = []
        temp_data[user_id]['choosed_vars'] = []
        n -= 1

    elif question[0][0] == '3':
        try:
            await bot.edit_message_text(text=f'{n}. {question[0][1:]}',
                                        chat_id=user_id,
                                        message_id=message_id,
                                        reply_markup=skip_question_creator(
                                            question, back=back))
        except:
            await bot.send_message(text=f'{n}. {question[0][1:]}',
                                   chat_id=user_id,
                                   reply_markup=skip_question_creator(
                                       question, back=back))

    elif question[0][0] == '4':
        try:
            await bot.edit_message_text(text=f'{n}. {question[0][1:]}',
                                        chat_id=user_id,
                                        message_id=message_id,
                                        reply_markup=get_sub_number(question,
                                                                    back=back))
        except:
            await bot.send_message(text=f'{n}. {question[0][1:]}',
                                   chat_id=user_id,
                                   reply_markup=get_sub_number(question,
                                                               back=back))

    else:
        try:
            await bot.edit_message_text(text=f'{n}. {question[0]}',
                                        chat_id=user_id,
                                        message_id=message_id,
                                        reply_markup=question_creator(question,
                                                                      back=back))
        except:
            await bot.send_message(text=f'{n}. {question[0]}',
                                   chat_id=user_id,
                                   reply_markup=question_creator(question,
                                                                 back=back))


async def sub_test_sender(user_id, message_id, answer, lang, n):
    sub_n = temp_data[user_id]['sub_n']
    num_sub = temp_data[user_id]['num_sub']
    cur_sub = temp_data[user_id]['cur_sub']
    temp_data[user_id][n][int(cur_sub)].append(answer)
    temp_data[user_id]['sub_n'] += 1
    sub_n += 1

    if sub_n == len(sub_questions[lang]):
        temp_data[user_id]['cur_sub'] += 1
        cur_sub += 1
        if temp_data[user_id]['extra_n'] and cur_sub <= num_sub:
            temp_data[user_id]['extra_n'] += 1
            question = extra_food[lang][temp_data[user_id]['extra_n']]
            try:
                await bot.edit_message_text(text=f'{question[0]}',
                                            chat_id=user_id,
                                            message_id=message_id,
                                            reply_markup=question_extra_creator(
                                                question, back=False))
            except:
                await bot.send_message(text=f'{question[0]}',
                                       chat_id=user_id,
                                       reply_markup=question_extra_creator(
                                           question, back=False))
            return

        sub_n = temp_data[user_id]['sub_n'] = 1
    if cur_sub > num_sub:
        temp_data[user_id]['sub_mode'] = False
        users_data.data[str(user_id)]['n'] += 1
        n += 1
        question = test_all[lang][n]
        await send_test(question=question, message_id=message_id,
                        user_id=user_id, n=n, lang=lang)
    else:
        msg_txt = 'Прием пищи' if lang == 'ru' else 'Тамақтану'
        if temp_data[user_id]['sub_n'] == 1 and not temp_data[user_id][
            'extra_n']:
            await bot.edit_message_text(message_id=message_id, chat_id=user_id,
                                        text=msg_txt+f' {cur_sub}')
            await bot.send_message(chat_id=user_id,
                                   text='Вопрос грузится')
            message_id += 1
        question = sub_questions[lang][sub_n]
        await send_test(question=question, message_id=message_id,
                        user_id=user_id, n=sub_n,
                        answer=answer,
                        lang=lang)
