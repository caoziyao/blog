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

from python_app import AppPyService
from notebook import AppNotebookService
from user import AppUserService
from config.log import debug_log


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
        'user': AppUserService,
    }
    if l == 2:
        s = argv[1]
        Api = args.get(argv[1])
        if Api is not None:
            # debug_log.info('running {}...'.format(s))
            Api().run()

    else:
        # error
        pass


if __name__ == "__main__":
    main()
