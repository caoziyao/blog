# coding: utf-8

import redis
import random
from app.config import Config as conf

class Redis(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Redis, cls).__new__(cls)
        return cls._instance

    def __init__(self, host, port, password, db):
        pool = redis.ConnectionPool(host=host, port=port, password=password, db=db)
        self.rdsclient = redis.Redis(connection_pool=pool)
        testKey = "testKey%s" % random.randint(1, 100)
        self.rdsclient.set(testKey, "test redis ok")
        self.rdsclient.delete(testKey)
        print('test redis ok')


redis_client = Redis(
    conf.redis_host,
    conf.redis_port,
    conf.redis_password,
    conf.redis_db).rdsclient