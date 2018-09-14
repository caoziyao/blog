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

# from python_app import AppPyService
from notebook import AppNotebookService
from user import AppUserService
from weixin import AppWeixinService


def default_run():
    print('default_run')


def main():
    argv = sys.argv
    l = len(argv)

    args = {
        'notebook': AppNotebookService,
        'user': AppUserService,
        'weixin': AppWeixinService,
    }
    if l == 2:
        s = argv[1]
        Api = args.get(argv[1])
        if Api is not None:
            Api().run()

    else:
        # todo
        pass


if __name__ == "__main__":
    # main()
    pass