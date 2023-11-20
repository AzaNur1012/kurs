from develop import utils

def test_get_data():
    """тест на функцию чтения json файла """
    assert len (utils.get_data('operations.json')[0]) > 0





