from develop import utils

def test_get_data():
    """тест на функцию чтения json файла """
    assert len (utils.get_data('operations.json')[0]) > 0



def test_get_operations_executed(test_data):
    """тест на функцию фильтрации операций со статусом EXECUTED"""
    assert len (utils.get_operations_executed(test_data)) == 2








