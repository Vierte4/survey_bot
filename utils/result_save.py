import json
from data.config import results_path, temp_data
from utils.google_sheets_api import results_to_table


def save_result(user_id):
    added_data = temp_data.pop(user_id)

    for a in ['extra_n', 'sub_mode', 'sub_n', 'num_sub', 'cur_sub', 'food_mod', 'food_n'
              ,'temp_vars']:
        added_data.pop(a)

    with open(results_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    data[user_id]=added_data
    with open(results_path, 'w', encoding='utf-8') as f:

        f.write(f'{json.dumps(data, ensure_ascii=False, indent=4)}')
        f.close()

    results_to_table(results=added_data, user_id=user_id)
