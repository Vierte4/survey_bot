import apiclient
import httplib2
from oauth2client.service_account import ServiceAccountCredentials

# Читаем ключи из файла
from data.config import CREDENTIALS_FILE, spreadsheetId, email, \
    test_ru

# Имя файла с закрытым ключом, вы должны подставить свое

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               [
                                                                   'https://www.googleapis.com/auth/spreadsheets',
                                                                   'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())  # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4',
                                    http=httpAuth)  # Выбираем работу с таблицами и 4 версию API

driveService = apiclient.discovery.build('drive', 'v3',
                                         http=httpAuth)  # Выбираем работу с Google Drive и 3 версию API
access = driveService.permissions().create(
    fileId=spreadsheetId,
    body={'type': 'user', 'role': 'writer', 'emailAddress': email},
    # Открываем доступ на редактирование
    fields='id'
).execute()


def append_to_sheet(data, list_name):
    results = service.spreadsheets().values().append(
        spreadsheetId=spreadsheetId,
        range=f"{list_name}!A1",
        valueInputOption="RAW",
        body={
            'values': data
        }).execute()


def results_to_table(results, user_id):
    main_q = [user_id]
    extra_q = []
    food_q = [user_id]
    for a in range(1, len(test_ru)):
        if a not in results.keys():
            continue
        if test_ru[a][0][0] == '5' or test_ru[a][0][0] == '4':
            if a in results.keys():
                for b in results[a].values():
                    if b == [] or b[0] == 'Нет':
                        continue
                    xx = [user_id]
                    for c in b:
                        if type(c) == list:
                            c = ', '.join(c)
                        xx.append(str(c))
                    extra_q.append(xx)
        elif test_ru[a][0][0] == '6':
            for b in results[a].values():
                food_q.append(b)
        else:
            main_q.append(str(results[a]))

    append_to_sheet(extra_q, list_name='Приёмы пищи')
    append_to_sheet([food_q], list_name='Виды пищи')
    append_to_sheet([main_q], list_name='Основные вопросы')
