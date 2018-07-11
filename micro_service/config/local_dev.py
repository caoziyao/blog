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

    # redis
    driver = 'redis'
    redis_host = '127.0.0.1'
    redis_port = 6400
    redis_db = 0
    redis_password = 'kuaibiji123@Redis'
    redis_max_connect = 1024
    redis_auto_connect = 1
    redis_cluster = 0
    redis_cache_timeout = 5 * 60

    # service
    api_srv_port = 5001
    api_host = '0.0.0.0'
    api_port = 5002

    notebook_host = '0.0.0.0'
    notebook_port = 8004

    user_host = '0.0.0.0'
    user_port = 8005

    weixin_host = '0.0.0.0'
    weixin_port = 8006


