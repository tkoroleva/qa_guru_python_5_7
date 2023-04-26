import os
import csv
from file_paths.file_paths import path_to_res


# TODO: оформить в тест, добавить проверки и использовать универсальный путь

def test_csv_file():
    path_to_csv = os.path.join(path_to_res, 'eggs.csv')
    with open(path_to_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(path_to_csv) as csvfile:
        csvreader = csv.reader(csvfile)
        csv_list = []
        for row in csvreader:
            csv_list.append(row)
            print(row)

    assert csv_list[1] == ['Alex', 'Serj', 'Yana']
