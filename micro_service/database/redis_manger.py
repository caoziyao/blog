# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/12 
@desc:
"""

import time
import redis
import random
import json
import math
import logging
from config import option

# from src.models import DataCacheBase
# from .init_data_cache import client

logger = logging.getLogger('dblog')


class RedisClient(object):
    _instance = None
    default_retry_count = 2

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(RedisClient, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        host = option.redis_host
        port = option.redis_port
        # password = option.redis_password
        db = option.redis_db

        # pool = redis.ConnectionPool(host=host, port=port, password=password, db=db)
        pool = redis.ConnectionPool(host=host, port=port, db=db)
        self.client = redis.Redis(connection_pool=pool)
        testKey = "testKey%s" % random.randint(1, 100)
        self.client.set(testKey, "test redis ok")
        self.client.delete(testKey)
        logger.info('test redis ok')


class RedisManager(object):
    _instance = None
    default_retry_count = 1

    def __init__(self):
        self.client = RedisClient().client
        self.expire_time = option.redis_cache_timeout

    def lock(self, lock_key):
        # model = DataCacheBase()
        # e = model.set(lock_key, "x", ex=self.default_retry_count, nx=True)
        # EX second ：设置键的过期时间为 second 秒, NX ：只在键不存在时，才对键进行设置操作
        e = self.client.set(lock_key, "x", ex=self.default_retry_count, nx=True)
        return e

    def get_bylock(self, key):
        """
        避免redis超时时的惊群现象，请必须配合 `set_bylock` 使用
        调用方法与`get`一样
        用法：
        cache_data = get_bylock(cache_id)
        if not cache_data:
            set_bylock(
                cache_id,
                json.dumps(data),
                config.CACHE_ID_PRODUCT_DETAIL_CACHE
            )
        """
        lock_key = key + ".lock"

        # model = DataCacheBase()
        # data = model.get(key)
        data = self.client.get(key)
        current = int(time.time())
        if data:
            real_data = json.loads(data)
            # 如果人为设置的超时时间超时了
            if real_data['expireat'] <= current:
                if self.lock(lock_key):
                    return None
                else:
                    # 如果没获取到锁
                    return real_data['data']
            else:
                return real_data['data']
        else:
            return None

    def set_bylock(self, key, data, expire_time=option.redis_cache_timeout):
        """
        避免redis超时时的惊群现象，请必须配合`get_bylock`使用
        调用方法与`setex`一样
        """
        self.expire_time = expire_time
        current = int(time.time())
        expireat = current + expire_time - math.ceil(expire_time / 4)
        real_data = {
            'data': data,
            'expireat': expireat,
        }
        # model = DataCacheBase()
        # model.setex(key, json.dumps(real_data), expire_time)
        self.client.setex(key, json.dumps(real_data), expire_time)
        lock_key = key + ".lock"
        self.client.delete(lock_key)

    def delete(self, key):
        """
        删除key
        :return:
        """
        # model = DataCacheBase()
        # model.delete(key)
        self.client.delete(key)


redis_client = RedisManager()
