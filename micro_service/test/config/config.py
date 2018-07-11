# coding: utf-8

import os
from pathlib import Path

# current = os.path.abspath(os.path.curdir)
# path_test_data = os.path.join(current, 'test_data')

root = Path.absolute(Path.cwd())
path_test_data = root.joinpath('test_data')
path_output = root.joinpath('output')
host = 'http://127.0.0.1:5000'

