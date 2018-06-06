# coding: utf-8

import json
import math
import random
import time

import redis

from micro_services.mznv.config import Config as conf


class Redis():
    _instance = None
    default_retry_count = 2

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

    def lock(self, lock_key):
        e = self.rdsclient.set(lock_key, "x", ex=self.default_retry_count, nx=True)
        return e

    def get_bylock(self, key):
        """
        避免redis超时时的惊群现象，请必须配合 `set_bylock` 使用

        调用方法与`get`一样
        """
        lock_key = key + ".lock"

        data = self.rdsclient.get(key)
        current = int(time.time())
        if data:
            real_data = json.loads(data)
            # 如果人为设置的超时时间超时了
            if real_data['expireat'] <= current:
                # EX second ：设置键的过期时间为 second 秒, NX ：只在键不存在时，才对键进行设置操作
                if self.lock(lock_key):
                    # 如果获取到锁
                    return None
                else:
                    # 如果没获取到锁
                    return real_data['data']
            else:
                return real_data['data']
        else:
            return None


    def set_bylock(self, key, data, expire_time):
        """
        避免redis超时时的惊群现象，请必须配合`get_bylock`使用

        调用方法与`setex`一样
        """
        current = int(time.time())
        expireat = current + expire_time - math.ceil(expire_time / 2)
        real_data = {
            'data': data,
            'expireat': expireat,
        }
        self.rdsclient.setex(key, json.dumps(real_data), expire_time)
        lock_key = key + ".lock"
        self.rdsclient.delete(lock_key)


redis_client = Redis(
    conf.redis_host,
    conf.redis_port,
    conf.redis_password,
    conf.redis_db)