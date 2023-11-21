import json #импортируем модуль json
from datetime import datetime #импортируем модуль работы с датой

def get_data(filename):
    """функция чтения json файла"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data



def get_operations_executed(data):
    """функция которая выделяет операции со статусом EXECUTED"""
    return [operation for operation in data if operation.get('state') == "EXECUTED"]




def get_last_num_operations(operation_with_from, num_of_operations):
    """функция фильтровки пяти последних операций"""
    operations_sort = sorted(operation_with_from, key=lambda operation: operation["date"], reverse=True)
    last_five_operations = operations_sort[0:num_of_operations]
    return last_five_operations



def get_operations_formatted(last_five_operations):
    """функция вывода данных в отформатированном виде"""
    operations_formatted_list = []
    for operation in last_five_operations:
        date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = operation['description']
        payer_info, payment_method = "", ""
        if "from" in operation:
            payer = operation["from"].split()
            payment_method = payer.pop(-1)
            if payer[0] == 'Счет':
                payment_method_from = f"**{payment_method[-4:]}"
            else:
                payment_method_from = f"{payment_method[:4]} {payment_method[4:6]}** *** {payment_method[-4:]}"
            payer_info = " ".join(payer)
        else:
            payment_method_from = ""
        recipient = f"{operation['to'].split()[0]} **{operation['to'][-4:]}"
        operation_amount = f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"
        operations_formatted_list.append(f"""
            {date} {description}
            {payer_info} {payment_method_from}->{recipient}
            {operation_amount}""")
    return operations_formatted_list


