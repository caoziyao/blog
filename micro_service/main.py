# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/10 
@desc:
"""
import os
from common.logger import log
from micro_services.api_kuaibiji import ApiService
from micro_services.notebook import App as app_notebook

from micro_services.user import App as app_user
from micro_services.weixin import App as app_weixin
from multiprocessing import Pool


def run_weixin(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    s = app_weixin()
    s.run()


def run_user(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    s = app_user()
    s.run()


def run_api(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    s = ApiService()
    s.run()


def run_notebook(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    s = app_notebook()
    s.run()


def main():
    # 3表示进程池中最多有三个进程一起执行
    pool = Pool(5)
    pool.apply_async(run_user, ('run_user',))
    pool.apply_async(run_notebook, ('run_notebook',))
    pool.apply_async(run_weixin, ('run_weixin',))
    # pool.apply_async(run_api, ('run_api',))

    pool.close()  # 关闭进程池
    pool.join()  # 主进程在这里等待，只有子进程全部结束之后，在会开启主线程


if __name__ == '__main__':
    main()
