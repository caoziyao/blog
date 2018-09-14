# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/13 
@desc:
"""
import os

class EnvironmentConfig(object):

    # os.getenv
    # env_dist = os.environ

    APP_ENV = os.getenv('APP_ENV')
    ENV_FILE = os.getenv('ENV_FILE')
    MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')
