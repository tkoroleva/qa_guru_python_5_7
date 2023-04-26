import os


root_path = os.path.dirname(os.path.abspath(__file__))
path_to_res = os.path.abspath(os.path.join(root_path, '../res'))
path_to_tmp = os.path.abspath(os.path.join(root_path, '..', 'tmp'))
path_to_archive = os.path.abspath(os.path.join(path_to_tmp, 'archive.zip'))
