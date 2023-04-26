import os
from pypdf import PdfReader
from file_paths.file_paths import path_to_res


# TODO: оформить в тест, добавить проверки и использовать универсальный путь

def test_pdf_file():
    reader = PdfReader(os.path.join(path_to_res, 'docs-pytest-org-en-latest.pdf'))
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    print(page)
    print(number_of_pages)
    print(text)

    assert number_of_pages == 412
