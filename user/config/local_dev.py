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
    host = '0.0.0.0'
    port = '8005'

    # mongodb
    mongodb_host = '47.75.156.182'
    mongodb_port = 27017
    mongodb_admin = 'admin'
    mongodb_db_name = 'kuaibiji_user'
    mongodb_username = 'root'
    mongodb_password = 'test@123'
