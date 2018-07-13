# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/10 
@desc:
"""
import grpc
from .app_run import app, app_config

from concurrent import futures
from config import option


class ApiService(object):

    def __init__(self):
        pass

    def run(self):
        config = app_config()
        print('http://{}:{}'.format(config['host'], config['port']))
        app.run(**config)
