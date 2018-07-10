# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6
@desc:
"""
from .default import DefaultConfig


class LocalDevConfig(DefaultConfig):
    debug = True

    # mongodb
    mongodb_host = '47.75.156.182'
    mongodb_port = 27017
    mongodb_admin = 'admin'
    mongodb_db_name = 'kuaibi'
    mongodb_username = 'root'
    mongodb_password = 'test@123'

    # service
    api_srv_port = 5001
    api_host = '0.0.0.0'
    api_port = 5002

    notebook_host = '0.0.0.0'
    notebook_port = 8004

    user_host = '0.0.0.0'
    user_port = 8005
