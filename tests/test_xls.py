import os
import xlrd
from file_paths.file_paths import path_to_res


# TODO: оформить в тест, добавить проверки и использовать универсальный путь

def test_xls_file():
    book = xlrd.open_workbook(os.path.join(path_to_res, 'file_example_XLS_10.xls'))
    print(f'Количество листов {book.nsheets}')
    assert book.nsheets == 1

    print(f'Имена листов {book.sheet_names()}')
    assert book.sheet_names() == ['Sheet1']

    sheet = book.sheet_by_index(0)
    print(f'Количество столбцов {sheet.ncols}')
    assert sheet.ncols == 8

    print(f'Количество строк {sheet.nrows}')
    assert sheet.nrows == 10

    print(f'Пересечение строки 9 и столбца 1 = {sheet.cell_value(rowx=9, colx=1)}')
    assert sheet.cell_value(rowx=9, colx=1) == 'Vincenza'

    # печать всех строк по очереди
    for rx in range(sheet.nrows):
        print(sheet.row(rx))
