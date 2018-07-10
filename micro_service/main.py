# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/10 
@desc:
"""
from micro_services.api import ApiService
from micro_services.notebook import NotebookService
from common.logger import log
from micro_services.user import UserService
from multiprocessing import Pool
import os
import random
import time


# def worker(num):
#     for i in range(5):
#         print('===pid=%d==num=%d=' % (os.getpid(), num))
#         time.sleep(1)
#
#
#
#
# # 子进程要执行的代码
# def run_proc(name):
#

def run_user(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    s = UserService()
    s.run()


def run_api(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    s = ApiService()
    s.run()


def run_notebook(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    s = NotebookService()
    s.run()


def main():
    # 3表示进程池中最多有三个进程一起执行
    pool = Pool(5)
    pool.apply_async(run_user, ('run_user',))
    pool.apply_async(run_notebook, ('run_notebook',))
    pool.apply_async(run_api, ('run_api',))

    pool.close()  # 关闭进程池
    pool.join()  # 主进程在这里等待，只有子进程全部结束之后，在会开启主线程


if __name__ == '__main__':
    main()
