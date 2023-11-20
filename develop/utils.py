import json #импортируем модуль json


def get_data(filename):
    """функция чтения json файла"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data



