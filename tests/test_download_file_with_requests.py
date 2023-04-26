import os.path
import requests
from file_paths.file_paths import path_to_tmp


def test_download_file_with_requests():
    # TODO: сохранять и читать из tmp, использовать универсальный путь

    url = 'https://selenium.dev/images/selenium_logo_square_green.png'
    tmp = os.path.join(path_to_tmp, 'selenium_logo.png')
    r = requests.get(url)
    with open(tmp, 'wb') as file:
        file.write(r.content)
    size = os.path.getsize(tmp)

    print(size)
    assert size == 30803

    os.remove(tmp)
    os.rmdir(path_to_tmp)
