import json #импортируем модуль json


def get_data(filename):
    """функция чтения json файла"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data



def get_operations_executed(data):
    """функция которая выделяет операции со статусом EXECUTED"""
    operations_executed = []
    for operation in data:
        if 'state' in operation and operation['state'] == 'EXECUTED':
            operations_executed.append(operation)
    operation_with_from = []
    for operation in operations_executed:
        if 'from' in operation:
            operation_with_from.append(operation)
    return operation_with_from



def get_last_num_operations(operation_with_from, num_of_operations):
    """функция фильтровки пяти последних операций"""
    operations_sort = sorted(operation_with_from, key=lambda operation: operation["date"], reverse=True)
    last_five_operations = operations_sort[0:num_of_operations]
    return last_five_operations


