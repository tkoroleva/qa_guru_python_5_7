import time
import os
from selenium import webdriver
from selene import browser
from file_paths.file_paths import path_to_tmp


# TODO: оформить в тест, добавить проверки и использовать универсальный путь к tmp

def test_download_file_with_browser(create_tmp):
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": path_to_tmp,
        "download.directory_upgrade": True,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(7)

    print(os.path.getsize(os.path.join(path_to_tmp, 'pytest-main.zip')))
    assert os.path.getsize(os.path.join(path_to_tmp, 'pytest-main.zip')) > 100
    tmp = os.path.join(path_to_tmp, 'pytest-main.zip')
    os.remove(tmp)
