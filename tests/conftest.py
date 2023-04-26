import os
import pytest
from file_paths.file_paths import path_to_tmp


@pytest.fixture
def create_tmp():
    if not os.path.exists(path_to_tmp):
        os.mkdir(path_to_tmp)

    yield

    os.rmdir(path_to_tmp)
