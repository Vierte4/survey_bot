import json
import os


class Data():
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = self.get_data()

    def update_data(self):
        with open(self.data_path, 'w', encoding='utf-8') as f:
            f.write(f'{json.dumps(self.data, ensure_ascii=False, indent=4)}')
            f.close()

    def get_data(self):
        print(os.getcwd())
        with open(self.data_path, 'r',
                  encoding='utf-8') as f:
            data = json.load(f)
            f.close()
        return data

if __name__ == '__main__':
    aa = Data(r'C:\Programming\Хакатон\Тимфорс\data\users.json')
    print(aa.data)
    print(aa.data_path)
    aa.data = {'319503958': 'Asad'}
    print(aa.data)
    aa.update_data()
    print(aa.data)
