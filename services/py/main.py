# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/10
@desc:
"""

import sys
import os

# sys.path.append(os.path.join(os.path.abspath(__file__), '..', '..'))
# print(os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..')))

# from py.api_kuaibiji.app import ApiService
# from py.api_test import ApiTestService
# from py.notebook import AppNotebookService
from python_app import AppPyService
from notebook import AppNotebookService

def default_run():
    print('default_run')


def main():
    argv = sys.argv
    l = len(argv)

    args = {
        # 'api_kuaibiji': ApiService,
        # 'api_test': ApiTestService,
        # 'notebook': AppNotebookService,
        'py': AppPyService,
        'notebook': AppNotebookService,
    }
    if l == 2:
        print('argv', argv)
        Api = args.get(argv[1])
        print('api', Api)
        if Api is not None:
            Api().run()

    else:
        # error
        pass


if __name__ == "__main__":
    main()