import os
import zipfile
from file_paths.file_paths import path_to_res, path_to_archive, path_to_tmp


def test_archive(create_tmp):
    file_dir = os.listdir(path_to_res)
    with zipfile.ZipFile(path_to_archive, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.join(path_to_res, file)
            zf.write(add_file, file)

    file_dict = {'about_the_truth.pdf': 7589,
                 'docs-pytest-org-en-latest.pdf': 1739253,
                 'eggs.csv': 34,
                 'file_example_XLSX_50.xlsx': 7360,
                 'file_example_XLS_10.xls': 8704,
                 'personal_data.csv': 105,
                 'x-file.xlsx': 5027}

    with zipfile.ZipFile(path_to_archive, 'r') as zf:
        for item in zf.infolist():
            print(f'File Name: {item.filename} Size: {item.file_size}')
            assert item.file_size == file_dict.get(item.filename)

    os.remove(path_to_archive)
