# coding:utf-8

import os
import json

# gunicorn配置
bind = '0.0.0.0:3000'                                  # 绑定的ip已经端口号
timeout = 60                                             # 超时 1 分钟
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'  # 设置gunicorn访问日志格式，错误日志无法设置
accesslog = "/dev/null"                                  # 访问日志文件的路径
errorlog = "./log/gunicorn_errorlog.log"                 # 错误日志文件的路径
pidfile = "./log/gunicorn.pid"
# pythonpath = '/Users/Shared/github/wiki'

#启动的进程数
# workers = multiprocessing.cpu_count() * 2 + 1            # 进程数(子进程共享了父进程的文件句柄,多进程共用一个 fd 的情况下使用 logging 模块写少量日志是进程安全的)
workers = 4
threads = 2                                              # 指定每个进程开启的线程数
backlog = 512                                            # 监听队列
