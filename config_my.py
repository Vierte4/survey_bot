from utils.temp_db import Data
from utils.test_creator import test_creator, variants_creator

CREDENTIALS_FILE = 'data/genuine-flight-345616-0896c75625bf.json'
spreadsheetId= '1MjDD36flFzObpjizW1vM9-cH8wlUoKDxAZWGmNb-ThE'
email = 'argut.98@gmail.com' # почта с доступом к редактированию таблицы

BOT_TOKEN = "5374061200:AAH4ssq2Hqcg1fvI3PCid6aVLpYLb9pYmAI"
ADMINS = ['319503958', ] # список админов через запятую, каждая запись в ''

results_path = 'data/results.json' # имя файла с результатами

"""Имена файлов с вопросами и вариантами ответов"""

users_data_path = r'data/user_data.json'
agreement_ru_path = 'data/Cоглашение на русском.txt'
agreement_kz_path = 'data/соглашение на казахском.txt'

test_ru_path = 'data/Вопросы на русском.txt'
test_kz_path = 'data/Вопросы на казахском.txt'

sub_questions_ru_path = 'data/Приёмы пищи на русском.txt'
sub_questions_kz_path = 'data/Приёмы пищи на казахском.txt'

food_ru_path = 'data/Виды пищи на русском.txt'
food_kz_path = 'data/Виды пищи на казахском.txt'

food_questions_ru_path = 'data/Вопросы к видам пищи на русском.txt'
food_questions_kz_path = 'data/Вопросы к видам пищи на казахском.txt'

extra_food_ru_path = 'data/Доп приёмы пищи на русском.txt'
extra_food_kz_path = 'data/Доп приёмы пищи на казахском.txt'

users_data = Data(users_data_path)
test_ru = test_creator(test_ru_path)
test_kz = test_creator(test_kz_path)

sub_questions_ru = test_creator('data/Приёмы пищи на русском.txt')
sub_questions_kz = test_creator('data/Приёмы пищи на казахском.txt')

food_ru = variants_creator('data/Виды пищи на русском.txt')
food_kz = variants_creator('data/Виды пищи на казахском.txt')

food_questions_ru = variants_creator('data/Вопросы к видам пищи на русском.txt')
food_questions_kz = variants_creator('data/Вопросы к видам пищи на казахском.txt')

extra_food_ru = test_creator('data/Доп приёмы пищи на русском.txt')
extra_food_kz = test_creator('data/Доп приёмы пищи на казахском.txt')

temp_data = {}
test_all = {'ru':test_ru, 'kz':test_kz}
extra_food = {'ru':extra_food_ru, 'kz':extra_food_kz}
sub_questions = {'ru':sub_questions_ru, 'kz':sub_questions_kz}
food = {'ru':food_ru,'kz':food_kz}
food_questions = {'ru':food_questions_ru, 'kz':food_questions_kz}