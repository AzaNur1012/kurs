from develop import utils

def test_get_data():
    """тест на функцию чтения json файла """
    assert len(utils.get_data('operations.json')[0]) > 0



def test_get_operations_executed(test_data):
    """тест на функцию фильтрации операций со статусом EXECUTED"""
    assert len(utils.get_operations_executed(test_data)) == 2



def test_get_last_num_operations(test_data):
    """тест на функцию фильтровки и сортировки пяти последних операций"""
    assert len(utils.get_last_num_operations(test_data, 4)) == 4
    assert utils.get_last_num_operations(test_data, 4)[0]['date'] == '2023-07-03T18:35:29.512364'







