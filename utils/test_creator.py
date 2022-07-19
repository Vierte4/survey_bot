def test_creator(directory):
    # Вовзращает список списков, построенный на основе полученного файла. Сначала файл делится на списки, резделитель
    # отступ между строками, затем списки делятся на строки, разделитель - новая строка
    with open(directory, encoding='UTF-8') as f:
        content = f.read()
    gg = []
    for g in content.split('\n\n'):
        g = g.split('\n')
        gg.append(g)
    return gg


def file_reader(directory):
    with open(directory, encoding='UTF-8') as f:
        content = f.read()
    return content



def variants_creator(path):
    # Вовзращает список списков, построенный на основе полученного файла. Сначала файл делится на списки, резделитель
    # 2 отступа между строками
    with open(path, encoding='UTF-8') as f:
        content = f.read()
    return content.split('\n')



